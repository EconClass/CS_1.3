#!python

from sets import Set
from hashtable import HashTable

import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.table.size == 0

    def test_size(self):
        s = Set(0,1,2,3)
        assert s.size() == 4
        s = Set()
        assert s.size() == 0

    def test_contains(self):
        s = Set(1,2,3)
        assert s.contains(1) == True
        assert s.contains(2) == True
        assert s.contains(3) == True

    def test_add(self):
        s = Set()
        pass

    def test_remove(self):
        s = Set()
        pass

    def test_union(self):
        s = Set()
        pass

    def test_intersection(self):
        s = Set()
        pass

    def test_difference(self):
        s = Set()
        pass

    def test_is_subset(self):
        s = Set()
        pass