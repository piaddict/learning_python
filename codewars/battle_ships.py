# Return Hash
# { 'sunk': 0, 'damaged': 2 , 'not_touched': 1, 'points': 0 }


def damaged_or_sunk(board, attacks):
    result = {'sunk': 0, 'damaged': 0, 'not_touched': 0, 'points': 0}
    rboard = list()
    for attack in attacks:
        rboard.append(board[-attack[1]][attack[0]-1])

    flat_board = list()
    for flat in board:
        flat_board.extend(flat)

    for i in range(1, max(flat_board) + 1):
        before = len(list(filter(lambda x: x == i, flat_board)))
        after = len(list(filter(lambda x: x == i, rboard)))
        if before == after:
            result['sunk'] += 1
        elif after == 0:
            result['not_touched'] += 1
        else:
            result['damaged'] += 1
    result['points'] = result['sunk'] * 1 + result['damaged'] * 0.5 + result['not_touched'] * -1
    return result


board = [[0, 0, 1, 0],
         [0, 0, 1, 0],
         [0, 0, 1, 0]]

attacks = [[3, 1], [3, 2], [3, 3]]
print(damaged_or_sunk(board, attacks))
