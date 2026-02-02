from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeToEat(rate):
            time = 0
            for pile in piles:
                time += (pile + rate - 1) // rate
            return time

        rate_max, rate_min = max(piles), 1
        result = rate_max

        while rate_max >= rate_min:
            mid = (rate_max + rate_min) // 2
            time = timeToEat(mid)

            if time <= h:
                result = mid
                rate_max = mid - 1
            else:
                rate_min = mid + 1

        return result
