class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen, l, r = 0, 0, 0
        curLen, curL, curR = 0, 0, 0

        for i in range(len(s)):
            curLen, curL, curR = self.findMaxLenPali(s, i)
            if curLen > maxLen:
                maxLen = curLen
                l, r = curL, curR

        return s[l:r+1]

    def findMaxLenPali(self, s, i):
        n = len(s)

        j = i
        while j+1 < n and s[j] == s[j+1]:
            j += 1

        while True:
            i -= 1; j += 1
            if i < 0 or j >= n or s[i] != s[j]:
                break

        return j-i-1, i+1, j-1
