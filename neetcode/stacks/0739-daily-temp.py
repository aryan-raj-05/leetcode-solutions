from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        result = [0] * n
        stack = [temperatures[0]]
        pos = [0]
        for i in range(1, n):
            t = temperatures[i]
            if t <= stack[-1]:
                stack.append(t)
                pos.append(i)
            else:
                while stack and stack[-1] < t:
                    idx = pos[-1]
                    days = i - idx
                    result[idx] = days
                    stack.pop(); pos.pop()

            stack.append(t)
            pos.append(i)

        return result
