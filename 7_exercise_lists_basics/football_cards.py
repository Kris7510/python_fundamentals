team_a = [(f"A-{number}")for number in range(1, 12)]

team_b = [(f"B-{number}")for number in range(1, 12)]

game_was_terminated = False

players = input().split()

for player in players:

    if player in team_a:
        team_a.remove(player)
        if len(team_a) < 7:
            break

    elif player in team_b:
        team_b.remove(player)
        if len(team_b) < 7:
            break

if len(team_a) < 7 or len(team_b) < 7:
    print (f"Team A - {len(team_a)}; Team B - {len(team_b)}")
    print("Game was terminated")

else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

