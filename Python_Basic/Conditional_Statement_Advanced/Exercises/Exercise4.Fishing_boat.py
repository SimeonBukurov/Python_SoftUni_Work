budget = int(input())
season = input()
fisherman_amount = int(input())
fee = 0
if season == "Spring":
    fee = 3000
    if fisherman_amount <= 6:
        fee -= fee * 0.10
    elif 7 <= fisherman_amount <= 11:
        fee -= fee * 0.15
    elif 12 <= fisherman_amount:
        fee -= fee * 0.25
    if fisherman_amount % 2 == 0:
        fee -= fee * 0.05
elif season == "Summer":
    fee = 4200
    if fisherman_amount <= 6:
        fee -= fee * 0.10
    elif 7 <= fisherman_amount <= 11:
        fee -= fee * 0.15
    elif fisherman_amount >= 12:
        fee -= fee * 0.25
    if fisherman_amount % 2 == 0:
        fee -= fee * 0.05
elif season == "Autumn":
    fee = 4200
    if fisherman_amount <= 6:
        fee -= fee * 0.10
    elif 7 <= fisherman_amount <= 11:
        fee -= fee * 0.15
    elif fisherman_amount >= 12:
        fee -= fee * 0.25
elif season == "Winter":
    fee = 2600
    if fisherman_amount <= 6:
        fee -= fee * 0.10
    elif 7 <= fisherman_amount <= 11:
        fee -= fee * 0.15
    elif fisherman_amount >= 12:
        fee -= fee * 0.25
    if fisherman_amount % 2 == 0:
        fee -= fee * 0.05
diff = abs(budget - fee)
if budget > fee:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")