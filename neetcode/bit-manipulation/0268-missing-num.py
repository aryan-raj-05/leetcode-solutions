from typing import List

class Solution:
    def missingNumber_bit(self, nums: List[int]) -> int:
        # xor of a number with itself is zero
        # (0 ^ 1 ^ 2 ^ 3) ^ (3 ^ 0 ^ 1)
        # (1 ^ 1) ^ (3 ^ 3) ^ 2
        # 0 ^ 0 ^ 2 = 2
        n = len(nums)

        xor_sum = 0
        for i in range(n + 1):
            xor_sum ^= i
        
        nums_xor_sum = 0
        for num in nums:
            nums_xor_sum ^= num

        return xor_sum ^ nums_xor_sum

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n + 1)) // 2
        for num in nums:
            total -= num
        return total
