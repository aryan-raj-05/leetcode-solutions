from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def dfs(i, aux: List[int]):
            if i == n:
                res.append(aux.copy())
                return
            
            aux.append(nums[i])
            dfs(i + 1, aux)

            aux.pop()
            j = i + 1
            while nums[j] == nums[i]:
                j += 1
            dfs(j, aux)

        dfs(0, [])
        return res
