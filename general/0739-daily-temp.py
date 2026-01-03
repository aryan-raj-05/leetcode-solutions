from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        res = [0] * n

        for i in range(n):
            while st and temperatures[i] > temperatures[st[-1]]:
                idx = st.pop()
                res[idx] = i - idx
            st.append(i)
        
        return res

    def dailyTemperatures_brute(self, temperatures: List[int]) -> List[int]:
        # brute force
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            today_temp = temperatures[i]
            max_temp = -1

            for j in range(i + 1, n):
                if temperatures[j] > today_temp:
                    max_temp = j
                    break
            
            if max_temp == -1:
                res[i] = 0
            else:
                res[i] = max_temp - i
        
        return res