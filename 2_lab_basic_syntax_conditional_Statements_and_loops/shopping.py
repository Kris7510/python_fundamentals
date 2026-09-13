budget = int(input())
product_price = input()

while product_price != "End":

    product_price = int(product_price)
    budget -= product_price

    if budget < 0:
        print ("You went in overdraft!")
        break

    product_price  = input()

if product_price == "End" and budget >= 0:
    print ("You bought everything needed.")

