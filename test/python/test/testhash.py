# pylint: disable = C0111,W0622,E0401

import sys
import unittest

from py27hash.hash import hash27

is_32bit = sys.maxsize < 2**32


class TestHash(unittest.TestCase):
    def test_thash1(self):
        expected = 2037533451 if is_32bit else -6007909421085996277
        self.assertEqual(hash27(("abc", 1)), expected)

    def test_thash2(self):
        expected = 864276487 if is_32bit else 8767369050595774471
        self.assertEqual(hash27((3.5, 5.83)), expected)

    def test_fhash(self):
        expected = -886554284 if is_32bit else 3408413012
        self.assertEqual(hash27(1235.333333), expected)

    def test_ihash(self):
        expected = 15344
        self.assertEqual(hash27(15344), expected)

    def test_shash(self):
        expected = -855915088 if is_32bit else 1724133767363937712
        self.assertEqual(hash27("test1234"), expected)

    def test_bhash(self):
        expected = -855915088 if is_32bit else 1724133767363937712
        self.assertEqual(hash27("test1234".encode("utf-8")), expected)
