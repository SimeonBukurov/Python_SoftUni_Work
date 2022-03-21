starting_n = int(input())
ending_n = int(input())
magic_n = int(input())
combination = 0
for starting_n in range(starting_n, starting_n + 1):
    for ending_n in range(ending_n, ending_n + 1):
        if starting_n + ending_n != magic_n:
            combination += 1
            print(f"{combination} combinations - neither equals {magic_n}")

        else:

            print(f"Combination N:{combination}")
            print(f"({starting_n}+{ending_n} = {magic_n})")
