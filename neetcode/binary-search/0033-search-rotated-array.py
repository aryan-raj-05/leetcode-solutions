from typing import List

"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at 
an unknown index k (1 <= k < nums.length) such that the resulting array 
is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] 
(0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 
indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
 return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. find the min val, say m
        l = 0
        r = len(nums) - 1
        while nums[l] > nums[r]:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        # 2. set m as offset and, % len(nums) for circularity
        start = l
        def idx(n):
            return (n + start) % len(nums)

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            val = nums[idx(mid)]
            if val == target:
                return idx(mid)
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
