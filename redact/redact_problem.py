def redact(words, banned_words):
    '''Returns a list of strings that are in the first list of strings,
    but are not in the second list of strings
    Time complexity: O(n + m)'''

    okay = []
    banned_words = set(banned_words) # O(m)

    for word in words: # O(n)
        if word not in banned_words: # O(1)
            okay.append(word) # *O(1)

    return okay