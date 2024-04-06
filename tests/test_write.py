import importlib.util
import sys
#spec = importlib.util.spec_from_file_location("pandas_frontend", "./yamld/pandas_frontend.py")
#pandas_frontend = importlib.util.module_from_spec(spec)
#sys.modules["pandas_frontend"] = pandas_frontend
#spec.loader.exec_module(pandas_frontend)
from ..yamld import pandas_frontend

import io
import os
import pandas as pd

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

def test_dataframe_to_yaml():
    outio = io.StringIO()
    # Convert DataFrame to YAML
    pandas_frontend.to_yamld(outio, df)


    # Test case 1: Check if the generated YAML has the correct structure
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

data:
  - name: 'Sami Aker'
    age: 30
    city: 'New York'
  - name: 'Jane Smith'
    age: 25
    city: 'San Francisco'
  - name: 'Bob Johnson'
    age: 35
    city: 'Chicago'
  - name: 'Test'
    age: 35
    city: 'Chicago'
"""
    outio.seek(0)
    assert normalize_yaml(outio.read()) == normalize_yaml(expected_yaml)
    
if __name__ == "__main__":
  test_dataframe_to_yaml()
