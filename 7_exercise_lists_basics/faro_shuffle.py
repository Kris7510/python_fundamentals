cards = input().split()

number_of_shuffling = int(input())

for current_shuffling in range(number_of_shuffling):

    middle_part = len(cards) // 2

    left_part = cards[:middle_part]
    right_part = cards[middle_part:]

    deck_after_shuffle = []

    for card in range(len(left_part)):
        deck_after_shuffle.append(left_part[card])
        deck_after_shuffle.append(right_part[card])

    cards = deck_after_shuffle

print(cards)