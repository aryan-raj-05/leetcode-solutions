from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if i > 0 and  nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1
            while j < k:
                total_sum = nums[j] + nums[k] + nums[i]

                if total_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif total_sum < 0:
                    j += 1
                else:
                    k -= 1

        return res
