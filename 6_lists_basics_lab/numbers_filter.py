n = int(input())

list_even = []
list_odd = []
list_negative = []
list_positive = []

for i in range(n):
    num = int(input())

    if num % 2 == 0:
        list_even.append(num)
    if num % 2 != 0:
        list_odd.append(num)
    if num < 0 :
        list_negative.append(num)
    if num >= 0 :
        list_positive.append(num)

cmd = input()

if cmd == "even":
    print(list_even)
elif cmd == "odd":
    print(list_odd)
elif cmd == "negative":
    print(list_negative)
elif cmd == "positive":
    print(list_positive)