wagons  = int(input())

wagons = "0" * wagons

lst = [int(num) for num in wagons]

command = input().split(" ")

while command[0] != "End":

    if command[0] == "add":
        lst [-1] += (int(command[1]))

    elif command[0] == "insert":
         wagon = int(command[1])
         people = int(command[2])
         lst [wagon] += people

    elif command[0] == "leave":
        wagon = int(command[1])
        people = int(command[2])
        lst[wagon] -= people

    command = input().split(" ")

print(lst)

