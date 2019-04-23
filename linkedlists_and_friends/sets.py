#!python

from hashtable import HashTable

class Set(object):
    def __init__(self):
        """Initialize set as an empty hash table."""
        self.table = HashTable()

    def size(self):
        """Returns the number of elements in the set."""
        # Constant time to look up object properties.
        return self.table.size # O(1)

    def contains(self, elem):
        """Returns True if element is in the set and False otherwise.
        NOTE: The Set.contains() also uses the HashTable.contains().
        Time complexity for Set.contains() is the same as HashTable.contains().
            *O(1) due to Hashtable's _resize()"""

        # Pass the element as a key to call the hash table method contains().
        # The contains() method checks to see if the key is in the hash table.
        return self.table.contains(elem)

    def add(self, elem):
        """Adds item to the set."""
        self.table.set(elem, None) 


    def remove(self, elem):
        """Removes item to the set."""
        self.table.delete(elem)

    def union(self, other_set):
        """Returns a subset of elements that are in current set OR the given set.
        Best and Worst case running time: O(2n) -> O(n)"""
        new_set = Set() 

        for elem in self.table.keys(): # O(n)
           new_set.add(elem) # O(1)
        
        for thing in other_set.keys(): # O(n)
            if new_set.contains(thing) != True: # O(1)
                new_set.add(thing) # O(1)

        return new_set


    def intersection(self, other_set):
        """Returns a subset of elements that are in current set AND the given set."""

    def difference(self, other_set):
        """Returns a subset of elements that are in current set AND
        NOT in the given set."""

    def is_subset(self, subset):
        """Returns True if the given subset is in current set, False otherwise."""
