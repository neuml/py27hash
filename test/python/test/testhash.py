# pylint: disable = C0111,W0622,E0401

import unittest

from py27hash.hash import hash27 as hash

class TestHash(unittest.TestCase):
    def test_thash1(self):
        self.assertEqual(hash(("abc", 1)), -6007909421085996277)

    def test_thash2(self):
        self.assertEqual(hash((3.5, 5.83)), 8767369050595774471)

    def test_fhash(self):
        self.assertEqual(hash(1235.333333), 3408413012)

    def test_ihash(self):
        self.assertEqual(hash(15344), 15344)

    def test_shash(self):
        self.assertEqual(hash("test1234"), 1724133767363937712)

    def test_bhash(self):
        self.assertEqual(hash("test1234".encode("utf-8")), 1724133767363937712)
