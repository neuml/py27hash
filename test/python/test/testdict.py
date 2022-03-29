# pylint: disable = C0111,W0622,E0401

import os
import pickle
import sys
import unittest

from py27hash.dict import Dict
from py27hash.hash import hash27

is_32bit = sys.maxsize < 2**32


class TestDict(unittest.TestCase):
    def test_small(self):
        d = Dict()

        for x in range(15):
            d[str(x)] = x

        # Test key and value
        expected = 175237028 if is_32bit else 6636034109572507556
        self.assertEqual(hash27("".join(d)), expected)
        self.assertEqual(hash27("".join([str(x) for x in d.values()])), expected)

    @unittest.skipIf(os.environ.get("SKIPSLOW", "skipslow"), "Slow tests skipped via skipslow argument")
    def test_large(self):
        d = Dict()

        for x in range(60000):
            d[str(x)] = x

        # Test key and value
        expected = -1791340678 if is_32bit else -35326655653467556
        self.assertEqual(hash27("".join(d)), expected)
        self.assertEqual(hash27("".join([str(x) for x in d.values()])), expected)

    def test_keys(self):
        d = Dict()
        d[("abc", 1)] = 1
        d[3.3] = 2
        d[30] = 3
        d["test1234"] = 4

        expected = 245633326 if is_32bit else 7766555225202364718
        self.assertEqual(hash27("".join([str(k) for k in d])), expected)

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

        expected = 2031185160 if is_32bit else -5846033856052761336
        self.assertEqual(hash27("".join(m)), expected)
        self.assertEqual(hash27("".join([str(x) for x in m.values()])), expected)

    def test_update(self):
        d = Dict()

        for x in range(500):
            d[str(x)] = x

        d["255"] = "abc"
        d["100"] = "123"

        expected = 536718340 if is_32bit else -7925872281736336380
        self.assertEqual(hash27("".join(d)), expected)

    def test_delete(self):
        d = Dict()

        for x in range(500):
            d[str(x)] = x

        del d["53"]
        d.pop("155")

        expected = 1168493700 if is_32bit else -8652364590473687932
        self.assertEqual(hash27("".join(d)), expected)

    def test_pickle(self):
        d = Dict()

        for x in range(500):
            d[str(x)] = x

        del d["300"]

        # Pickle and reload object
        data = pickle.dumps(d)
        d = pickle.loads(data)

        expected = -1296777260 if is_32bit else 6818550152093286356
        self.assertEqual(hash27("".join(d)), expected)

    def test_clear(self):
        d = Dict()

        for x in range(500):
            d[str(x)] = x

        d.clear()

        for x in range(1000, 1500):
            d[str(x)] = x

        expected = 698340888 if is_32bit else -1473514505880218088
        self.assertEqual(hash27("".join(d)), expected)

    def test_copy(self):
        d = Dict()

        for x in range(500):
            d[str(x)] = x

        d = d.copy()

        expected = -1829309066 if is_32bit else 1141231293364439680
        self.assertEqual(hash27("".join(d)), expected)

    def test_fromkeys(self):
        s = []

        for x in range(500):
            s.append(str(x))

        d = Dict.fromkeys(s)

        expected = 536718340 if is_32bit else -7925872281736336380
        self.assertEqual(hash27("".join(d)), expected)

    def test_fromdict(self):
        d = Dict({2: None, 3: None, 4: None, 5: None, 8: None})

        expected = -522874759 if is_32bit else -834114354854653831
        self.assertEqual(hash27("".join([str(x) for x in d])), expected)

    def test_fromdictresize(self):
        d = Dict({2: None, 3: None, 4: None, 5: None, 8: None, 9: None, 10: None, 11: None, 12: None, 13: None, 14: None})

        expected = 1667650642 if is_32bit else -2555609460481043374
        self.assertEqual(hash27("".join([str(x) for x in d])), expected)

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

        expected = 267158528 if is_32bit else -434207861779954688
        self.assertEqual(hash27("".join(d)), expected)
