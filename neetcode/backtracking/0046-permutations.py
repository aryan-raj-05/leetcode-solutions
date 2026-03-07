from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def aux(idx):
            if idx == n:
                res.append(nums.copy())
                return

            for i in range(idx, n):
                nums[idx], nums[i] = nums[i], nums[idx]
                aux(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]

        aux(0)
        
        return res