type_project = input()
rows = int(input())
columns = int(input())

all_places = rows * columns
profit = 0

if type_project == "Premiere":
    profit = all_places * 12

elif type_project == "Normal":
    profit = all_places * 7.5
elif type_project == "Discount":
    profit = all_places * 5
print(f'{profit:.2f} leva')