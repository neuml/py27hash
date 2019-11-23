"""
Compatibility methods to support Python 2.7 style key iteration in Python 3.X+

This is designed for compatibility not performance.
"""

import ctypes

# pylint: disable = E0401
from .hash import Hash

class Keys(object):
    """
    Compatibility class to support Python 2.7 style iteration in Python 3.X+

    Logic ported from the 2.7 Python branch: cpython/Objects/dictobject.c
    Logic ported from the 2.7 Python branch: cpython/Objects/setobject.c
    """

    # Min dict size
    MINSIZE = 8

    # Hash collisions
    PERTURB_SHIFT = 5

    def __init__(self):
        """
        Initializes a keys object.
        """

        self.keylist = []
        self.keysort = None

        # Python 2 dict default size
        self.mask = Keys.MINSIZE - 1

    def __setstate__(self, state):
        """
        Overrides default pickling object to force re-adding all keys and match Python 2.7 deserialization logic.

        Args:
            state: input state
        """

        self.__dict__ = state
        keys = self.keys()

        # Clear keys and re-add to match deserialization logic
        self.__init__()

        for k in keys:
            self.add(k)

    def __iter__(self):
        """
        Default iterator.

        Returns:
            iterator
        """

        return iter(self.keys())

    def keys(self):
        """
        Returns keys ordered using Python 2.7's iteration algorithm.

        Method: static PyDictEntry *lookdict(PyDictObject *mp, PyObject *key, register long hash)

        Returns:
          list of keys
        """

        if not self.keysort:
            keys = []
            hids = set()

            for k in self.keylist:
                # C API uses unsigned values
                h = ctypes.c_size_t(Hash.hash(k)).value
                i = h & self.mask

                hid = i
                perturb = h

                while hid in hids:
                    i = (i << 2) + i + perturb + 1

                    hid = i & self.mask

                    perturb >>= Keys.PERTURB_SHIFT

                keys.append((hid, k))
                hids.add(hid)

            # Cache result - performance - clear if more keys added
            self.keysort = [v for (k, v) in sorted(keys, key=lambda x: x[0])]

        return self.keysort

    def add(self, key):
        """
        Called each time a new item is inserted. Tracks via insertion order and will maintain the same order
        as a dict in Python 2.7.

        Method: static int dict_set_item_by_hash_or_entry(register PyObject *op, PyObject *key, long hash,
                                                          PyDictEntry *ep, PyObject *value)

        Args:
          key: key to add
        """

        # Add key to list. If this is a replace/update then size won't change.
        if key and key not in self.keylist:
            # Append key to list
            self.keylist.append(key)

            # Clear cached keys
            self.keysort = None

            # Resize dict if 2/3 capacity
            if len(self.keylist) * 3 >= ((self.mask + 1) * 2):
                # Reset key list to simulate the dict resize + copy operation
                self.keylist = self.keys()
                self.keysort = None

                self.setMask()

    def remove(self, key):
        """
        Remove a key from the backing list.

        Args:
            key: key to remove
        """

        if key in self.keylist:
            # Remove key from list
            self.keylist.remove(key)

            # Clear cached keys
            self.keysort = None

    def merge(self, d):
        """
        Merges keys from an existing iterable into this key list.

        Method: int PyDict_Merge(PyObject *a, PyObject *b, int override)

        Args:
            d: input dict
        """

        # PyDict_Merge initial merge size is double the size of the current + incoming dict
        self.setMask((len(self.keylist) + len(d)) * 2)

        # Copy actual keys
        for k in d:
            self.add(k)

    def copy(self):
        """
        Makes a copy of self.

        Method: PyObject *PyDict_Copy(PyObject *o)

        Returns:
            copy of self
        """

        # Copy creates a new object and merges keys in
        new = Keys()
        new.merge(self.keys())

        return new

    def pop(self):
        """
        Pops the top element from the sorted keys if it exists. Returns None otherwise.

        Method: static PyObject *dict_popitem(PyDictObject *mp)

        Return:
            top element or None if Keys is empty
        """

        if self.keylist:
            # Pop the top element
            value = self.keys()[0]
            self.remove(value)
            return value

        return None

    def setMask(self, request=None):
        """
        Key based on the total size of this dict. Matches ma_mask in Python 2.7's dict.

        Method: static int dictresize(PyDictObject *mp, Py_ssize_t minused)
        """

        if not request:
            length = len(self.keylist)

            # Python 2 dict increases by a factor of 4 for small dicts, 2 for larger ones
            request = length * (2 if length > 50000 else 4)

        newsize = Keys.MINSIZE
        while newsize <= request:
            newsize <<= 1

        self.mask = newsize - 1
