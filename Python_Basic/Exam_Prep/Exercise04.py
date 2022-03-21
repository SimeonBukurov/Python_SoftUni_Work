import math

number_of_days = int(input())
full_amount_of_food = float(input())
total_biscuit = 0
total_dog = 0
total_cat =0
for days in range(1, number_of_days + 1):
    food_dog = int(input())
    total_dog += food_dog
    food_cat = int(input())
    total_cat += food_cat

    if days % 3 == 0:
     total_of_food_ate_for_a_day = food_cat + food_dog
     biscuits_eaten = total_of_food_ate_for_a_day * 0.10
     total_biscuit += biscuits_eaten

print(f"Total eaten biscuits: {round(total_biscuit)}gr.")

total_eaten_food = total_dog + total_cat
percent_eaten_food = (total_eaten_food / full_amount_of_food) * 100
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")

percent_dog = (total_dog / total_eaten_food) * 100

print(f"{percent_dog:.2f}% eaten from the dog.")

percent_cat = (total_cat / total_eaten_food) * 100

print(f"{percent_cat:.2f}% eaten from the cat.")