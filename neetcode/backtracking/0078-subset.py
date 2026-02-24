from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def recurse(i, arr):
            if i == n:
                ans.append(arr.copy())
                return

            arr.append(nums[i])
            recurse(i + 1, arr)

            arr.pop()
            recurse(i + 1, arr)

        recurse(0, [])
        return ans
