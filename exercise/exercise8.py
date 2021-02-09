print("choose: rock, paper or scissors")

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_1 = str(input("player1: "))
    player_2 = str(input("player2: "))
    p1 = game_dict.get(player_1)
    p2 = game_dict.get(player_2)
    dif = p1 - p2

    if dif in [-1, 2]:
        print('player 1 wins.')
        if str(input('one more game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player 2 wins.')
        if str(input('one more game, yes or no?\n')) == 'yes':
            continue
        else:
            break
    else:
        print('tie.')
        break
