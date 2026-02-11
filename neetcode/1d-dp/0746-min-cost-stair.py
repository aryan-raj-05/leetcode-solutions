from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * 2
        for i in range(2, len(cost)):
            cost1 = dp[0] + cost[i - 2]
            cost2 = dp[1] + cost[i - 1]

            dp[0] = dp[1]
            dp[1] = min(cost1, cost2)

        return min(dp[0] + cost[-2], dp[1] + cost[-1])
