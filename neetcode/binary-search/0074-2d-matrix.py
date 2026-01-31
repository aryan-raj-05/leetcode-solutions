from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin_search(row: int) -> bool:
            l, r = 0, len(matrix[row]) - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False

        if len(matrix) == 1:
            return bin_search(0)
        
        top, down = 0, len(matrix) - 1
        while top <= down:
            mid = (top + down) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                return bin_search(mid)
            elif matrix[mid][0] > target:
                down = mid - 1
            else:
                top = mid + 1
        return False
    

matrix = [[1],[3]]
target = 8
sol = Solution()
print(sol.searchMatrix(matrix, target))