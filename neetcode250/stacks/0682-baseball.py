from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            match op:
                case "+":
                    new_score = stack[-1] + stack[-2]
                    stack.append(new_score)
                case "D":
                    new_score = 2 * stack[-1]
                    stack.append(new_score)
                case "C":
                    stack.pop()
                case _:
                    stack.append(int(op))

        return sum(stack)
