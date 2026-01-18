from typing import List

'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        max_len = 0
        for n in unique_nums:
            if n - 1 not in unique_nums:
                cur_len = 1
                val = n + 1

                while val in unique_nums:
                    val += 1
                    cur_len += 1

                max_len = max(cur_len, max_len)
                
        return max_len

    def brute_force(self, nums: List[int]) -> int: # got accepted ????
        sorted_nums = sorted(list(set(nums)))

        i, j = 0, 0
        size = 1
        while j < len(sorted_nums) - 1:
            if sorted_nums[j + 1] == sorted_nums[j] + 1:
                j += 1
                cur_size = j - i + 1
                size = max(size, cur_size)
            else:
                j += 1
                i = j

        return size
