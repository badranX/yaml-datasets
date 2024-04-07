import yaml
from pyfakefs.fake_filesystem_unittest import TestCase
from pathlib import Path
from ...yamld import with_iofile

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

class TestWrite(TestCase):
    def setUp(self):
        self.setUpPyfakefs()

    def test_write_no_columns(self):
        with_iofile.write_dataframe('mock', df, is_min=True, add_column_names=False)

        path = Path('mock')

        output = yaml.safe_load(path.read_text())
        expected = yaml.safe_load(expected_yaml)

        assert output == expected
