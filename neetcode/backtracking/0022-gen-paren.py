from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(op, cl):
            if len(path) == 2*n:
                res.append(''.join(path))
                return

            if op < n:
                path.append('(')
                backtrack(op + 1, cl)
                path.pop()

            if cl < op:
                path.append(')')
                backtrack(op, cl + 1)
                path.pop()

        backtrack(0, 0)
        return res
