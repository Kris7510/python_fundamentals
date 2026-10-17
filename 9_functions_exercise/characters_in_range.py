def operation(first_character, second_character)-> str:

    for i in range(first_character + 1, second_character):
        i = chr(i)
        print(i, end=" ")


first_character = ord(input())
second_character = ord(input())

(operation(first_character, second_character))





