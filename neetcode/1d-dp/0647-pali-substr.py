class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        for i in range(n):
            j = i
            while j+1 < n and s[j] == s[j+1]:
                j += 1
                count += 1

            left, right = i, j
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1

        return count
