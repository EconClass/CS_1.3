#!python

from sets import Set
import unittest
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        pass
    
    def test_size(self):
        s = Set()
        pass

    def test_contains(self):
        s = Set()
        pass

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