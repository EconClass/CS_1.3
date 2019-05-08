from itertools import permutations

d = open('words')
DICTIONARY = d.read().split('\n')
d.close()
DICTIONARY = frozenset(DICTIONARY)

def unjumble(string):
    perms = [''.join(word) for word in permutations(string)]

    for possible in perms:
        if possible in DICTIONARY:
            return possible

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]

    print(unjumble(args[0]))