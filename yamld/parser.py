from itertools import chain
import warnings
import re
import ast
import yaml
from .common import _is_dataset_heading

#TODO literal_eval and replace none
none_pattern = re.compile(r"\bnull\b")

def _eval(val):
    val = val.strip()
    if val == "null":
        return None
    else:
        return ast.literal_eval(val)

def parse(entry):
    islist = entry[0].strip()[0] == '-'
    entry = [_eval(line[2 if islist else line.find(':') + 1:].strip())
             for line in entry]
    return entry

    
def parse_feature_names_if_exist(entry):
    islist = entry[0].strip()[0] == '-'
    if islist:
        return None
    keys = [line[:line.find(':')].strip() 
             for line in entry]
    return keys

def parse_meta(lines):
    lines = iter(lines)
    #parse meta
    metadata = ""
    first = True
    tmp = []
    for line in lines:
        if not line.strip():
            continue
        if first and line.lstrip().startswith('-'):
            tmp.append(line)
            break
        first = False
        if _is_dataset_heading(line):
            tmp.append(line)
            break
        metadata += line + '\n'
    
    metadata = yaml.safe_load(metadata) if metadata else None 
    lines = chain(tmp, lines)
    return metadata, lines


def _process_dataset_line(line, tab=0, front = None):
    line =  line[tab + 2:].strip()  #remove first '- '
    if line[:2] == '- ': #check second '- ' 
        return line[2:], None, False
    else:
        split = line.split(':', 1)
        return split[0], split[1], True
    

def _get_feature_names_and_indent(lines):
    lines = iter(lines)
    lines = _skip_to_dataset(lines)
    tmp = []
    indent_idx = None
    feature_names = None
    entry = []
    for line in lines:
        if line.strip():
            tmp.append(line)
            if indent_idx == None:
                indent_idx = line.find('-')
                assert indent_idx != None
            elif line[indent_idx] == '-':
                feature_names = parse_feature_names_if_exist(entry)
                entry = []
                break
            if not entry and line[indent_idx+1:].lstrip().startswith('-'):
                #first char
                feature_names = None
                break
            entry.append(line[indent_idx+2:])
    lines = chain(tmp, lines)
    return feature_names, len(entry), indent_idx, lines

def _skip_to_dataset(lines):
    #skip meta data if any
    tmp = []
    is_first = True
    for line in lines:
        strp_line = line.strip()
        if strp_line:
            if is_first and strp_line.startswith('-'):
                tmp.append(line)
                break
            is_first = False
            if _is_dataset_heading(line):
                break

    lines = chain(tmp, lines)
    return lines
    #DONE meta
        
def parse_dataset(lines):
    lines = _skip_to_dataset(lines)
    _, _, tab, lines = _get_feature_names_and_indent(lines)

    lines = iter(lines)
    entry = []
    #read first line to avoid extra is_first checks
    for line in lines:
        if line.strip():
            entry.append(line[tab+2:].strip())
            break

    #start dataset
    for line in lines:
        if line.strip():
            if line[tab] == '-':
                yield parse(entry)
                entry = []

            entry.append(line[tab+2:].strip())
    if entry:
        yield parse(entry)