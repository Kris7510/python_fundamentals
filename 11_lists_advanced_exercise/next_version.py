current_version = input().split(".")\

lst = [i for i in current_version]

operating_data = int("".join(lst)) + 1

lst_2 = [i for i in str(operating_data)]

final_lst = (".".join(lst_2))

print(final_lst)
