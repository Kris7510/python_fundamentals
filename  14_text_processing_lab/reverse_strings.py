word = input()

while True:

    if word == "end":
        break

    else:

        reversed_word = word[::-1]
        print(f"{word} = {reversed_word}")

        word = input()




