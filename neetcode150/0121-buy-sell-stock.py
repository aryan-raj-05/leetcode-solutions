from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10000
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            cur_profit = price - min_price
            max_profit = max(max_profit, cur_profit)

        return max_profit
