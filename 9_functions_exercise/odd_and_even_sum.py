def operation_even(num:str):
    sum_even = 0

    for character in num:
        num_in_int = int(character)
        if num_in_int % 2 == 0:
            sum_even += num_in_int
    return f"Even sum = {sum_even}"

def operation_odd(num:str):
    sum_odd = 0

    for character in num:
        num_in_int = int(character)
        if num_in_int % 2 != 0:
            sum_odd += num_in_int
    return f"Odd sum = {sum_odd}"


num = input()

lst = ", ".join([operation_odd(num), operation_even(num)])

print(lst)