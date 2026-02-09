class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = -x if x < 0 else x
        limit = 2**31 // 10

        rev = 0
        while x > 0:
            units = x % 10
            if rev > limit or (rev == limit and units >= 8):
                return 0
            
            rev = rev * 10 + units
            x //= 10

        return sign * rev
