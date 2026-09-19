
delivery = int(input())
total_price = 0

for i in range(delivery):
    price_per_capsul = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not 0.01 <= price_per_capsul <= 100:
        continue

    if not 1 <= days <= 31:
        continue

    if not 1 <= capsules_per_day <= 2000:
        continue

    total_capsules = days * capsules_per_day
    price = total_capsules * price_per_capsul

    total_price += price

    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")