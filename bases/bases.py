#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

# def bin_to_int(digits = '101101'):
#     digits = digits[::-1]
#     result = 0
#     for d in digits:
#         if d[1] == '1':
#             # print('INDEX', d[0])
#             result += 1 << d[0]
#     print('RESULT', result)
#     return result

# def hex_to_int(digits):
#     result = 0
#     compare = list(string.digits + string.ascii_lowercase)
#     digits = list(digits)
#     counter = len(digits)

#     for d in digits:
#         counter -= 1
#         multiplier = 16 ** digits.index(d)
#         result += compare.index(d) * multiplier
#     print(result)

#     return result

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    # ================================================================
    # This implentation will use the following formula for conversion:
    #     D * B^(n)
    # D = numeric value of character (example: 'd' = 13)
    # B = number base of input (example: B = 2 for binary input)
    # n = index of current value within the input string
    # ================================================================
    result = 0
    # compare allows a way to find D for any given character in an input
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
    compare = string.digits + string.ascii_lowercase
    dividend = number
    result = ''
    
    while dividend > 0:
        div_tup = divmod(dividend, base)
        dividend = div_tup[0]

        # Use the remainder to index the desired corresponding character
        result += compare[div_tup[1]]

    return result[::-1]


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
    # # hex_to_int('a')
    # main()
    encode(10, 2)