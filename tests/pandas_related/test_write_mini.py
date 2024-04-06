import yaml
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
  - name: 'Sami Aker'
    age: 30
    city: 'New York'
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

def test_write_mini():
    outio = io.StringIO()
    # Convert DataFrame to YAML
    with_pandas.to_yamld(outio, df, is_min=True)


    
    outio.seek(0)
    output = yaml.safe_load(outio)
    expected = yaml.safe_load(expected_yaml)

    assert output == expected
      
      # Assert equality after processing