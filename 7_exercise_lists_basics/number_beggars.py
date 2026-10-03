nums = (input()).split(", ")
beggars = int(input())

lst = []

for beggar in range(beggars):
    money = 0

    for index in range(beggar, len(nums), beggars):
        money += int(nums[index])

    lst.append(money)

print(lst) 