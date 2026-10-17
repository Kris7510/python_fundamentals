def password_validator(current_password):

    counter = 0

    if not 6 <= len(current_password) <= 10:
        print("Password must be between 6 and 10 characters")

    if not current_password.isalnum():
        print("Password must consist only of letters and digits")

    for symbol in current_password:

        if symbol.isdigit():
            counter += 1

    if counter < 2:
        print("Password must have at least 2 digits")

    if (6 <= len(current_password) <= 10
            and current_password.isalnum()
            and counter >= 2):
        print("Password is valid")

password = input()

password_validator(password)

