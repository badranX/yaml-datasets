import importlib.util
import sys
from ..yamld import parser


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

def test_read_onelist_dataframe():
    l = []
    for entry in parser.parse_dataset(yaml_content.split('\n')):
        l.append(entry)

    #l =  list(parser.parse_dataset(yaml_content.split('\n')))
    # Test case 5: Check if the values in the DataFrame are correct
    expected_values = [
        ['John Doe', 30, 'New York'],
        ['Jane Smith', 25, 'San Francisco'],
        ['Bob Johnson', 35, 'Chicago'],
        ['Test', 35.0, 'Chicago']
    ]
    
    assert l == expected_values


if __name__ == "__main__":
  test_read_onelist_dataframe()
