from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n

        for i in range(n):
            if i == 0: 
                left[i] = 1
            else:
                left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                right[i] = 1
            else:
                right[i] = right[i + 1] * nums[i + 1]

        for i in range(n):
            left[i] = left[i] * right[i]

        return left