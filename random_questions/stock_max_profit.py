def calculate_max_profit(prices):
    if len(prices) <= 1:
        return 0
    local_min_max = []
    total_profit = 0
    local_min = None
    local_max = None
    for idx, each_price in enumerate(prices):
        try:
            if prices[idx+1] <= each_price:
                continue
        except IndexError:
            continue
        if not local_min:
            local_min = each_price
        if each_price >= prices[idx-1]:
            continue
        buy_sell_pair = [local_min, prices[idx-1]]
        local_min_max.append(buy_sell_pair)
        local_min = None
    if local_min_max:
        for each_price in local_min_max:
            profit = each_price[1] -each_price[0]
            total_profit += profit
            print(f'Buy {each_price[0]}, Sell {each_price[1]}, Profit={profit}')
    return total_profit

import ipdb; ipdb.set_trace()
print(calculate_max_profit([20,30,30,40]))
#print(calculate_max_profit([90,100,90,100]))
#print(calculate_max_profit([130,110,100,115,90,100,75,85,65,70,85]))
