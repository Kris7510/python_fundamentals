total = int(input())

total_electrons = 0
lst = []

for number in range(1, total + 1):

    current_shell = 2 * (number ** 2)

    if total_electrons + current_shell < total:
        total_electrons += current_shell
        lst.append(current_shell)
    else:
        lst.append(total - total_electrons)
        break

print(lst)