# pylint: disable = C0111,W0622,E0401

import os
import pickle
import unittest

from py27hash.dict import Dict
from py27hash.hash import hash27

class TestDict(unittest.TestCase):
    def test_small(self):
        d = Dict()

        for x in range(15):
            d[str(x)] = x

        # Test key and value
        self.assertEqual(hash27("".join(d)), 6636034109572507556)
        self.assertEqual(hash27("".join([str(x) for x in d.values()])), 6636034109572507556)

    @unittest.skipIf(os.environ.get("SKIPSLOW", "skipslow"), "Slow tests skipped via skipslow argument")
    def test_large(self):
        d = Dict()

        for x in range(60000):
            d[str(x)] = x

        # Test key and value
        self.assertEqual(hash27("".join(d)), -35326655653467556)
        self.assertEqual(hash27("".join([str(x) for x in d.values()])), -35326655653467556)

    def test_keys(self):
        d = Dict()
        d[("abc", 1)] = 1
        d[3.3] = 2
        d[30] = 3
        d["test1234"] = 4

        self.assertEqual(hash27("".join([str(k) for k in d])), 7766555225202364718)

    def test_merge(self):
        # Build list of (key, value) pairs to preserve insertion ordering
        d = []
        e = []

        for x in range(200):
            d.append((str(x), x))

        for x in range(200):
            e.append((str(x), x))

        m = Dict(d)
        m.update(e)

        self.assertEqual(hash27("".join(m)), -5846033856052761336)
        self.assertEqual(hash27("".join([str(x) for x in m.values()])), -5846033856052761336)

    def test_update(self):
        d = Dict()

        for x in range(500):
            d[str(x)] = x

        d["255"] = "abc"
        d["100"] = "123"

        self.assertEqual(hash27("".join(d)), -7925872281736336380)

    def test_delete(self):
        d = Dict()

        for x in range(500):
            d[str(x)] = x

        del d["53"]
        d.pop("155")

        self.assertEqual(hash27("".join(d)), -8652364590473687932)

    def test_pickle(self):
        d = Dict()

        for x in range(500):
            d[str(x)] = x

        del d["300"]

        # Pickle and reload object
        data = pickle.dumps(d)
        d = pickle.loads(data)

        self.assertEqual(hash27("".join(d)), 6818550152093286356)

    def test_clear(self):
        d = Dict()

        for x in range(500):
            d[str(x)] = x

        d.clear()

        for x in range(1000, 1500):
            d[str(x)] = x

        self.assertEqual(hash27("".join(d)), -1473514505880218088)

    def test_copy(self):
        d = Dict()

        for x in range(500):
            d[str(x)] = x

        d = d.copy()

        self.assertEqual(hash27("".join(d)), 1141231293364439680)

    def test_fromkeys(self):
        s = []

        for x in range(500):
            s.append(str(x))

        d = Dict.fromkeys(s)

        self.assertEqual(hash27("".join(d)), -7925872281736336380)

    def test_pop(self):
        d = Dict()

        for x in range(10):
            d[str(x)] = x

        self.assertEqual(d.pop("300", 100), 100)

    def test_popitem(self):
        d = Dict()

        for x in range(500):
            d[str(x)] = x

        d.popitem()

        self.assertEqual(hash27("".join(d)), -434207861779954688)
