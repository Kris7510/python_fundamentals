chr_lines = int(input())
total = 0

for i in range(chr_lines):

    symbols = input()
    total += ord(symbols)

print(f"The sum equals: {total}")

