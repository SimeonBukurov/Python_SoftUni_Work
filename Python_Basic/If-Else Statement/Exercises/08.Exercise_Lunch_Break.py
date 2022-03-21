import math
name_of_the_serial = input()
episode_runtime = int(input())
break_runtime = int(input())

time_for_lunch = break_runtime * 1/8
time_for_break = break_runtime * 1/4
left_time = break_runtime - time_for_lunch - time_for_break

diff = abs(left_time - episode_runtime)

if left_time >= episode_runtime:
    print(f'You have enough time to watch {name_of_the_serial} and left with {math.ceil(diff)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_of_the_serial}, you need {math.ceil(diff)} more minutes.")

