class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        freq = {}
        for i in range(len(nums)):
            look_for = target - nums[i]

            if look_for in freq:
                return [i, freq[look_for]]
            
            freq[nums[i]] = i
            
        return []