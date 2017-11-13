def change(n, coins_available, coins_so_far):
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif not coins_available:
        pass
    else:
        for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
            yield c
        for c in change(n, coins_available[1:], coins_so_far):
            yield c

import ipdb; ipdb.set_trace()
n = 5
coins = [1, 2, 3, 5]

solutions = [s for s in change(n, coins, [])]
for s in solutions:
    print(s)
