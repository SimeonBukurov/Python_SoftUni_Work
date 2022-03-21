import sys

commands = input()
min_num = sys.maxsize
while commands != "Stop":
    numbers = int(commands)
    if numbers < min_num:
        min_num = numbers

    commands = input()
else:
    print(min_num)