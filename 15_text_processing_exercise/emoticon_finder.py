sentence = input()

for i in range(len(sentence) - 1):
    if sentence[i] == ':':
        print(f"{sentence[i]}{sentence[i+1]}")