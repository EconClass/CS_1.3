#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    res = find_all_indexes(text, pattern)
    if res != []:
        return True
    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.
    c"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # if len(pattern) == 0: # O(1)
    #     return 0
    
    # index = 0
    
    # for i, char in enumerate(text): # O(n)
    #     if char == pattern[index]: # O(1)
    #         if index == len(pattern) - 1: # O(1)
    #             return i - index # O(1)
    #         index += 1 # O(1)
    #     else:
    #         index = 0 # O(1)
    #         if char == pattern[index]: # O(1)
    #             index += 1 # O(1)

    # return None # O(1)

    res = find_all_indexes(text, pattern)
    if res != []:
        return res[0]
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found.
    Time comlexity: O(n*m)"""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if len(pattern) == 0:
        return list(range(len(text)))
    
    txt_dex = 0
    pat_dex = 0
    found = []

    while txt_dex <= len(text) - len(pattern): # O(n)

        if text[txt_dex] == pattern[pat_dex]:  # O(1)

            while pat_dex < len(pattern): # O(m)

                if text[txt_dex] != pattern[pat_dex]: # O(1)
                    txt_dex -= pat_dex
                    pat_dex = 0
                    break
                
                if pat_dex >= len(pattern) - 1: # O(1)
                    txt_dex -= pat_dex
                    found.append(txt_dex)
                    pat_dex = 0
                    break
                
                txt_dex += 1 
                pat_dex += 1

        txt_dex += 1
    
    return found


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
