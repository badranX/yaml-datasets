# yaml-datasets (YAMLd)

YAML datasets (**YAMLd**) is a tiny subset of *YAML* designed specifically for representing tabular data (such as **CSV**). It is particularly useful for datasets with numerous features or lengthy sequences that are hard to read.

### YAMLd Rules:

- The file ends with a top-level key `data` or `dataset` that contains the list of entries in the dataset.
- Everything before is considered meta-data. If you are using **pandas**, it will be loaded in the `attrs` property of the dataframe.
    
### Example

``` yaml
features_description:
  name: 'embloyee name'
  age: 'age'
  city: 'closest city to adress'

extra: 3.4

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
```

Using a 'mini' version of this, you can remove the feature names from each line as follows.

``` yaml
data:
  - name: 'John Doe'
    age: 30
    city: 'New York'
  - - 'Jane Smith'
    - 25
    - 'San Francisco'
  - - 'Bob Johnson'
    - 35
    - 'Chicago'
```

You can also remove feature names completly.

> **_Note:_** This library is still experimental, use it with caution.


## Scripting
A simple example:
```python
import yamld

#Read dataframe
dataframe = yamld.read_dataframe('your_yamld_file.yaml')

#Print meta-data
print(dataframe.attrs)

#Write dataframe to a file
yamld.write_dataframe('new_yamld_file.yaml', dataframe)

#Read yamld as a generator of `dict` values
dataset_gen = yamld.read_generator('your_yamld_file.yaml')
```

**Note:** this API is subject to change.

## Convert CSV to YAMLd and vice versa:
```console
csv2yamld <your-csv-file>
```

```console
yamld2csv <your-yamld-file>
```

For more details use `csv2yamld -h` or `yamld2csv -h`.

## Open CSV files with VIM/NVIM
Reading *CSV* can be annoying, here is a simple solution:

```console
csv2yamld <your-csv-file> --stdout | nvim -c 'set filetype=yaml' -
```

Of course, you can edit it, save it, and convert it back to *CSV* using `yamld2csv`.


## Setup
```console 
pip install -U yamld
```

To install without virtual environments, you can use [*pipx*](https://github.com/pypa/pipx).

## Details
The main goal is to edit and view your data files with nothing but your text editor. Consequently, a lot of YAML features are not parsed after the top-level key-word `data` or `dataset`, as their inclusion could either introduce clutter or hinder the parsing efficiency for dataset. For example, YAML explicit types markings and comments are not supported.


### Data Types:
- Dataset data types:
    - List: surrounded with `[]`
    - String: surrounded with `""` or `''` 
    - Number

    
### As for now the followings are allowed:
    
- No meta, only dataset: This can be done by providing only a list using the dash charachter.  Example:

``` yaml
- - 30
  - 'New York'
- - 25
  - 'San Francisco'
```

- Meta data only: A YAML file with no top-level `dataset` or `data` key and it is not only a list of dash charachters is read exactly as any YAML file.
``` yaml
meta_val: "some_value"
another_meta_val: "another_value"
```
