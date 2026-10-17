def operation(word_):
    list_of_vowels = ['a', 'e', 'i', 'o', 'u']

    lst_after_operation = [symbol for symbol in word_ if symbol.lower() not in list_of_vowels]

    print("".join(lst_after_operation))

word = input()

operation(word)