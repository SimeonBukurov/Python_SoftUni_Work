Peter_Budget = float(input())
number_of_video_cards = int(input())
number_of_processors = int(input())
number_of_RAM = int(input())
price_of_video_cards = number_of_video_cards * 250
price_of_processors = (price_of_video_cards * 0.35) * number_of_processors
price_of_RAM = (price_of_video_cards * 0.10) * number_of_RAM
price_sum = price_of_RAM + price_of_processors + price_of_video_cards
if number_of_video_cards > number_of_processors:
    price_sum -= price_sum * 0.15
else:
    price_sum = price_sum
diff = abs(Peter_Budget - price_sum)
diff_loose = abs(price_sum - Peter_Budget)
if Peter_Budget >= price_sum:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f"Not enough money! You need {diff_loose:.2f} leva more!")
