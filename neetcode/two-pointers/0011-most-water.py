from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            curArea = (r - l) * min(height[l], height[r])
            maxArea = max(maxArea, curArea)
            if height[l] <= height[r]: l += 1
            else: r -= 1

        return maxArea

    # Time Complexity: O(n^2)
    def brute(self, height: List[int]) -> int:
        maxArea = 0
        n = len(height)
        
        for i in range(n):
            for j in range(i + 1, n):
                h = min(height[i], height[j])
                w = j - i
                maxArea = max(maxArea, h * w)

        return maxArea
    
height = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(height))
