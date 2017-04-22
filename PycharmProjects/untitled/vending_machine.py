coins = [1, .50, .20, .10, .05, .02, .01]


def give_change(amount):
    change = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)
    return change