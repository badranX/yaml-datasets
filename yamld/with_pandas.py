#TODO bad import, hide these functions
import csv 
if __name__ == "__main__":
    from parser import parse_dataset, parse_meta, _get_feature_names_and_indent
    from writer import _dump_list, write_meta
else:
    from .parser import parse_dataset, parse_meta, _get_feature_names_and_indent
    from .writer import _dump_list, write_meta, write_dataset_heading
import pandas as pd

def _parse2dataframe(lines):
    meta, lines = parse_meta(lines) 
    features, _, _, lines = _get_feature_names_and_indent(lines)
    if features:
        df = pd.DataFrame(parse_dataset(lines), columns=features)
    else:
        df = pd.DataFrame(parse_dataset(lines))
    df.attrs = meta if meta else {}
    return df

def from_yamld(lines):
    return _parse2dataframe(lines)
    
def to_yamld(iofile, df, is_min=True, add_column_names=True):
    write_meta(iofile, df.attrs)
    write_dataset_heading(iofile)

    df = df.reset_index(drop=True)
    features = df.columns.tolist() if add_column_names else None
    ser = df.apply(lambda x: _dump_list(x.tolist(), features, is_min, x.name), axis=1).\
        explode()
    ser.to_csv(iofile, mode='a', sep='\n', quoting= csv.QUOTE_NONE, index=False, header=False)
 

if __name__ == "__main__":
    l = """
data: "sdlkfs"

dataset:
- test: "wow"
  testy: "testy"
- - "what"
  - "whater"
- - "fuck"
  - "fucker"
"""
    df = _parse2dataframe(l.split('\n'))
    print(df)
    to_yamld(df,'test.yaml')