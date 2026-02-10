class Solution:
    def characterReplacement2(self, s: str, k: int) -> int:
        count = {}
        i = max_len = most_freq = 0

        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            most_freq = max(most_freq, count[s[j]])

            while (j - i + 1) - most_freq > k:
                count[s[i]] -= 1
                i += 1
            max_len = max(max_len, j - i + 1)

        return max_len

    def characterReplacement(self, s: str, k: int) -> int:
        i = j = max_len = 0
        myDict = {s[i]: 1}
        while i <= j and j < len(s):
            most_freq = 0
            for value in myDict.values():
                most_freq = max(most_freq, value)
            d = 0 if i == j else (j - i + 1) - most_freq

            if d > k:
                key = s[i]
                myDict[key] = myDict.get(key, 0) - 1
                if myDict[key] <= 0:
                    myDict.pop(key, None)
                i += 1
                continue

            max_len = max(max_len, j - i + 1)
            j += 1
            if j < len(s):
                myDict[s[j]] = myDict.get(s[j], 0) + 1

        return max_len
