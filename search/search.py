#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index >= len(array):
        return None

    if array[index] == item:
        return index

    index += 1
    return linear_search_recursive(array, item, index)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0
    right = len(array) - 1
    

    while True:
        middle = (right + left) // 2
        mid_elem = array[middle]

        if mid_elem == item: # Check if we have what we need
            return middle
        # Adjust search to which half to look for item in   
        elif mid_elem < item:
            left = middle + 1
        elif mid_elem > item:
            right = middle - 1
        
        # We reached the end of the search
        if left == right:
            if array[left] == item: # Target is last or first in the list
                return left # Found it!
            return None # It ain't there.


def binary_search_recursive(array, item, left=None, right=None):
    if left == None and right == None:
        left = 0
        right = len(array) - 1
    
    middle = ( left + right ) // 2
    mid_elem = array[middle]

    if mid_elem == item: # Check if we have what we need
            return middle
    # Adjust search to which half to look for item in   
    elif mid_elem < item:
        left = middle + 1
    elif mid_elem > item:
        right = middle - 1
    
    # We reached the end of the search
    if left == right:
        if array[left] == item: # Target is last or first in the list
            return left # Found it!
        return None # It ain't there.
    
    return binary_search_recursive(array, item, left, right)
