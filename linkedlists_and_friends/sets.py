#!python

from hashtable import HashTable

class Set(object):
    def __init__(self, items=[]):
        """Initialize set as an empty hash table."""
        self.table = HashTable()

        if len(items) != 0:
            for item in items: # O(i)
                self.table.set(item, None) # O(1)

    def __iter__(self):
        """Allows Set class to be iterable."""
        return iter(self.table.keys()) # O(n)

    def __repr__(self):
        """Return a string representation of this set."""
        items = ['{!r}'.format(key) for key in self.table.keys()]
        return '{' + ', '.join(items) + '}'

    def size(self):
        """Returns the number of elements in the set."""
        # Constant time to look up object properties.
        return self.table.length() # O(1)

    def contains(self, elem):
        """Returns True if element is in the set and False otherwise.
        NOTE: The Set.contains() uses the HashTable.contains().
        Best and Worst case running time for Set.contains() is the same as HashTable.contains().
            *O(1) due to Hashtable's _resize()"""

        # Pass the element as a key to call the hash table method contains().
        # The contains() method checks to see if the key is in the hash table.
        return self.table.contains(elem)

    def add(self, elem):
        """Adds item to the set.
        Best and Worst case running time: O(1)"""
        if not self.contains(elem): # O(1)
            self.table.set(elem, None) # *O(1)
        else:
            raise KeyError("Item is already in the set.")

    def remove(self, elem):
        """Removes item to the set.
        Best and Worst case running time: O(1)"""
        if self.contains(elem): # O(1)
            self.table.delete(elem) # *O(1)
        else:
            raise KeyError("Item not in set. ")

    def union(self, other_set):
        """Returns a subset of elements that are in current set OR the other set.
        Best and Worst case running time: O(n + p)
        Where:  n = number of elements in current set
                m = number of elements in other set"""
        new_set = Set()

        for elem in self: # O(n)
           new_set.add(elem) # O(1)
        
        for thing in other_set: # O(m)
            if new_set.contains(thing) != True: # O(1)
                new_set.add(thing) # O(1)

        return new_set


    def intersection(self, other_set):
        """Returns a subset of elements that are in current set AND the other set.
        Best and Worst case running time: O(n + m)
        Where:  n = number of elements in current set
                m = number of elements in other set"""
        new_set = Set()

        if self.size() > other_set.size():
            smaller = other_set
            bigger = self
        else:
            smaller = self
            bigger = other_set
        
        for elem in smaller: # O(m)
            if bigger.contains(elem): # O(1)
                new_set.add(elem) # O(1)

        return new_set

    def difference(self, other_set):
        """Returns a subset of elements that are in current set AND
        NOT in the other set.
        Best and Worst case running time: O(n)
        Where:  n = number of elements in current set"""
        new_set = Set()

        for elem in self: # O(n)
            if not other_set.contains(elem): # O(1)
                new_set.add(elem) # O(1)
        
        return new_set

    def is_subset(self, subset):
        """Returns True if the given subset is in current set, False otherwise.
        Best and Worst case running time: O(m)
        Where:  m = number of elements in subset"""
        if subset.size() > self.size():
            return False
        
        for elem in subset: # O(m)
            if not self.contains(elem): # O(1)
                return False
        return True

if __name__ == "__main__":
    # print(Set([1,2,3]))
    s = Set([1,2,3])
    print(s)
    for i in s:
        print(i)