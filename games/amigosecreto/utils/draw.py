from random import shuffle


def game_draw(players):
    '''Selecting player pairs
    '''
    pairs = []
    shuffle(players)
    len_players = len(players)
    for player in range(len_players):
        # Border condition
        if player == len_players - 1:
            pairs.append((players[player], players[0]))
        else:
            pairs.append((players[player], players[player + 1]))

    return pairs
