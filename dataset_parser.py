from itertools import chain
import yaml

def parse(entry):
    if not entry:
        return None
    islist = entry[0].strip()[0] == '-'
    entry = map(lambda x: x.strip(), entry)
    entry = [line[2 if islist else line.find(':') + 1:].strip() 
             for line in entry]
    print(entry)
    
def parse_feature_names_if_exist(entry):
    islist = entry[0].strip()[0] == '-'
    if islist:
        return None
    keys = [line[:line.find(':')].strip() 
             for line in entry]
    print('FEATURES: ', keys)

def parser(lines):
    lines = iter(lines)
    #parse meta
    metadata = ""
    for line in lines:
        if not line.strip():
            continue
        if line.startswith('dataset'):
            break
        metadata += line + '\n'
    metadata = yaml.safe_load(metadata) 
    print('meta -- ' , metadata)
    
    #DONE meta


    #read meta data
    tab = None
    dim = None
    feature_names = None
    entry = []
    
    tmp = []
    for line in lines:
        tmp.append(line)
        if not line.strip():
            continue
        if not tab:
            tab = line.find('-')
        elif line[tab] == '-':
            feature_names = parse_feature_names_if_exist(entry)
            dim = len(entry)
            entry = []
            break
        entry.append(line[tab+2:])
    #done read meta

    lines = chain(tmp, lines)

    #start dataset
    for line in lines:
        if not line.strip():
            continue
        if line[tab] == '-':
            parse(entry)
            entry = []
        entry.append(line[tab+2:])
            
    parse(entry)

if __name__ == '__main__':
    test = """
key: meta_val
dataset:

   -  key: val1
      key: val2
   -  - testy
      - testttot
   -  - tamsty
            """
            
    parser(test.split('\n'))
