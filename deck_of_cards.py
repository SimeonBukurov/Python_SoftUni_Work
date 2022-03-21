cards = input().split(", ")
n = int(input())

for i in range(1, n + 1):
    split_list = input().split(", ")
    command = split_list[0]


    if command == "Add":
        card_name = split_list[1]
        if card_name in cards:
            print("Card is already in the deck")
        else:
            cards.append(card_name)
            print("Card successfully added")
    if command == "Remove":
        card_name = split_list[1]
        if card_name not in cards:
            print("Card not found")
        else:
            cards.remove(card_name)
            print("Card successfully removed")
    if command == "Remove At":
        index = split_list[1]
        if int(index) > len(cards):
            print("Index out of range")
        else:
            cards.pop(int(index))
            print("Card successfully removed")
    if command == "Insert":
        index = split_list[1]
        card_name = split_list[2]
        if int(index) > len(cards):
            print("Index out of range")
        elif card_name in cards:
            print("Card is already added")
        else:
            cards.insert(int(index), card_name)
            print("Card successfully added")
print(', '.join(cards))