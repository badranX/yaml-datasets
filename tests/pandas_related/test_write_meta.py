from unittest.mock import patch, mock_open
from pathlib import Path
import yaml
from pyfakefs.fake_filesystem_unittest import TestCase

from ...yamld import  with_iofile

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
"""


df = pd.DataFrame()
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

    def test_write(self):
        with_iofile.write_metadata('mock', df.attrs, is_min=False)

        path = Path('mock')

        output = yaml.safe_load(path.read_text())
        expected = yaml.safe_load(expected_yaml)

        assert output == expected