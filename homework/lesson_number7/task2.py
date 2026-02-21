words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def print_words(dictionary):
    for word, count in dictionary.items():
        print(word * count)

print_words(words)
