number_of_lines = int(input())
capacity = 0
for _ in range(number_of_lines):
    litres_of_water = int(input())
    if litres_of_water + capacity <= 255:
        capacity += litres_of_water
        continue
    print('Insufficient capacity!')
print(capacity)