# given a list of positive prices
# find the maximum profit that can be earned
# only one buy and one sale allowed
# sale happens after the buy
# keep track of the min price so far
# compute profit from difference of current price and min price
# keep track of max_profit at each iteration
# return the max profit

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(price, min_price)
        profit = price - min_price
        max_profit = max(profit, max_profit)

    return max_profit

# random prices
prices_1 = [7, 2, 5, 1, 3, 2, 6]
profit = max_profit(prices_1)
print(profit)

# increasing prices
prices_2 = [1, 2, 3, 4, 5]
profit = max_profit(prices_2)
print(profit)

# decreasing prices
prices_3 = [7, 5, 3, 2, 1]
profit = max_profit(prices_3)
print(profit)
