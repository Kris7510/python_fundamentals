num = int(input())

for i in range(num):

    operation_num = int(input())

    if operation_num == 88:
        print("Hello")

    elif operation_num == 86:
        print("How are you?")

    elif operation_num < 88 and operation_num != 86:
        print("GREAT!")

    elif operation_num > 88:
        print("Bye.")


