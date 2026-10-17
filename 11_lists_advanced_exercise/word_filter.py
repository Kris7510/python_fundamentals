words = input().split(" ")

lst = "\n".join(word for word in words if len(word) % 2 == 0)

print(lst)

# important
