class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_table = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        for paren in s:
            if paren in ['(', '{', '[']:
                stack.append(paren)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == paren_table[paren]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
