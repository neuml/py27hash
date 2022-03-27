# pylint: disable = C0111,W0622,E0401

import pickle
import os
import sys
import unittest

from py27hash.hash import hash27
from py27hash.set import Set

is_32bit = sys.maxsize < 2**32


class TestSet(unittest.TestCase):
    def test_small(self):
        d = Set()

        for x in range(15):
            d.add(str(x))

        expected = 175237028 if is_32bit else 6636034109572507556
        self.assertEqual(hash27("".join(d)), expected)

    @unittest.skipIf(os.environ.get("SKIPSLOW", "skipslow"), "Slow tests skipped via skipslow argument")
    def test_large(self):
        d = Set()

        for x in range(60000):
            d.add(str(x))

        expected = -1791340678 if is_32bit else -35326655653467556
        self.assertEqual(hash27("".join(d)), expected)

    def test_values(self):
        d = Set()
        d.add(("abc", 1))
        d.add(3.3)
        d.add(30)
        d.add("test1234")

        expected = 245633326 if is_32bit else 7766555225202364718
        self.assertEqual(hash27("".join([str(k) for k in d])), expected)

    def test_merge(self):
        # Build list of (key, value) pairs to preserve insertion ordering
        d = []
        e = []

        for x in range(200):
            d.append(str(x))

        for x in range(200):
            e.append(str(x))

        m = Set(d)
        m.update(e)

        expected = 2031185160 if is_32bit else -5846033856052761336
        self.assertEqual(hash27("".join(m)), expected)

    def test_delete(self):
        d = Set()

        for x in range(500):
            d.add(str(x))

        d.remove("53")
        d.discard("155")

        expected = 1168493700 if is_32bit else -8652364590473687932
        self.assertEqual(hash27("".join(d)), expected)

    def test_pickle(self):
        d = Set()

        for x in range(500):
            d.add(str(x))

        d.remove("300")

        # Pickle and reload object
        data = pickle.dumps(d)
        d = pickle.loads(data)

        expected = -1296777260 if is_32bit else 6818550152093286356
        self.assertEqual(hash27("".join(d)), expected)

    def test_clear(self):
        d = Set()

        for x in range(500):
            d.add(str(x))

        d.clear()

        for x in range(1000, 1500):
            d.add(str(x))

        expected = 698340888 if is_32bit else -1473514505880218088
        self.assertEqual(hash27("".join(d)), expected)

    def test_copy(self):
        d = Set()

        for x in range(500):
            d.add(str(x))

        d = d.copy()

        expected = -1829309066 if is_32bit else 1141231293364439680
        self.assertEqual(hash27("".join(d)), expected)

    def test_pop(self):
        d = Set()

        for x in range(500):
            d.add(str(x))

        d.pop()

        expected = 267158528 if is_32bit else -434207861779954688
        self.assertEqual(hash27("".join(d)), expected)
