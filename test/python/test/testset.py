import os
import unittest

# pylint: disable = E0401
from py27hash.hash import hash27 as hash
from py27hash.set import Set as set

class TestSet(unittest.TestCase):
    def test_small(self):
        d = set()

        for x in range(15):
            d.add(str(x))

        self.assertEqual(hash("".join(d)), 6636034109572507556)

    @unittest.skipIf(os.environ.get("SKIPSLOW", "skipslow"), "Slow tests skipped via skipslow argument")
    def test_large(self):
        d = set()

        for x in range(60000):
            d.add(str(x))

        self.assertEqual(hash("".join(d)), -35326655653467556)

    def test_values(self):
        d = set()
        d.add(("abc", 1))
        d.add(3.3)
        d.add(30)
        d.add("test1234")

        self.assertEqual(hash("".join([str(k) for k in d])), 7766555225202364718)

    def test_merge(self):
        # Build list of (key, value) pairs to preserve insertion ordering
        d = []
        e = []

        for x in range(200):
            d.append(str(x))

        for x in range(200):
            e.append(str(x))

        m = set(d)
        m.update(e)

        self.assertEqual(hash("".join(m)), -5846033856052761336)

    def test_delete(self):
        d = set()

        for x in range(500):
            d.add(str(x))

        d.remove("53")
        d.remove("155")

        self.assertEqual(hash("".join(d)), -8652364590473687932)
