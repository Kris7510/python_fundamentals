elements = input().split(" ")

stock = {}

for i in range(0, len(elements), 2):

    food = elements[i] # pochva ot 1 index
    quantity = int(elements[i + 1]) # pochva ot 2 index
    stock[food] = quantity

print(stock)