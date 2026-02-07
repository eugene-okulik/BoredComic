sentence = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
            "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

words = sentence.split()
fin_words = []

for word in words:
    punctuation = ""

    if word[-1] in ",.":
        punctuation = word[-1]
        word = word[:-1]

    fin_words.append(word + "ing" + punctuation)

print(" ".join(fin_words))
