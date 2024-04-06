import yaml
#spec = importlib.util.spec_from_file_location("pandas_frontend", "./yamld/pandas_frontend.py")
#pandas_frontend = importlib.util.module_from_spec(spec)
#sys.modules["pandas_frontend"] = pandas_frontend
#spec.loader.exec_module(pandas_frontend)
from ...yamld import with_pandas

import io
import os
import pandas as pd


expected_yaml = """
oneval0: 2
config1:
  key1: 'value1'
  key2: 'value2'

oneval1: 'test'

config2:
  keyA: 'valueA'
  keyB: 'valueB'

oneval2: 3.4


dataset:
  - - 'Sami Aker'
    - 30
    - 'New York'
  - - 'Jane Smith'
    - 25
    - 'San Francisco'
  - - 'Bob Johnson'
    - 35
    - 'Chicago'
  - - 'Test'
    - 35
    - 'Chicago'
"""

# Sample DataFrame
data = {
    'name': ['Sami Aker', 'Jane Smith', 'Bob Johnson', 'Test'],
    'age': [30, 25, 35, 35],
    'city': ['New York', 'San Francisco', 'Chicago', 'Chicago']
}

df = pd.DataFrame(data)
df.attrs['oneval0'] = 2
df.attrs['config1'] = {'key1': 'value1',
                       'key2': 'value2'}
df.attrs['oneval1'] = 'test'
df.attrs['config2'] = {'keyA': 'valueA', 
                       'keyB': 'valueB'}
df.attrs['oneval2'] = 3.4

def normalize_yaml(text):
    return os.linesep.join([s.rstrip() for s in text.splitlines() if s])
x =  "wow"

def test_write_no_columns():
    outio = io.StringIO()
    # Convert DataFrame to YAML
    with_pandas.to_yamld(outio, df, is_min=True, add_column_names=False)


    
    outio.seek(0)
    output = yaml.safe_load(outio)
    expected = yaml.safe_load(expected_yaml)

    assert output == expected