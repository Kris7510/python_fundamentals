words = input().split(" ")
word_for_searching = input()

lst_palindrome = []
count_palindrome = 0

for word in words:

    if word == word[::-1]:
        lst_palindrome.append(word)

    if word == word_for_searching:
        count_palindrome += 1

print(lst_palindrome)
print(f"Found palindrome {count_palindrome} times")



