import math

number_of_days = int(input())
daily_km = float(input())
total_km = 0
for days in range(0, number_of_days + 1):
    percent = int(input()) / 100
    daily_km = daily_km + (daily_km * (percent))
    total_km += daily_km

diff = abs(total_km - 1000)
if total_km >= 1000:
    print(f"You've done a great job running {math.floor(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.floor(diff)}")