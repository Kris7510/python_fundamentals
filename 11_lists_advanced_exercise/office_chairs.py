rooms = int(input())

free_chairs = 0

for room in range(1, rooms + 1):

    chairs, visitors = input().split(" ")

    if len(chairs) > int(visitors):
        free_chairs += len(chairs) - int(visitors)

    elif len(chairs) < int(visitors):
        free_chairs_in_room =  int(visitors) - len(chairs)
        free_chairs -= free_chairs_in_room

        print(f"{free_chairs_in_room} more chairs needed in room {room}")

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")







