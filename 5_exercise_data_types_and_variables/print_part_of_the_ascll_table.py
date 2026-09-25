start_opr = int(input())
end_opr = int(input())

for i in range(start_opr, end_opr + 1):
    if i == end_opr:
        print(chr(i))
    else:
        print(chr(i), end=" ")
