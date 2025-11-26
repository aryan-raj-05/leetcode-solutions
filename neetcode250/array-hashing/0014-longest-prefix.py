class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common = strs[0]
        index_upto_match = 10**20

        for s in strs:
            index_upto_match = min(self.matchPrefix(common, s), index_upto_match)

        return common[0:index_upto_match]

    def matchPrefix(self, str1: str, str2: str) -> int:
        i = 0
        while i < min(len(str1), len(str2)):
            if str1[i] != str2[i]:
                return i
            i += 1
        return i
