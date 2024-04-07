from ...yamld import with_iofile

import pandas as pd
from pathlib import Path
from unittest.mock import patch, mock_open
#from ..yamld.read import from_yamld


def test_read_from_file():

    # Test case 1: Check if the function returns a DataFrame
    pathyaml = Path(__file__).parent/'test.yaml'
    pathcsv = Path(__file__).parent/'test.csv'
    dfyaml = with_iofile.read_dataframe(pathyaml)
    dfcsv = pd.read_csv(pathcsv)
    # Test case 2: Check if the DataFrame has the correct number of rows
    assert dfyaml.equals(dfcsv)


if __name__ == "__main__":
  test_read_onelist_dataframe()
