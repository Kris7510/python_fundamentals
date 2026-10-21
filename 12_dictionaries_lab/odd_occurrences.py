words = input().split(" ")

stock = {}

for word in words:

    word = word.lower()

    if word not in stock:
        stock[word] = 1
    else:
        stock[word] += 1

lst = []
for key, value in stock.items():
    if value % 2 != 0:
        lst.append(key)

print(" ".join(lst))
