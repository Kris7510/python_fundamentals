banded_word = input().split(", ")
sentence = input()

for word in banded_word:
    while word in sentence:
        sentence = sentence.replace(word, len(word) * "*")

print(sentence)
