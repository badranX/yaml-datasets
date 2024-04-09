from setuptools import setup, find_packages

setup(
    name='yamld',
    version='0.0.33',
    author='Yahya Badran',
    author_email='techtweaking@gmail.com',
    description='parser of YAMLd, a tiny subset of YAML',
    url='https://github.com/badranx/yaml-datasets',
    install_requires=['pandas >= 1.0.0'],
    packages = [package for package in find_packages() if package.startswith("yamld")],
    scripts=['bin/csv2yamld', 'bin/yamld2csv', 'bin/yamld'],
    license='MIT',
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
