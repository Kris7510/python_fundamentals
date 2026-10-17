first_list = input().split(", ")
second_list = input().split(", ")

result = []

for word in first_list:
    for word2 in second_list:
        if word in word2:
            result.append(word)
            break

print(result)