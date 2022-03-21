the_days_of_the_adventure = int(input())
count_of_players = int(input())
groups_energy = float(input())
current_energy = groups_energy
water = float(input())
food = float(input())
total_water = the_days_of_the_adventure * count_of_players * water
current_water = total_water
total_food = the_days_of_the_adventure * count_of_players * food
current_food = total_food
for days in range(1, the_days_of_the_adventure + 1):
    if days % 1 == 0:
        energy_lost_a_day = float(input())
        current_energy = current_energy - energy_lost_a_day
        if current_energy <= 0:
            print(f"You will run out of energy." + \
                 f" You will be left with {current_food:.2f} food and {current_water:.2f} water.")
            break
    if days % 2 == 0:
        current_water = current_water * 0.7
        current_energy = current_energy + (current_energy * 0.05)
    if days % 3 == 0:
        current_food = current_food - (current_food / count_of_players)
        current_energy += current_energy * 0.10

if current_energy >= 0:
    print(f"You are ready for the quest. You will be left with - {current_energy:.2f} energy!")
