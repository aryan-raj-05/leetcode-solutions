class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        n = 1 -> 1
        n = 2 -> 2 (1 + 1, 2)
        n = 3 -> 3 (1+1+1, 1+2, 2+1)
        n = 4 -> 5 (1+1+1+1, 2 + 2, 2 + 1 + 1, 1 + 2 + 1, 1 + 1 + 2)
        '''
        if n < 3:
            return n
        
        a, b = 1, 2
        for i in range(3, n + 1):
            c = a + b
            a, b = b, c
        return b
