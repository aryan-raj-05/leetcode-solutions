'''
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time
complexity and with the smallest space complexity possible.
'''
# Since, the question requires smallest space complexity,
# 1. QuickSort : TLE
# 2. HeapSort : accepted
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.sift_down(nums, n, i)

        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.sift_down(nums, i, 0)
        return nums

    def sift_down(self, nums: list[int], n: int, start: int) -> None:
        i = start

        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and nums[left] > nums[largest]:
                largest = left
            
            if right < n and nums[right] > nums[largest]:
                largest = right

            if largest == i:
                break
            
            nums[i], nums[largest] = nums[largest], nums[i]
            i = largest
            