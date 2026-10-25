words = input()

dictionary = {}
for word in words:

    if word == " ":
        continue

    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")