class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for i in range(2,len(cost)):
            cost[i] = (min(cost[i - 1], cost[i - 2]) + cost[i])
        return min(cost[-1], cost[-2])