class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1Freq = [0] * 26
        windowFreq = [0] * 26

        for i in range(n1):
            s1Freq[ord(s1[i]) - ord('a')] += 1
            windowFreq[ord(s2[i]) - ord('a')] += 1

        i, j = 0, n1 - 1
        while j < n2:
            if s1Freq == windowFreq:
                return True

            i += 1; j += 1
            windowFreq[ord(s2[i - 1]) - ord('a')] -= 1
            if j < n2:
                windowFreq[ord(s2[j]) - ord('a')] += 1

        return False


    def same(self, s1, s2):
        n1, n2 = len(s1), len(s2)

        i, j = 0, n1 - 1
        str_match = sorted(s1)

        while j < n2:
            if str_match == sorted(s2[i:j+1]):
                return True
            i += 1
            j += 1

        return False
