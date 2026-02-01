from typing import List

class Solution:
    # naive solution
    # time complexity = O(n log n)
    # optimized solution uses dp for linear time complexity
    def countBits(self, n: int) -> List[int]:
        def setBits(k):
            count = 0
            while k != 0:
                k = k & (k - 1)
                count += 1
            return count
        
        res = []
        for i in range(n + 1):
            res.append(setBits(i))
        return res

n = 24
sol = Solution()
print(sol.countBits(n))