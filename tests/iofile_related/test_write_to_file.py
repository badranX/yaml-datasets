from ...yamld import with_iofile
from ...yamld import with_pandas

import pandas as pd
from pathlib import Path
from unittest.mock import patch, mock_open
#from ..yamld.read import from_yamld

from pyfakefs.fake_filesystem_unittest import TestCase

pathyaml = Path(__file__).parent/'test.yaml'
pathcsv = Path(__file__).parent/'test.csv'
dfyaml = with_iofile.read_dataframe(pathyaml)
dfcsv = pd.read_csv(pathcsv)

yaml_content = pathyaml.read_text().strip()

class MyTest(TestCase):
    def setUp(self):
        self.setUpPyfakefs()

    def test_foobar(self):
        self.fs.create_file('mock.yaml', contents='')
        with_iofile.write_dataframe('mock.yaml', dfcsv, is_min=False)
        path = Path('mock.yaml')
        self.assertEqual(path.read_text().strip(), yaml_content)