py27hash: Python 2.7 hashing and iteration in Python 3+
======

[![Version](https://img.shields.io/pypi/v/py27hash.svg?style=flat)](https://pypi.org/project/py27hash/)
[![Build Status](https://img.shields.io/travis/neuml/py27hash/master.svg?style=flat)](https://travis-ci.org/neuml/py27hash)
[![Coverage Status](https://coveralls.io/repos/github/neuml/py27hash/badge.svg)](https://coveralls.io/github/neuml/py27hash)

This package helps ease the migration from Python 2 to 3 for applications that depend on the old hash/iteration order of sets/dicts. Even when setting PYTHONHASHSEED=0, the hash (and default iteration order) will still be different as the hashing algorithm changed in Python 3. This package allows Python 2.7 hashing and set/dict iteration.

## Installation
The easiest way to install is via pip and PyPI

    pip install py27hash

You can also use Git to clone the repository from GitHub and install it manually:

    git clone https://github.com/neuml/py27hash.git
    cd py27hash
    pip install .

Python 2.7 and 3+ are supported.

## How to use
You only need to replace object instantiation to use this package. There are multiple ways to do this, with the best way to do it on a case by case basis.

### Replace each instantiation
The first example replaces a single dict and set with a 2.7 dict.

```python
from py27hash.dict import Dict

# Replace {} with Dict()
d = Dict()

d["a"] = 1

# Python 2.7 sets can be used in the same manner.

from py27hash.set import Set

# Replace set() with Set()
d = Set()

d.add("a")
```

### Override function via import

The same example above can be changed to override the dict and set import statement. This will globally change an entire file which could cause issues but it is an option. If a dict or set was created with the {} syntax, it still needs to be changed to dict()/set().

```python
from py27hash.dict import Dict as dict

d = dict()

d["a"] = 1

# Python 2.7 sets can be used in the same manner.
from py27hash.set import Set as set

d = set()

d.add("a")
```

### Using other methods

The hashing and key iteration methods can be directly accessed via the hash and key packages as follows.

```python
from py27hash.hash import hash27

print(hash27("test1234"))

# As with the example above you could even override the hash function for a particular file.

from p27hash.hash import hash27 as hash

print(hash("test1234"))
```

Both Dict and Set are backed by the keys class. As new values as added/modified, a Keys instance tracks each value to store the order via Python 2.7 hashing. This class can also be used directly.

```python
from p27hash.key import Keys

keys = Keys()
keys.add("1")
keys.add("2")
```

## Background
Python 2 will reach end of life (EOL) on January 1st, 2020. This package helps ease the migration from Python 2 to 3 for applications that depend on the old hash/iteration order of sets/dicts. Even when setting PYTHONHASHSEED=0, the hash (and default iteration order) will still be different as the hashing algorithm changed in Python3. Python 3.6 changed the default iteration order to insertion order.

One target use case is with machine learning. Optimization of machine learning model hyperparameters can take a very long time and if a model was built under Python 2 and feature set/dicts used the default sort order, new parameters would need to be used. This library can be used to allow a full conversion to Python 3 while fixes are made to re-optimize large model parameters. There likely are other use cases, especially in the scientific/engineering space where non-random deterministic iteration in Python 2 was used to create reproducible results.

This package implements logic in cpython 2.7 C source, mainly the Objects/ folder in pure Python. Performance was not a goal of this package and it will perform worse than native collections. It should only be used when there is a clear use case to preserve Python 2.7 hashing/iteration to ease a transition to Python 3.

## Development
If an issue is found in this library, it can be cloned and changed.

    git clone https://github.com/neuml/py27hash.git
    cd py27hash

After changes are made to the source, unit tests should also be added and run via:
    scripts/test.sh

During development slower tests can be skipped via:
    scripts/test.sh skipslow
