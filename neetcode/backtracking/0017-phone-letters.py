from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        myDict = {}
        start = 97

        for i in range(2, 10):
            if i == 7 or i == 9:
                myDict[str(i)] = [
                    chr(start), chr(start + 1), chr(start + 2), chr(start + 3)
                ]
                start += 4
            else:
                myDict[str(i)] = [chr(start), chr(start + 1), chr(start + 2)]
                start += 3

        res = []
        for digit in digits:
            chars = myDict[digit]

            if len(res) == 0:
                for c in chars: res.append(c)
            else:
                new_res = []
                for r in res:
                    for c in chars:
                        new_res.append(r + c)
                res = new_res

        return res
