"""You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7."""


## Note unlike single transaction, here you can make multiple transactions to maximiza profit
# you do not need to track global minimum and maximum b'coz any time price goes up from one day to the next, 
# hat increase can be added as profit
# Approach - loop over the array, compare next > prev, add the profit
# TC: O(n)
# SC: O(1)

def maxProfit(prices: list[int]) -> int:
    max_profit = 0
    
    for i in range(1, len(prices)): #[7,1,5,3,6,4],[7,1,5,7,6,4]
        if prices[i] > prices[i-1]:
            max_profit += (prices[i] - prices[i-1])
    
    return max_profit

prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
# prices = [7]
print(maxProfit(prices))