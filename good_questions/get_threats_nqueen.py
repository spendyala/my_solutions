
def horizontal_validation(x, y, a, n_queen):
    counter = 0
    for i in range(len(a)):
        if n_queen.get((i+1, y)) and (i+1, y) != (x, y):
            counter += 1
    return 2 if counter >= 2 else counter


def vertical_validation(x, y, a, n_queen):
    counter = 0
    for i in range(len(a)):
        if n_queen.get((x, i+1)) and (x, i+1) != (x, y):
            counter += 1
    return 2 if counter >= 2 else counter


def diagonal_validation(x, y, a, n_queen):
    counter = 0
    # import pdb; pdb.set_trace()
    for i in range(1-max(x, y), len(a)+1):
        print(x, y, x+i, y+i)
        if n_queen.get((x+i, y+i)) and (x+i, y+i) != (x, y):
            counter += 1
    counter = 2 if counter >= 2 else counter
    for i in range(1-min(x, y), len(a)+1):
        print(x, y, x-i, y+i)
        if n_queen.get((x-i, y+i)) and (x-i, y+i) != (x, y):
            counter += 1
    return 4 if counter >= 4 else counter


def maxThreats(a):
    len_a = len(a)
    threat_count = [0] * len_a
    index = 1
    n_queen = {}
    for each in a:
        n_queen[(index, each)] = True
        index += 1
    index = 1
    for each in a:
        threat_count[index-1] += horizontal_validation(index, each, a, n_queen)
        threat_count[index-1] += vertical_validation(index, each, a, n_queen)
        threat_count[index-1] += diagonal_validation(index, each, a, n_queen)
        index += 1
    return max(threat_count)


maxThreats([4, 5, 1, 3, 7, 8, 2, 6])
