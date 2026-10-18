numbers =  [int(number) for number in input().split(", ")]

current_group = 10

while numbers:
    operating_numbers = [number for number in numbers if number <= current_group]
    print(f"Group of {current_group}'s: {operating_numbers}")

    final_numbers = [number for number in operating_numbers if number in numbers]

    for number in final_numbers:
        if number in numbers:
            numbers.remove(number)

    current_group += 10

    if current_group > 100:
        break
