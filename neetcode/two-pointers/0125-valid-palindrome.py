class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        n = len(s)
        while l < r:
            while not self.is_alpha(s[l]):
                l += 1
                if l >= n: return False
            while not self.is_alpha(s[r]): 
                r -= 1
                if r < 0: return False
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def is_alpha(self, s: str) -> bool:
        return ord(s.lower()) in range(97, 123) or ord(s) in range(48, 58)

s = "0P"
sol = Solution()

print(sol.isPalindrome(s))