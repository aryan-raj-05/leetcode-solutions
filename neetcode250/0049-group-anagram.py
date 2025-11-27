class Solution:
    # optimization:
    # sort the string and place it in a dict<sorted_string, index_in_result>
    # Time Complexity: O(n * k log k)   // k = max len of strings, n = number of strings
    # Space Complexity: O(nk)
    def groupAnagrams_opt(self, strs: list[str]) -> list[list[str]]:
        store = {}
        result = []
        for word in strs:
            sorted_str = ''.join(sorted(word))
            if sorted_str in store:
                result[store[sorted_str]].append(word)
                continue
            store[sorted_str] = len(result)
            result.append([word])
        return result

    # Time Complexity: O(n^2 * k)
    # Time Limit Exceeded
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        n = len(strs)
        seen = [False] * n
        result = []

        for i in range(n):
            if seen[i]: continue
            word = strs[i]
            seen[i] = True
            res = [word]
            for j in range(n):
                if not seen[j] and self.isAnagram(word, strs[j]):
                    res.append(strs[j])
                    seen[j] = True
            result.append(res)

        return result

    def isAnagram(self, s: str, t: str) -> bool:
        table = [0] * 26
        for c in s: table[ord(c) - ord('a')] += 1
        for c in t: table[ord(c) - ord('a')] -= 1
        for val in table:
            if val != 0:
                return False
        return True