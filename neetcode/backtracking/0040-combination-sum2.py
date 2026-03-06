from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)

        def dfs(idx, total, path):
            if total == target:
                res.append(path.copy())
                return

            if (idx >= n) or (total > target):
                return

            path.append(candidates[idx])
            dfs(idx + 1, total + candidates[idx], path)

            path.pop()
            idx += 1
            while idx < n and candidates[idx - 1] == candidates[idx]:
                idx += 1
            dfs(idx, total, path)

        dfs(0, 0, [])
        return res