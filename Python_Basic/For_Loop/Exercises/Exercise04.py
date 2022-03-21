lily_age = int(input())
price_of_washer = float(input())
price_of_toy = int(input())
saved_money = 0
number_of_toys = 0
for num in range(1,lily_age + 1):
    if num % 2 == 0:
        saved_money += ((num / 2) * 10) - 1
    else:
        number_of_toys += 1


total_saved_money = saved_money + (number_of_toys * price_of_toy)
diff = abs(total_saved_money - price_of_washer)
if total_saved_money >= price_of_washer:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
