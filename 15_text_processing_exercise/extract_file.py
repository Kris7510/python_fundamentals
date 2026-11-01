full_file_name = input().split('\\')

name, extension = (full_file_name[-1]).split(".")

print(f"File name: {name}")
print(f"File extension: {extension}")

