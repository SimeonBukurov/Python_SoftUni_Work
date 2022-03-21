import sys

commands = input()
max_num = -sys.maxsize
while commands != "Stop":
    numbers = int(commands)
    if numbers > max_num:
        max_num = numbers

    commands = input()
else:
    print(max_num)