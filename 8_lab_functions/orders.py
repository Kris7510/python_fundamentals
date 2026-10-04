# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00

def bill (product:str, quantity:int):

    if product == "coffee":
        return f"{quantity * 1.5:.2f}"
    elif product == "water":
        return f"{quantity * 1:.2f}"
    elif product == "coke":
        return f"{quantity * 1.4:.2f}"
    elif product == "snacks":
        return f"{quantity * 2:.2f}"

product_ = input()
quantity_ = int(input())
result = bill(product_, quantity_)

print(result)
