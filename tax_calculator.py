import math
vehicle = input().split(">>")
initial_tax = 0
total_tax = 0
for i in range(len(vehicle)):
    explode = vehicle[i]
    car_separator = explode.split(" ")
    type_of_car = car_separator[0]
    years = car_separator[1]
    km_traveled = car_separator[2]
    if type_of_car != "sports" and type_of_car != "heavyDuty" and type_of_car != "family":
        print("Invalid car type.")
        car_separator.remove(type_of_car)
        car_separator.remove(years)
        car_separator.remove(km_traveled)
        continue
    elif type_of_car == "family":
        initial_tax = 50
        total_initial_tax = math.floor(int(km_traveled) / 3000) * 12 + (int(initial_tax) - int(years) * 5)
        total_tax += total_initial_tax
        print(f"A {type_of_car} car will pay {total_initial_tax:.2f} euros in taxes.")
    elif type_of_car == "heavyDuty":
        initial_tax = 80
        total_initial_tax = math.floor(int(km_traveled) / 9000) * 14 + (initial_tax - int(years) * 8)

        total_tax += total_initial_tax
        print(f"A {type_of_car} car will pay {total_initial_tax:.2f} euros in taxes.")
    elif type_of_car == "sports":
        initial_tax = 100
        total_initial_tax = math.floor(int(km_traveled) / 2000) * 18 + (initial_tax - int(years) * 9)
        total_tax += total_initial_tax
        print(f"A {type_of_car} car will pay {total_initial_tax:.2f} euros in taxes.")
    if len(explode) <= 0:
        break
print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")

