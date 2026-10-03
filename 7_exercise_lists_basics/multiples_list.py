start_num = int(input())
num_of_multiply = int(input())

lst = []

for i in range (1, num_of_multiply + 1):

    i = start_num * i

    lst.append(i)
print(lst)


