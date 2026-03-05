from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(idx, total, path: List[int]):
            if total == target:
                result.append(path.copy())
                return

            if idx >= len(candidates) or total > target:
                return

            path.append(candidates[idx])
            dfs(idx, total + candidates[idx], path)
            path.pop()
            dfs(idx + 1, total, path)

        dfs(0, 0, [])
        return result
