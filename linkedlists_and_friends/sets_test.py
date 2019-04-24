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
        s = Set([1,2,3])
        assert s.table.size == 3

    def test_size(self):
        s = Set([0,1,2,3])
        assert s.size() == 4
        s = Set()
        assert s.size() == 0

    def test_contains(self):
        s = Set([1,2,3])
        assert s.contains(1) is True
        assert s.contains(2) is True
        assert s.contains(3) is True
        # items not in set
        assert s.contains(0) is False
        assert s.contains(4) is False
        assert s.contains('A') is False

    def test_add(self):
        s = Set()
        assert s.size() == 0

        s.add('A')
        assert s.size() == 1
        assert s.contains('A') is True

        s.add('B')
        assert s.size() == 2
        assert s.contains('B') is True

        s.add(1)
        assert s.size() == 3
        assert s.contains(1) is True

        # Cannot add duplicate elements
        with self.assertRaises(KeyError):
            s.add('A')
        with self.assertRaises(KeyError):
            s.add(1)

    def test_remove(self):
        s = Set([1,2,3])
        assert s.size() == 3
        assert s.contains(2) is True

        s.remove(2)
        assert s.size() == 2
        assert s.contains(2) is False
        # Can't remove nonexistent element
        with self.assertRaises(KeyError):
            s.remove(2)

        s.remove(3)
        assert s.size() == 1
        assert s.contains(3) is False
        # Can't remove nonexistent element
        with self.assertRaises(KeyError):
            s.remove(3)

        s.remove(1)
        assert s.size() == 0
        assert s.contains(1) is False
        # Can't remove nonexistent element
        with self.assertRaises(KeyError):
            s.remove(1)

    def test_union(self):
        s = Set(['A', 'B', 'C'])
        ss = Set(['B', 'C', 'D'])

        sss = s.union(ss)
        assert sss.contains('A') is True
        assert sss.contains('B') is True
        assert sss.contains('C') is True
        assert sss.contains('D') is True

    def test_intersection(self):
        s = Set(['A', 'B', 'C'])
        ss = Set(['B', 'C', 'D'])

        sss = s.intersection(ss)

        assert sss.contains('B') is True
        assert sss.contains('C') is True

        assert sss.contains('A') is False
        assert sss.contains('D') is False
        

    def test_difference(self):
        s = Set(['A', 'B', 'C'])
        ss = Set(['B', 'C', 'D'])
        sss1 = s.difference(ss)
        sss2 = ss.difference(s)

        assert sss1.contains('A') is True

        assert sss1.contains('B') is False
        assert sss1.contains('C') is False
        assert sss1.contains('D') is False

        assert sss2.contains('D') is True

        assert sss2.contains('A') is False
        assert sss2.contains('B') is False
        assert sss2.contains('C') is False


    def test_is_subset_with_valid_subsets(self):
        s = Set(['A', 'B', 'C'])
        # sets are subsets of themselves
        assert s.is_subset(s) is True
        ss = Set(['A'])
        assert s.is_subset(ss) is True
        ss = Set(['B'])
        assert s.is_subset(ss) is True
        ss = Set(['C'])
        assert s.is_subset(ss) is True
        ss = Set(['A', 'B'])
        assert s.is_subset(ss) is True
        ss = Set(['A', 'C'])
        assert s.is_subset(ss) is True
        ss = Set(['B', 'C'])
        assert s.is_subset(ss) is True

    def test_is_subset_with_invalid_subsets(self):
        s = Set(['A', 'B', 'C'])
        ss = Set(['D'])
        assert s.is_subset(ss) is False

        assert s.is_subset(ss) is False
        ss = Set(['A', 'D'])
        assert s.is_subset(ss) is False
        ss = Set(['D', 'C'])
        assert s.is_subset(ss) is False
        