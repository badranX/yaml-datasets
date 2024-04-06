from .parser import parse_dataset, parse_meta, _get_feature_names_and_indent
from .writer import _dump_list, write_meta
import pandas as pd

def _parse2dataframe(lines):
    meta, lines = parse_meta(lines) 
    features, _, lines = _get_feature_names_and_indent(lines)
    if features:
        df = pd.DataFrame(parse_dataset(lines), columns=features)
    else:
        df = pd.DataFrame(parse_dataset(lines))
    df.attrs = meta if meta else {}
    return df

def from_yamld(path):
    with open(path, 'r') as f:
        return _parse2dataframe(f)
    
def to_yamld(df, path, is_min=True):
    write_meta(path, df.attrs)

    df = df.reset_index(drop=True)
    features = df.columns.tolist()
    df.apply(lambda x: _dump_list(x.tolist(), features, is_min, x.name), axis=1).\
        explode().to_csv(path, mode='a', index=False, header=False)
 

if __name__ == "__main__":
    l = """
data: "sdlkfs"

dataset:
- - "what"
  - "whater"
- - "fuck"
  - "fucker"
"""
    df = _parse2dataframe(l.split('\n'))
    to_yamld(df,'test.yaml')