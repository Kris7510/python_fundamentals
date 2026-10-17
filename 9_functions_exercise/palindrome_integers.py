def compare (nums_):

    for num in nums_:

        if num == num[::-1]:
            print ("True")
        else:
            print ("False")


nums = input().split(", ")

compare(nums)