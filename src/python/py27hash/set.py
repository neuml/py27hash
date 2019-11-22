"""
Compatibility methods to support Python 2.7 style sets in Python 3.X+

This is designed for compatibility not performance.
"""

# pylint: disable = E0401
from .key import Keys

class Set(set):
    """
    Compatibility class to support Python 2.7 style iteration in Python 3.X+
    """

    def __init__(self, *args, **kwargs):
        """
        Overrides set logic to always call set item. This allows Python 2.7 iteration.

        Args:
            *args: args
            *kwargs: keyword args
        """

        super(Set, self).__init__()

        self.keylist = Keys()

        # Initialize base arguments
        self.update(*args, **kwargs)

    def add(self, value):
        """
        Adds value to the set.

        Args:
            value: value to add
        """

        super(Set, self).add(value)

        # Store key for Python 2.7 iteration
        self.keylist.add(value)

    def remove(self, value):
        """
        Removes a value from the set.

        Args:
            value: value to remove
        """

        super(Set, self).remove(value)

        # Remove key
        self.keylist.remove(value)

    def update(self, *args, **kwargs):
        """
        Overrides set logic to always call add item. This allows Python 2.7 style iteration.

        Args:
            *args: args
            *kwargs: keyword args
        """

        for arg in args:
            # Cast to dict if applicable. Otherwise, assume it's an iterable of (key, value) pairs.
            if isinstance(arg, set):
                # Merge incoming keys into keylist
                self.keylist.merge(arg)

            for k in arg:
                self.add(k)

        for k in list(**kwargs):
            self.add(k)

    def __iter__(self):
        """
        Default iterator.

        Returns:
            iterator
        """

        return self.keylist.__iter__()

    def __str__(self):
        """
        Creates a string version of this Set.

        Returns:
            string
        """

        string = "set(["

        for x, k in enumerate(self):
            string = ", " if x > 0 else ""
            string += "'%s'" % (k)

        string += "])"

        return string

    def __repr__(self):
        """
        Creates a string version of this Set.

        Returns:
            string
        """

        return self.__str__()
