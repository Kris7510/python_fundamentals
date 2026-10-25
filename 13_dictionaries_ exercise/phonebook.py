phonebook = {}

while True:
    command = input()

    if "-" not in command:
        break

    name, phone = command.split("-")
    phonebook[name] = phone

searches = int(command)

for search in range(searches):
    searches_name = input()

    if searches_name in phonebook:
        print(f"{searches_name} -> {phonebook[searches_name]}")
    else:
        print(f"Contact {searches_name} does not exist.")
