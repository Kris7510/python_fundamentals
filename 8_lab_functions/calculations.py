def solve (operation_:str, number1:int, number2:int ) -> int | str:
    if operation_ == "add":
        return number1 + number2
    elif operation == "subtract":
        return number1 - number2
    elif operation == "multiply":
        return number1 * number2
    elif operation == 'divide':
        return number1 // number2
    else:
        return f"Invalid operation"


operation = input()
number_1 = int(input())
number_2 = int(input())

result = solve(operation, number_1, number_2)

print(result)





