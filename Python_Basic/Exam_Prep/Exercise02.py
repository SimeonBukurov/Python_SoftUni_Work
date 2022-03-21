budget = float(input())
count_nights = int(input())
price_per_night = float(input())
percent = int(input())
if count_nights > 7:
    price_per_night = price_per_night - 0.05 * price_per_night

sum_nights = price_per_night * count_nights
sum_extra = (percent / 100) * budget
total_sum = sum_nights + sum_extra
diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f"{diff:.2f} leva needed.")