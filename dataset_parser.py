def parse(entry):
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
    tab = None
    is_first_entry = True
    feature_names = None
    entry = []
    for line in lines:
        if not line.strip():
            continue
        if not tab:
            tab = line.find('-')
        
        elif line[tab] == '-':
            parse(entry)
            if is_first_entry:
                feature_names = parse_feature_names_if_exist(entry)
                is_first_entry = False
            entry = []
        entry.append(line[tab+2:])
            
    parse(entry)

if __name__ == '__main__':
    test = """
   -  key: val1
      key: val2
   -  - testy
      - testttot
   -  - tamsty
            """
            
    parser(test.split('\n'))