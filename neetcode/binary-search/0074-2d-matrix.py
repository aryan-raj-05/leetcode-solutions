from typing import List

class Solution:
    # Approach 2:
    #     Treating the matrix as a flattened sorted array and performing binary search
    #     A value converts to 2D (row, col) as:
    #     row = idx // n, col = idx % n
    #     initial bounds are: l = 0, r = m * n - 1,
    #     where m = rows, n = col
    # Time Complexity: O(log(m.n))
    def searchMatrix_flat(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            val = matrix[row][col]

            if val == target:
                return True
            elif val > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


    # Approach 1:
    # Nested binary search
    # Time Complexity: O(log(m.n))
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
