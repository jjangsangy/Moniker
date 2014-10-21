Moniker
=======

A simple batch file rename tool.

|Build Status| |PyPI version| |Documentation Status| |Coverage Status|

|Moniker|

Installation
============

| Moniker is a simple Python utility for renaming and manipulating the
filesystem based
| off similar project and work from `Irving
Ruan <https://github.com/irvingruan/Moniker.git>`__.

Install from PyPi
-----------------

.. code:: sh

    $ pip install -r requirements.txt && pip install moniker

From Source
-----------

To get the latest version to try out, clone the github repo.

.. code:: sh

    $ git clone https://github.com/jjangsangy/moniker.git

Setup dependencies with ``requirements.txt`` (Optional: Adds Color
Output)

.. code:: sh

    $ pip install -r requirements.txt

Use ``setup.py`` to install

.. code:: sh

    # For Python 2.x Install
    $ python setup.py install

    # For Python 3.x
    $ python3 setup.py install

Thats it!

Usage
=====

.. code:: sh

    # Default recursive search at current directory
    $ moniker --replace .py .py.bak

.. code:: javascript

    {
      ".": [
        {
          "setup.py": "setup.py.bak"
        }
      ], 
      "docs": [
        {
          "conf.py": "conf.py.bak"
        }
      ], 
      "moniker": [
        {
          "__init__.py": "__init__.py.bak"
        }, 
        {
          "__main__.py": "__main__.py.bak"
        }, 
        {
          "__version__.py": "__version__.py.bak"
        }, 
        {
          "moniker.py": "moniker.py.bak"
        }, 
        {
          "structs.py": "structs.py.bak"
        }
      ], 
      "tests": [
        {
          "__init__.py": "__init__.py.bak"
        }, 
        {
          "test_main.py": "test_main.py.bak"
        }
      ]
    }

Get Help Instructions
---------------------

.. code:: sh

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

.. |Build Status| image:: https://travis-ci.org/jjangsangy/Moniker.svg?branch=master
   :target: https://travis-ci.org/jjangsangy/Moniker
.. |PyPI version| image:: https://badge.fury.io/py/moniker.svg
   :target: http://badge.fury.io/py/moniker
.. |Documentation Status| image:: https://readthedocs.org/projects/moniker/badge/?version=latest
   :target: https://readthedocs.org/projects/moniker/?badge=latest
.. |Coverage Status| image:: https://img.shields.io/coveralls/jjangsangy/Moniker.svg
   :target: https://coveralls.io/r/jjangsangy/Moniker
.. |Moniker| image:: https://raw.githubusercontent.com/jjangsangy/Moniker/master/img/moniker.png
