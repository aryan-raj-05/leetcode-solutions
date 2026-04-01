class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        i2, i1 = 0, 0
        for i in range(1, n):
            cur = max(nums[i] + i2, i1)
            i2, i1 = i1, cur
        
        j2, j1 = 0, 0
        for j in range(0, n - 1):
            cur = max(nums[j] + j2, j1)
            j2, j1 = j1, cur

        return max(i1, j1)
