from math import ceil
number_of_people = int(input())
capacity = int(input())

course = ceil(number_of_people / capacity)

print(course)