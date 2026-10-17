def smallest_of_three_numbers(lst_data:list ) -> int:

  return min(lst_data)

first_num = int(input())
second_num = int(input())
third_num = int(input())

lst = [first_num, second_num, third_num]

print (smallest_of_three_numbers(lst))