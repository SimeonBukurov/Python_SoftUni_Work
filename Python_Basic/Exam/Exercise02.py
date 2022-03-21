import math

number_of_day_santa_is_away = int(input())
food_left = int(input())
food_for_first_deer = float(input())
food_for_second_deer = float(input())
food_for_third_deer = float(input())

first_deer_ate = number_of_day_santa_is_away * food_for_first_deer
second_deer_ate = number_of_day_santa_is_away * food_for_second_deer
third_deer_ate = number_of_day_santa_is_away * food_for_third_deer
food_needed = first_deer_ate + second_deer_ate + third_deer_ate
diff = abs(food_left - food_needed)

if food_left >= food_needed:
    print(f"{math.ceil(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")