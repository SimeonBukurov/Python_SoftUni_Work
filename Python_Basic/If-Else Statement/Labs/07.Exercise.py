import math
figure = str(input())
if figure == "square":
    number = float(input())
    result = number * number
    print(f"{result:.3f}")
elif figure == "rectangle":
    numberA = float(input())
    numberB = float(input())
    result = numberA * numberB
    print(f"{result:.3f}")
elif figure == "circle":
    number = float(input())
    result = math.pi * number * number
    print(f"{result:.3f}")
elif figure == "triangle":
    number = float(input())
    height = float(input())
    result = 1/2 * height * number
    print(f"{result:.3f}")