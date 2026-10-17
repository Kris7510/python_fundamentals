def operation_even(number):
    number = int(number)
    return number % 2 == 0


nums = input().split()

even_numbers = list(filter(operation_even, nums))

lst = []

for num in even_numbers:
    lst.append(int(num))

print(lst)