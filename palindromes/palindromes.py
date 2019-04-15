#!python

import string

LETTERS = frozenset(string.ascii_letters)

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    left = 0
    right = len(text) - 1

    while left < right:
        while text[left] not in LETTERS:
            left += 1

        while text[right] not in LETTERS:
            right -= 1
            
        if text[left] != text[right]:
            if text[left].lower() != text[right].lower():
                return False

        left += 1
        right -= 1

    return True

def is_palindrome_recursive(text, left=None, right=None):
    
    if left == None and right == None:
        left = 0
        right = len(text) - 1

    if left > right:
        return True

    while text[left] not in LETTERS:
        left += 1

    while text[right] not in LETTERS:
        right -= 1
        
    if text[left] != text[right]:
        if text[left].lower() != text[right].lower():
            return False    

    left += 1
    right -= 1

    return is_palindrome_recursive(text, left, right)

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
