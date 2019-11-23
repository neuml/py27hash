# pylint: disable = C0111,W0622,E0401

import os
import pickle
import unittest

from py27hash.dict import Dict as dict
from py27hash.hash import hash27 as hash

class TestDict(unittest.TestCase):
    def test_small(self):
        d = dict()

        for x in range(15):
            d[str(x)] = x

        # Test key and value
        self.assertEqual(hash("".join(d)), 6636034109572507556)
        self.assertEqual(hash("".join([str(x) for x in d.values()])), 6636034109572507556)

    @unittest.skipIf(os.environ.get("SKIPSLOW", "skipslow"), "Slow tests skipped via skipslow argument")
    def test_large(self):
        d = dict()

        for x in range(60000):
            d[str(x)] = x

        # Test key and value
        self.assertEqual(hash("".join(d)), -35326655653467556)
        self.assertEqual(hash("".join([str(x) for x in d.values()])), -35326655653467556)

    def test_keys(self):
        d = dict()
        d[("abc", 1)] = 1
        d[3.3] = 2
        d[30] = 3
        d["test1234"] = 4

        self.assertEqual(hash("".join([str(k) for k in d])), 7766555225202364718)

    def test_merge(self):
        # Build list of (key, value) pairs to preserve insertion ordering
        d = []
        e = []

        for x in range(200):
            d.append((str(x), x))

        for x in range(200):
            e.append((str(x), x))

        m = dict(d)
        m.update(e)

        self.assertEqual(hash("".join(m)), -5846033856052761336)
        self.assertEqual(hash("".join([str(x) for x in m.values()])), -5846033856052761336)

    def test_update(self):
        d = dict()

        for x in range(500):
            d[str(x)] = x

        d["255"] = "abc"
        d["100"] = "123"

        self.assertEqual(hash("".join(d)), -7925872281736336380)

    def test_delete(self):
        d = dict()

        for x in range(500):
            d[str(x)] = x

        del d["53"]
        del d["155"]

        self.assertEqual(hash("".join(d)), -8652364590473687932)

    def test_pickle(self):
        d = dict()

        for x in range(500):
            d[str(x)] = x

        del d["300"]

        # Pickle and reload object
        data = pickle.dumps(d)
        d = pickle.loads(data)

        self.assertEqual(hash("".join(d)), -3717600429202393594)
