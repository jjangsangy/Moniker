# Moniker
A simple batch file rename tool.

[![Build Status](https://travis-ci.org/jjangsangy/Moniker.svg?branch=master)](https://travis-ci.org/jjangsangy/Moniker) [![PyPI version](https://badge.fury.io/py/moniker.svg)](http://badge.fury.io/py/moniker) [![Documentation Status](https://readthedocs.org/projects/moniker/badge/?version=latest)](https://readthedocs.org/projects/moniker/?badge=latest) [![Coverage Status](https://img.shields.io/coveralls/jjangsangy/Moniker.svg)](https://coveralls.io/r/jjangsangy/Moniker)

![Moniker](https://raw.githubusercontent.com/jjangsangy/Moniker/master/img/moniker.png)

# Installation

Moniker is a simple Python utility for renaming and manipulating the filesystem based
off similar project and work from [Irving Ruan](https://github.com/irvingruan/Moniker.git).

## Install from PyPi

```sh
$ pip install -r requirements.txt && pip install moniker
```

## From Source

To get the latest version to try out, clone the github repo.
```sh
$ git clone https://github.com/jjangsangy/moniker.git
```

Setup dependencies with `requirements.txt` (Optional: Adds Color Output)
```sh
$ pip install -r requirements.txt
```

Use `setup.py` to install
```sh
# For Python 2.x Install
$ python setup.py install

# For Python 3.x
$ python3 setup.py install
```
Thats it!

# Usage

## Get Usage
```sh
$ moniker -h

usage: moniker [-h] [-v] [--depth depth] [--replace pat rep]
               [directory]

Simple batch file renaming tool.

positional arguments:
  directory             target directory root

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit

  --depth depth         Recursion depth, default is max
  --replace (pat, rep)  File extension patterns
```

### Specify Depth and Replacement Search/Replace

```sh
$ moniker --depth 2 --replace .py .py.bak .
```

```javascript
{
    ".": [
        {
            "depth": 0, 
            "moniker": "setup.pyo", 
            "name": "setup.py", 
            "size": 1609
        }
    ], 
    "docs": [
        {
            "depth": 1, 
            "moniker": "conf.pyo", 
            "name": "conf.py", 
            "size": 10809
        }
    ], 
    "moniker": [
        {
            "depth": 1, 
            "moniker": "__init__.pyo", 
            "name": "__init__.py", 
            "size": 212
        }, 
        {
            "depth": 1, 
            "moniker": "__main__.pyo", 
            "name": "__main__.py", 
            "size": 2168
        }, 
        {
            "depth": 1, 
            "moniker": "__version__.pyo", 
            "name": "__version__.py", 
            "size": 41
        }, 
        {
            "depth": 1, 
            "moniker": "moniker.pyo", 
            "name": "moniker.py", 
            "size": 1664
        }, 
        {
            "depth": 1, 
            "moniker": "structs.pyo", 
            "name": "structs.py", 
            "size": 170
        }
    ], 
    "moniker/tests": [
        {
            "depth": 2, 
            "moniker": "__init__.pyo", 
            "name": "__init__.py", 
            "size": 0
        }, 
        {
            "depth": 2, 
            "moniker": "test_main.pyo", 
            "name": "test_main.py", 
            "size": 339
        }
    ]
}
```

