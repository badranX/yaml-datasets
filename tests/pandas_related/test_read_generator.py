import importlib.util
import sys
#spec = importlib.util.spec_from_file_location("pandas_frontend", "./yamld/pandas_frontend.py")
#pandas_frontend = importlib.util.module_from_spec(spec)
#sys.modules["pandas_frontend"] = pandas_frontend
#spec.loader.exec_module(pandas_frontend)
from ...yamld import with_iofile

import pandas as pd
from unittest.mock import patch, mock_open
#from ..yamld.read import from_yamld

# Sample YAML content
yaml_content = """
config1:
  key1: 'value1'
  key2: 'value2'
  key3: 'value3'

oneval: "onevalue"

oneval_list: [1,2,3,4]

config2:
  keyA: 'valueA'
  keyB: 'valueB'
  keyC: 'valueC'

oneval_float: -3.4

dataset:
  - name: 'John Doe'
    age: 30
    city: 'New York'
  - name: 'Jane Smith'
    age: 25
    city: 'San Francisco'
  - name: 'Bob Johnson'
    age: 35
    city: 'Chicago'
  - name: 'Test'
    age: 35.0
    city: 'Chicago'
"""

def test_read_generator():

    with patch("builtins.open", mock_open(read_data=yaml_content)) as mock_file:
        # Test case 1: Check if the function returns a DataFrame
        gen = with_iofile.read_generator('./mocked_path')
        df = pd.DataFrame(gen())
        assert isinstance(df, pd.DataFrame)

        # Test case 2: Check if the DataFrame has the correct number of rows
        assert len(df) == 4


        # Test case 3: Check if the values in the DataFrame are correct
        expected_values = [
            ['John Doe', 30, 'New York'],
            ['Jane Smith', 25, 'San Francisco'],
            ['Bob Johnson', 35, 'Chicago'],
            ['Test', 35.0, 'Chicago']
        ]
        for i, row in enumerate(df.itertuples(index=False)):
            assert list(row) == expected_values[i]

