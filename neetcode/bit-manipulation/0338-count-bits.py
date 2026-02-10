from typing import List

class Solution:
    def countBits2(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        res = [0, 1]
        j = 1
        for i in range(2, n + 1):
            if (i & (i - 1)) == 0:
                res.append(1)
                j = 1
                continue

            res.append(1 + res[j])
            j += 1

        return res


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
