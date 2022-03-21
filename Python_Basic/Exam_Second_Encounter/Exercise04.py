N = int(input())
M = int(input())
S = int(input())

for house in range(M, N - 1, -1):
    if house % 2 == 0 and house % 3 == 0:
        if house == S:
            break
        print(house, end=' ')