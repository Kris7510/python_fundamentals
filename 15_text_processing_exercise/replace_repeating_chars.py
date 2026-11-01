symbols = input()

last_symbol = ""
final_string = ""

for symbol in symbols:

    if symbol != last_symbol:
        final_string += symbol

    last_symbol = symbol

print(final_string)
