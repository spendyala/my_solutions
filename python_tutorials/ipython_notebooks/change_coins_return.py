def change_coins_return(n, coins_available, coins_so_far):
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif not coins_available:
        pass
    else:
        for each in change_coins_return(n, coins_available[:], coins_so_far+[coins_available[0]]):
            yield each
        for each in change_coins_return(n, coins_available[1:], coins_so_far):
            yield each


n = 5
coins = [1, 2, 3, 5]

for each_coin in change_coins_return(n, coins, []):
    print(each_coin)
