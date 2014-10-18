# Moniker
A simple batch file rename tool.

[![Build Status](https://travis-ci.org/jjangsangy/Moniker.svg?branch=master)](https://travis-ci.org/jjangsangy/Moniker) [![PyPI version](https://badge.fury.io/py/moniker.svg)](http://badge.fury.io/py/moniker) [![Documentation Status](https://readthedocs.org/projects/moniker/badge/?version=latest)](https://readthedocs.org/projects/moniker/?badge=latest) [![Coverage Status](https://img.shields.io/coveralls/jjangsangy/Moniker.svg)](https://coveralls.io/r/jjangsangy/Moniker)

# Installation

Moniker is a simple Python utility for renaming and manipulating the filesystem based
off similar project and work from [Irving Ruan](https://github.com/irvingruan/Moniker.git).

## Install from PyPi

```sh
$ pip install -r requirements.txt
$ pip install moniker
```

# Usage

```sh
$ moniker . .py .python
```

```javascript
{
    ".": [
        {
            "setup.py": "setup.python"
        }
    ], 
    "docs": [
        {
            "conf.py": "conf.python"
        }
    ], 
    "moniker": [
        {
            "__init__.py": "__init__.python"
        }, 
        {
            "__main__.py": "__main__.python"
        }, 
        {
            "__version__.py": "__version__.python"
        }, 
        {
            "moniker.py": "moniker.python"
        }
    ], 
    "moniker/tests": [
        {
            "__init__.py": "__init__.python"
        }, 
        {
            "test_main.py": "test_main.python"
        }
    ]
}
```

