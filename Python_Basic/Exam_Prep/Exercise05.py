first_egg_count = int(input())
second_egg_count = int(input())
command = input()
while True:
    if command == "End of battle":
        print(f"Player one has {first_egg_count} eggs left.")
        print(f"Player two has {second_egg_count} eggs left.")
        break

    elif command == "one":
        second_egg_count -= 1
    elif command == "two":
        first_egg_count -= 1

    if first_egg_count <= 0:

        print(f"Player one is out of eggs. Player two has {second_egg_count} eggs left.")
        break
    elif second_egg_count <= 0:
        print(f"Player two is out of eggs. Player one has {first_egg_count} eggs left.")
        break
    command = input()