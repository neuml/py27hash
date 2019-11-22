py27hash: Python 2.7 style hashing and iteration
======

# About
This package is designed to support Python 2.7 style hashing and iteration in any Python version. While there are a number of Python 2/3 compatibility libraries most are designed to support the old API classes/methods. This package will ensure the exact same behavior for dictionaries and sets.

This package helps ease the transition from Python 2 to 3 for a small series of use cases. If an application for some reason depended on the old hashing/sort order of these collections, this package will solve that issue and ease a transition towards Python 3. Even when setting PYTHONHASHSEED=0, the hash (and default iteration order) will still be different as the hashing algorithm changed in Python3. Python 3.6 changed the default iteration order to insertion order.

One target use case is with machine learning. Optimization of machine learning model hyperparameters can take a very long time and if a model was built under Python 2 and feature set/dicts used the default sort order, new parameters would need to be used.

This package implements logic in cpython 2.7 C source, mainly the Objects/ folder in pure Python. Performance was not a goal of this package and it will perform worse than native collections. It should only be used when there is a clear use case to preserve Python 2.7 hashing/iteration to ease a transition to Python 3.

# Installation
You can use Git to clone the repository from GitHub and install it manually:

    git clone <url>
    cd py27hash
    python setup.py install

Python 2.7, 3.5, 3.6, 3.7, & 3.8 are supported.

# How to use
You only need to replace object instantiation to use this package. There are multiple ways to do this, with the preferred way to do it on a case by case basis.

## Replace each instantiation
The first example replaces a single dict and set with a 2.7 style dict.

```python
from py27hash.dict import Dict

# Replace {} with Dict()
d = Dict()

d["a"] = 1

# Python 2.7 style sets can be used in the same manner.

from py27hash.set import Set

# Replace set() with Set()
d = Set()

d.add("a")
```

## Override function via import

The same example above can be changed to override the dict and set import statement. This will globally change an entire file which could cause issues but it is an option. If a dict or set was created with the {} syntax, it still needs to be changed to dict()/set().

```python
from py27.dict import Dict as dict
from py27.set import Set as set

d = dict()

d["a"] = 1

# Python 2.7 style sets can be used in the same manner.

from py27hash.set import Set

d = set()

d.add("a")
```

## Using other methods

The hashing and key iteration methods can be directly accessed via the hash and key packages as follows.

```python
from py27hash.hash import Hash

print(Hash.hash("test1234"))

#As with the example above you could even override the hash function for a particular file.

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

# Development
If an issue is found in this library, it can be cloned and changed.

    git clone <url>
    cd py27hash

After changes are made to the source, unit tests should also be added and run via:
    scripts/test.sh

During development slower tests can be skipped via:
    scripts/test.sh skipslow
