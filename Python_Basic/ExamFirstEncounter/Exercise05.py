import sys
best_player = " "
max_goals = -sys.maxsize

while True:
    player_name = input()
    if player_name == "END":
        if max_goals >= 3:
            print(f"{best_player} is the best player!")
            print(f"He has scored {number_of_goals} goals and made a hat-trick !!!")
            break
        else:
            print(f"{best_player} is the best player!")
            print(f"He has scored {number_of_goals} goals.")
            break
        break

    number_of_goals = int(input())
    current_player = player_name
    if number_of_goals > max_goals:
        max_goals = number_of_goals
        best_player = current_player
    if number_of_goals >= 10:
        print(f"{best_player} is the best player!")
        print(f"He has scored {number_of_goals} goals and made a hat-trick !!!")
        break






