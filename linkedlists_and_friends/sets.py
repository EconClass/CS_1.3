#!python

from hashtable import HashTable

class Set(object):
    def __init__(self, *items):
        """Initialize set as an empty hash table."""
        self.table = HashTable()

        if len(items) != 0:
            for item in items:
                self.table.set(item, None)

    def __iter__(self):
        """Allows Set class to be iterable."""
        return iter(self.table.keys())

    def __repr__(self):
        """Return a string representation of this set."""
        return "Set{!r}".format(self.table.keys())

    def size(self):
        """Returns the number of elements in the set."""
        # Constant time to look up object properties.
        return self.table.size # O(1)

    def contains(self, elem):
        """Returns True if element is in the set and False otherwise.
        NOTE: The Set.contains() uses the HashTable.contains().
        Time complexity for Set.contains() is the same as HashTable.contains().
            *O(1) due to Hashtable's _resize()"""

        # Pass the element as a key to call the hash table method contains().
        # The contains() method checks to see if the key is in the hash table.
        return self.table.contains(elem)

    def add(self, elem):
        """Adds item to the set."""
        if not self.contains(elem):
            self.table.set(elem, None) # *O(1)
        raise KeyError("Item is already in the set.")

    def remove(self, elem):
        """Removes item to the set."""
        if self.contains(elem) == True:
            self.table.delete(elem) # *O(1)
        raise KeyError("Item not in set. ")

    def union(self, other_set):
        """Returns a subset of elements that are in current set OR the given set.
        Best and Worst case running time: O(2n) -> O(n)"""
        new_set = Set()

        for elem in self: # O(n)
           new_set.add(elem) # O(1)
        
        for thing in other_set: # O(p)
            if new_set.contains(thing) != True: # O(1)
                new_set.add(thing) # O(1)

        return new_set


    def intersection(self, other_set):
        """Returns a subset of elements that are in current set AND the given set."""
        new_set = Set()

        for e in self:
            if other_set.contains(e):
                new_set.add(e)
        
        for elem in other_set:
            if self.contains(elem):
                new_set.add(elem)


    def difference(self, other_set):
        """Returns a subset of elements that are in current set AND
        NOT in the given set."""
        new_set = Set()

        for elem in self: 
            if not other_set.contains(elem):
                new_set.add(elem)
        
        return new_set


    def is_subset(self, subset):
        """Returns True if the given subset is in current set, False otherwise."""
        for elem in subset:
            if not self.contains(elem):
                return False
        return True

if __name__ == "__main__":
    s = Set(1,2,3)
    print(s)
    for i in s:
        print(i)