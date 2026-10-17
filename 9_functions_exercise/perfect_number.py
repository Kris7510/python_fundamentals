def operation(num_):
    summary = []

    for number in range(1, num_):
        if num_ % number == 0:
            summary.append(number)

    if sum(summary) == num_:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


num = int(input())
operation(num)
