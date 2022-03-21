import math

width_of_the_spaceship = float(input())
length_of_the_spaceship = float(input())
height_of_the_spaceship = float(input())
average_height_of_the_astronauts = float(input())
spaceship_area = width_of_the_spaceship * length_of_the_spaceship * height_of_the_spaceship
area_of_one_room = (average_height_of_the_astronauts + 0.40) * 2 * 2
people_capable_of_living_there = spaceship_area / area_of_one_room
if 3 <= people_capable_of_living_there <= 10:
    print(f"The spacecraft holds {math.floor(people_capable_of_living_there)} astronauts.")
elif people_capable_of_living_there < 3:
    print("The spacecraft is too small.")
elif people_capable_of_living_there > 10:
    print("The spacecraft is too big.")