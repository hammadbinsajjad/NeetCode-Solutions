import math
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = 0
        r = 1
        max_profit = -math.inf

        while l < len(prices) and r < len(prices):
            if prices[r] - prices[l] < 0:
                l += 1
                
                if l == r:
                    r += 1
            else:
                cur_profit = prices[r] - prices[l]
                max_profit = max(cur_profit, max_profit)

                r += 1

        return max(max_profit, 0)