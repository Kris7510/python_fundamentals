sentence = input().split(" ")

lst = []

for word in sentence:

    letters = ""
    number = ""

    for symbol in word:
        if symbol.isdigit():
            number += symbol
        else:
            letters += symbol
    if len(letters) > 1:
        letters = letters[-1] + letters[1:-1] + letters[0]
    lst.append(chr(int(number)) + letters)

print(" ".join(lst))
