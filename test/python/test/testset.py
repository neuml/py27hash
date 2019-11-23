# pylint: disable = C0111,W0622,E0401

import pickle
import os
import unittest

from py27hash.hash import hash27
from py27hash.set import Set

class TestSet(unittest.TestCase):
    def test_small(self):
        d = Set()

        for x in range(15):
            d.add(str(x))

        self.assertEqual(hash27("".join(d)), 6636034109572507556)

    @unittest.skipIf(os.environ.get("SKIPSLOW", "skipslow"), "Slow tests skipped via skipslow argument")
    def test_large(self):
        d = Set()

        for x in range(60000):
            d.add(str(x))

        self.assertEqual(hash27("".join(d)), -35326655653467556)

    def test_values(self):
        d = Set()
        d.add(("abc", 1))
        d.add(3.3)
        d.add(30)
        d.add("test1234")

        self.assertEqual(hash27("".join([str(k) for k in d])), 7766555225202364718)

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

        self.assertEqual(hash27("".join(m)), -5846033856052761336)

    def test_delete(self):
        d = Set()

        for x in range(500):
            d.add(str(x))

        d.remove("53")
        d.discard("155")

        self.assertEqual(hash27("".join(d)), -8652364590473687932)

    def test_pickle(self):
        d = Set()

        for x in range(500):
            d.add(str(x))

        d.remove("300")

        # Pickle and reload object
        data = pickle.dumps(d)
        d = pickle.loads(data)

        self.assertEqual(hash27("".join(d)), 6818550152093286356)

    def test_clear(self):
        d = Set()

        for x in range(500):
            d.add(str(x))

        d.clear()

        for x in range(1000, 1500):
            d.add(str(x))

        self.assertEqual(hash27("".join(d)), -1473514505880218088)

    def test_copy(self):
        d = Set()

        for x in range(500):
            d.add(str(x))

        d = d.copy()

        self.assertEqual(hash27("".join(d)), 1141231293364439680)

    def test_pop(self):
        d = Set()

        for x in range(500):
            d.add(str(x))

        d.pop()

        self.assertEqual(hash27("".join(d)), -434207861779954688)
