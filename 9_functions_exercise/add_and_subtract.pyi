def sum_numbers(num1: int, num2: int) -> int:
    return num1 + num2


def subtract(sum_numbers_: int, num3: int) -> int:
    return sum_numbers_ - num3


def add_and_subtract(first_num: int, second_num: int, third_num: int) -> int:
    sum_result = sum_numbers(first_num, second_num)
    total = subtract(sum_result, third_num)
    return total


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

result = add_and_subtract(num_1, num_2, num_3)

print(result)