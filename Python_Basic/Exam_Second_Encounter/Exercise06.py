number_of_locations = int(input())

for loc in range(number_of_locations):
    gold_income_daily_total = 0
    expected_average_income = float(input())
    number_of_days_for_mining_in_this_loc = int(input())
    for days_working in range(1, number_of_days_for_mining_in_this_loc + 1):
            gold_income_daily = float(input())
            gold_income_daily_total += gold_income_daily
            average_income = gold_income_daily_total / number_of_days_for_mining_in_this_loc
            total = average_income
    diff = abs(expected_average_income - total)
    if total >= expected_average_income:
        print(f"Good job! Average gold per day: {total:.2f}.")
    else:
        print(f"You need {diff:.2f} gold.")


