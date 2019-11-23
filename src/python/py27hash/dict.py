"""
Compatibility methods to support Python 2.7 style dicts in Python 3.X+

This is designed for compatibility not performance.
"""

# pylint: disable = E0401
from .key import Keys

class Dict(dict):
    """
    Compatibility class to support Python 2.7 style iteration in Python 3.X+
    """

    def __init__(self, *args, **kwargs):
        """
        Overrides dict logic to always call set item. This allows Python 2.7 style iteration.

        Args:
            *args: args
            *kwargs: keyword args
        """

        super(Dict, self).__init__()

        # Initialize iteration key list
        self.keylist = Keys()

        # Initialize base arguments
        self.update(*args, **kwargs)

    def __reduce__(self):
        """
        Method necessary to fully pickle Python 3 subclassed dict objects with attribute fields.
        """

        # pylint: disable = W0235
        return super(Dict, self).__reduce__()

    def __setitem__(self, key, value):
        """
        Override of __setitem__ to track keys and simulate Python 2.7 dict.

        Args:
            key: key
            value: value
        """

        super(Dict, self).__setitem__(key, value)

        self.keylist.add(key)

    def __delitem__(self, key):
        """
        Override of __delitem__ to track keys and simulate Python 2.7 dict.

        Args:
            key: key
        """

        super(Dict, self).__delitem__(key)

        self.keylist.remove(key)

    def update(self, *args, **kwargs):
        """
        Overrides dict logic to always call set item. This allows Python 2.7 style iteration.

        Args:
            *args: args
            *kwargs: keyword args
        """

        for arg in args:
            # Cast to dict if applicable. Otherwise, assume it's an iterable of (key, value) pairs.
            if isinstance(arg, dict):
                # Merge incoming keys into keylist
                self.keylist.merge(arg.keys())

                arg = arg.items()

            for k, v in arg:
                self[k] = v

        for k, v in dict(**kwargs).items():
            self[k] = v

    def clear(self):
        """
        Clears the dict along with it's backing Python 2.7 keylist.
        """

        super(Dict, self).clear()

        self.keylist = Keys()

    def copy(self):
        """
        Copies the dict along with it's backing Python 2.7 keylist.

        Returns:
            copy of self
        """

        new = Dict()

        # First copy the keylist to the new object
        new.keylist = self.keylist.copy()

        # Copy keys into backing dict
        for (k, v) in self.items():
            new[k] = v

        return new

    def pop(self, key, default=None):
        """
        Pops the value at key from the dict if it exists, returns default otherwise.

        Args:
            key: key to remove
            default: value to return if key is not found

        Returns:
            value of key if found or default
        """

        value = super(Dict, self).pop(key, default)
        self.keylist.remove(key)

        return value

    def popitem(self):
        """
        Pops an element from the dict and returns the item.

        Returns:
            (key, value) of an element if found or None if dict is empty
        """

        if self:
            key = self.keylist.pop()
            value = self[key] if key else None

            del self[key]

            return (key, value)

        return None

    def __iter__(self):
        """
        Default iterator.

        Returns:
            iterator
        """

        return self.keylist.__iter__()

    def __str__(self):
        """
        Creates a string version of this Dict.

        Returns:
            string
        """

        string = "{"

        for x, k in enumerate(self):
            string += ", " if x > 0 else ""
            string += "'%s': %s" % (k, self[k])

        string += "}"

        return string

    def __repr__(self):
        """
        Creates a string version of this Dict.

        Returns:
            string
        """

        return self.__str__()

    def keys(self):
        """
        Returns keys ordered using Python 2.7's iteration algorithm.

        Returns:
          list of keys
        """

        return self.keylist.keys()

    def values(self):
        """
        Returns values ordered using Python 2.7's iteration algorithm.

        Returns:
          list of values
        """

        return [self[k] for k in self.keys()]

    def items(self):
        """
        Returns items ordered using Python 2.7's iteration algorithm.

        Returns:
          list of items
        """

        return [(k, self[k]) for k in self.keys()]

    # Backwards compat methods removed in Python 3.X
    def has_key(self, key):
        """
        Backwards compat method for Python 2 dict's

        Args:
            key: key to lookup

        Returns:
            True if key exists, False otherwise
        """

        return key in self

    def viewkeys(self):
        """
        Backwards compat method for Python 2 dict

        Returns:
            keys
        """

        return self.keys()

    def viewvalues(self):
        """
        Backwards compat method for Python 2 dict

        Returns:
            values
        """

        return self.values()

    def viewitems(self):
        """
        Backwards compat method for Python 2 dict

        Returns:
            items
        """

        return self.items()

    def iterkeys(self):
        """
        Backwards compat method for Python 2 dict

        Returns:
            iter(keys)
        """

        return iter(self.keys())

    def itervalues(self):
        """
        Backwards compat method for Python 2 dict

        Returns:
            iter(values)
        """

        return iter(self.values())

    def iteritems(self):
        """
        Backwards compat method for Python 2 dict

        Returns:
            iter(items)
        """

        return iter(self.items())
