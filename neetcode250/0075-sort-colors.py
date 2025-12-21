class Solution:
    # 1. Simple and Standard Sorting Algorithms: O(nlogn)
    # 2. Counting Sort: TC O(n)
    # 3. Dutch National Flag
    def sortColors(self, nums: list[int]) -> None:
        freq = [0] * 3
        for num in nums:
            freq[num] += 1
        
        k = 0
        for i in range(3):
            while freq[i] > 0:
                nums[k] = i
                k += 1
                freq[i] -= 1

    def sortColorsDNF(self, nums: list[int]) -> None:
        lo = mid = 0
        hi = len(nums) - 1
        while mid <= hi:
            if nums[mid] == 0:
                nums[mid], nums[lo] = nums[lo], nums[mid]
                mid += 1
                lo += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
