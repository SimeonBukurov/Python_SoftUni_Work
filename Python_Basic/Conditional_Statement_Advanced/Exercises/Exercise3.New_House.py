flower_type = input()
flower_quantity = int(input())
budget = int(input())
costs = 0
if flower_type == 'Roses':
    costs = flower_quantity * 5
    if flower_quantity > 80:
        costs -= costs * 0.10
elif flower_type == 'Dahlias':
    costs = flower_quantity * 3.80
    if flower_quantity > 90:
        costs -= costs * 0.15
elif flower_type == 'Tulips':
    costs = flower_quantity * 2.80
    if flower_quantity > 80:
        costs -= costs * 0.15
elif flower_type == 'Narcissus':
    costs = flower_quantity * 3
    if flower_quantity < 120:
        costs += costs * 0.15
elif flower_type == 'Gladiolus':
    costs = flower_quantity * 2.50
    if flower_quantity < 80:
        costs += costs * 0.2
diff = abs(budget - costs)
if budget >= costs:
    print(f"Hey, you have a great garden with {flower_quantity} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
