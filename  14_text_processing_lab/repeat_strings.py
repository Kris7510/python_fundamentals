symbols = input().split()

final_symbols = ""

for symbol in symbols:

    symbol_len = len(symbol)
    final_symbols += symbol_len * symbol

print("".join(final_symbols))

