class Solution:
    def hammingWeight2(self, n: int) -> int:
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count
