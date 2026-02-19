
words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def word_dict(word):
    for x in word:
        print(x * word[x])


word_dict(words)

