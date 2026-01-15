# Given a string s, find the length of the longest without duplicate characters.

# Solutions
# 1. Brute Force: (TLE)
#       go through all combination of string and check for duplicates
# 2. Optimized brute force: (TLE)
#       start with substring of max length, gradually reducing size,
#       check for duplicates if none is found then that substring is the 
#       largest and further inspections are not needed
# 3. Sliding Window: (Accepted)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return self._sliding_window(s)

    def _sliding_window(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        table = set()

        while l <= r and r < len(s):
            if s[r] in table:
                table.remove(s[l])
                l += 1
            else:
                table.add(s[r])
                max_len = max(max_len, r - l + 1)
                r += 1

        return max_len

    def _bruteSolution(self, s: str) -> int:
        n = len(s)
        for size in range(n, 0, -1):
            for i in range(0, n - size + 1):
                upper_bound = i + size
                if not self._brute_contains_dupl(s[i:upper_bound]):
                    return size
        
        return 0

    def _brute_contains_dupl(self, s: str) -> bool:
        mem = set()
        for c in s:
            if c in mem:
                return True
            mem.add(c)
        return False
