n = int(input())
for i in range(1 , n + 1):

    if i > 9:
        left = str(i)[0]
        right = str(i)[-1]

        total = (int(left) + int(right))

        if total == 5 or total == 7 or total == 11:
            print (f"{i} -> True")
        else:
            print(f"{i} -> False")

    elif i <= 9:
        if i == 5 or i == 7 or i == 11:
            print(f"{i} -> True")
        else:
            print(f"{i} -> False")
