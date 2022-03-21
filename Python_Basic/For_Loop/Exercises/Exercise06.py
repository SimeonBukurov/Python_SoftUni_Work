name_of_the_actor = input()
points_of_academy = float(input())
judges = int(input())
award = 0
total = 0
for n in range(judges):
    name = input()
    points = float(input())
    award += len(name) * points / 2
    total = award + points_of_academy
    if total > 1250.5:
        break
diff = abs(total - 1250.5)

if total > 1250.5:
    print(f"Congratulations, {name_of_the_actor} got a nominee for leading role with {total:.1f}!")

else:
    print(f"Sorry, {name_of_the_actor} you need {diff:.1f} more!")