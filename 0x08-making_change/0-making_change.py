#!/usr/bin/python3
""" 0x08-making_change """


def makeChange(coins, total):
    """
    Prototype: def makeChange(coins, total)
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    sum = 0
    m = 0
    counter = 0
    num_coins = len(coins)
    while sum < total and m < num_coins:
        while coins[m] <= total - sum:
            sum += coins[m]
            counter += 1
            if sum == total:
                return counter
        m += 1
    return -1
