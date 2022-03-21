first = int(input())
last = int(input())

for character in (chr(number) for number in range(first, last + 1)):
    print(character, end=' ')