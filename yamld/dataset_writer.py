import yaml

BUFFER_SIZE = 1024

_cast = {
    list: repr,
    str: repr,
    int: repr,
    float: repr,
}

def _caster(entry):
    try:
        return map(lambda x: _cast[type(x)](x), entry)
    except KeyError as e:
        raise e


def write(path, dataset=None, features=None, meta= None, is_min=True):
    assert all(map(lambda x: isinstance(x, str), features))
    is_add_features = (not is_min) or (not features)
    with open(path, 'w') as f:
        if meta:
            yaml.safe_dump(meta, f, default_flow_style=False)
            f.write('\n---\n')
            f.write('\ndataset:\n')
    
    if dataset:
        is_first = True

        batch = ""
        with open(path, 'a') as f:
            for entry in dataset:
                assert len(entry) == len(features)
                entry = _caster(entry)
                lines = ""
                is_feat = is_add_features or is_first
                front = '- ' if is_feat else '- - '
                for feature, val in zip(features, entry):
                    if is_feat:
                        lines = lines + front + feature + ': ' + val + '\n'
                        front = '  '  #2 spaces
                    else:
                        lines = lines + front +  val + '\n'
                        front = '  - ' #4 spaces
                    
                is_first = False
                batch = batch + lines
                if len(batch) > BUFFER_SIZE:
                    f.write(batch)
                    batch = ""
            f.write(batch)
            

if __name__ == '__main__':
    meta = {"whatever" : [1,2,3], "wow": "test"}
    data = [[1,2,3]]*2
    features = ['test1', 'test2', 'test3']
    write('./out.yaml', data, features, meta=meta)