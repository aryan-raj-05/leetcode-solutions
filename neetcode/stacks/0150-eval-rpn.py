from typing import List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
                case "-":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                case "*":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)
                case "/":
                    b = stack.pop()
                    a = stack.pop()
                    sign = -1 if (a * b) < 0 else 1
                    res = abs(a) // abs(b)
                    stack.append(sign * res)
                case _:
                    stack.append(int(token))

        return stack[0]
