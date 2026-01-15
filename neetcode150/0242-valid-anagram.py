class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memo_table = [0] * 26
        for i in t:
            memo_table[ord(i) - ord('a')] += 1
        for i in s:
            memo_table[ord(i) - ord('a')] -= 1
        for val in memo_table:
            if val != 0:
                return False
        return True