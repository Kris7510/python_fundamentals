elements = input().split()

stock = {}

for i in range (0, len(elements), 2):              # do 9-tiq red e klasichesko vzemane na dva elementa

    product = elements[i]
    quantity = elements[i + 1]
    stock[product] = quantity

product_to_search = input().split()

for product in product_to_search:
    if product in elements:                                    # proverka dali gi imame veche
        print(f"We have {stock[product]} of {product} left")

    else:
        print(f"Sorry, we don\'t have {product}")