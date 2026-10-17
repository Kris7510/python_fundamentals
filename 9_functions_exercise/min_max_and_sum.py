def operation_nums(nums_):
    lst = []

    for num in nums_:
        num = int(num)
        lst.append(num)

    print(f"The minimum number is {min(lst)}")
    print(f"The maximum number is {max(lst)}")
    print(f"The sum number is: {sum(lst)}")


nums = input().split()

operation_nums(nums)