#!/usr/bin/python3
"""Module on making change.
"""


def makeChange(coins, total):
    """ Function that determines fewest number of coins needed
    to meet a given amount total when given a pile of coins of
    different values.
    """
    if total <= 0:
        return 0
    change = total
    coin_count = 0
    coin_id = 0
    sorted_coins = sorted(coins, reverse=True)
    l = len(coins)
    
    while change > 0:
        if coin_id >= l:
            return -1
        if change - sorted_coins[coin_id] >= 0:
            change -= sorted_coins[coin_id]
            coin_count += 1
        else:
            coin_id += 1
    return coin_count