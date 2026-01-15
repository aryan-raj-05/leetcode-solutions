class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i, j = 0, 0
        while i < len(nums):
            if nums[i] == val:
                i += 1
            else:
                nums[j] = nums[i]
                i += 1
                j += 1
        return j