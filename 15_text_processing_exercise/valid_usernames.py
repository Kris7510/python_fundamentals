
def length_of_username(username: str) -> bool:
    return 3 <= len(username) <= 16


def valid_username(username: str) -> bool:
    for character in username:
        if not (character.isalpha() or character.isdigit() or character == "_" or character == "-"):
            return False
    return True


def is_valid(username: str) -> bool:
    return length_of_username(username) and valid_username(username)


usernames = input().split(", ")

for username in usernames:
    if is_valid(username):
        print(username)

