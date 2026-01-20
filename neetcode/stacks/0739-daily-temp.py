from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        result = [0] * n
        pos_stack = [0]
        for i in range(1, n):
            t = temperatures[i]
            
            while pos_stack and temperatures[pos_stack[-1]] < t:
                result[pos_stack[-1]] = i - pos_stack[-1]
                pos_stack.pop()

            pos_stack.append(i)

        return result
