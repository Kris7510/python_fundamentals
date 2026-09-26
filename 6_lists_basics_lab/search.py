n = int(input())
magic_words = input()

all_elements = []
special_elements = []

for _ in range(n):
    elements = input()
    all_elements.append(elements)

    if magic_words in elements:
        special_elements.append(elements)

print(all_elements)
print(special_elements)


