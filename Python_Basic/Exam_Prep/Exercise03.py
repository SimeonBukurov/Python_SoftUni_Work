film_budget = float(input())
destination = input()
season = input()
number_of_days = int(input())
price_for_a_day = 0
if destination == "Dubai":
    if season == "Winter":
        price_for_a_day = 45000
    elif season == "Summer":
        price_for_a_day = 40000
elif destination == "Sofia":
    if season == "Winter":
        price_for_a_day = 17000
    elif season == "Summer":
        price_for_a_day = 12500
elif destination == "London":
    if season == "Winter":
        price_for_a_day = 24000
    elif season == "Summer":
        price_for_a_day = 20250

if destination == "Dubai":
    final_price = number_of_days * price_for_a_day
    final_price = final_price - 0.3 * final_price
elif destination == "Sofia":
    final_price = number_of_days * price_for_a_day
    final_price = final_price + 0.25 * final_price
else:
    final_price = number_of_days * price_for_a_day

diff =abs(film_budget - final_price)

if film_budget >= final_price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")