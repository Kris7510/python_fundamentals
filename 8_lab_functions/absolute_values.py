numbers = input().split()

lst = []

for number in numbers:

    number = float(number)

    lst.append(abs(float(f"{number}")))

print(lst)