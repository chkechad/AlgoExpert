# Non-Constructible Change
# Difficulty: 🟢 Category: Arrays Successful Submissions: 70,822+
# Given an array of positive integers representing the values of coins in your possession,
# write a function that returns the minimum amount of change (the minimum sum of money) that you cannot create.
# The given coins can have any positive integer value and aren't necessarily unique
# (i.e., you can have multiple coins of the same value).
# For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4.
# If you're given no coins, the minimum amount of change that you can't create is 1.
# Sample Input


def nonConstructibleChange(coins):
    coins_sort = sorted(coins)
    change = 0
    for c in coins_sort:
        if c > change + 1:
            return change + 1
        else:
            change += c
    return change + 1


if __name__ == "__main__":
    coins = [5, 7, 1, 1, 2, 3, 22]

    assert nonConstructibleChange(coins) == 20
