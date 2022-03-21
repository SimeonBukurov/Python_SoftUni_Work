red_card_players = input().split(' ')
team_A_players = 11
team_B_players = 11
players_loses = []
condition = False
for card in red_card_players:
    if card not in players_loses:
        players_loses.append(card)
        if 'A' in card:
            team_A_players -= 1
        elif 'B' in card:
            team_B_players -= 1
        if team_A_players < 7 or team_B_players < 7:
            condition = True
            break

print(f"Team A - {team_A_players}; Team B - {team_B_players}")
if condition:
    print("Game was terminated")