#!python

import string

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # ================================================================
    # This implentation will use the following formula for conversion:
    #     target = D * B^(n)
    # target = Base 10 equivalent of given digits of any base
    # D = numeric value of character (example: 'd' = 13)
    # B = number base of input (example: B = 2 for binary input)
    # n = index of current value within the input string
    # ================================================================

    result = 0
    # compare allows a way to find D for any given character in an input
    # compare = '0123456789abcdefghijklmnopqrstuvwxyz'
    compare = string.digits + string.ascii_lowercase
    counter = len(digits)

    for d in digits:
        counter -= 1
        multiplier = base ** counter
        result += compare.index(d) * multiplier
    return result

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    # ======================CUSTOM======================
    # compare = '0123456789abcdefghijklmnopqrstuvwxyz'
    compare = string.digits + string.ascii_lowercase
    dividend = number
    result = ''
    
    while dividend > 0:
        div_tup = divmod(dividend, base)
        dividend = div_tup[0]

        # Use the remainder to index the desired corresponding character
        result = compare[div_tup[1]] + result

    return result


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    # ====================== CUSTOM ======================
    result = decode(digits, base1)
    return encode(result, base2)

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')

if __name__ == '__main__':
    main()