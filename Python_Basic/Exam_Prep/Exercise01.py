#strawberries, bananas, oranges, berries
#sum for strawberries = price for kilo * amount
#sum for banana = price for kilo * amount
#sum for oranges = price for kilo * amount
#sum for berries = price for kilo * amount
#full sum = sum of all fruits

strawberry_price = float(input())
banana_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberry_quantity = float(input())

strawberry_sum = strawberry_price * strawberry_quantity

raspberries_price = strawberry_price / 2
raspberries_sum = raspberries_price * raspberries_quantity

banana_price = raspberries_price - 0.8 * raspberries_price
banana_sum = banana_price * banana_quantity

oranges_price = raspberries_price - 0.4 * raspberries_price
oranges_sum = oranges_price * oranges_quantity

total_sum = strawberry_sum + raspberries_sum + banana_sum + oranges_sum

print(f'{total_sum:.2f}')