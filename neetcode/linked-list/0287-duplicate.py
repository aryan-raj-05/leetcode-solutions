from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyd's algorithms
        # 1. find x where slow == fast
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # 2. start with new pointer h and move h and slow until they meet
        h = 0
        while True:
            if h == slow:
                break
            h = nums[h]
            slow = nums[slow]

        return h
        