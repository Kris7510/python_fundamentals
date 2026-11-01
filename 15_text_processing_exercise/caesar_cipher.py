sentence = input()

cipher = ""

for symbol in sentence:

    cipher += chr(ord(symbol) + 3)

print(cipher)

