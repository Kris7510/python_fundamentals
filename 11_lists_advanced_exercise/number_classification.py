numbers = input().split(", ")

positive_numbers = ", ".join([positive_number for positive_number in numbers if int(positive_number) >= 0])

negative_numbers = ", ".join([negative_numbers for negative_numbers in numbers if int(negative_numbers) < 0])

even_numbers = ", ".join([even_numbers for even_numbers in numbers if int(even_numbers) % 2 == 0])

odd_numbers = ", ".join([odd_numbers for odd_numbers in numbers if int(odd_numbers) % 2 != 0])

print(f"Positive: {positive_numbers}")
print(f"Negative: {negative_numbers}")
print(f"Even: {even_numbers}")
print(f"Odd: {odd_numbers}")
