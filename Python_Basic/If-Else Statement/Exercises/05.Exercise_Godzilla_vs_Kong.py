budget_film = float(input())
number_of_statists = int(input())
price_for_dressing_for_one_statist = float(input())
decor = budget_film * 0.10
clothing_for_all_statist = price_for_dressing_for_one_statist * number_of_statists
if number_of_statists > 150:
    clothing_for_all_statist -= clothing_for_all_statist * 0.10
total_cost = decor + clothing_for_all_statist
diff = abs(budget_film - total_cost)
if total_cost <= budget_film:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')