from typing import List

'''
- Sorting a Map: O(nlogn)
    put all occurances of items in a map then sort it and return the first k values
- Heap: O(k log n)
    1. put all occurances of items in a map
    2. store all the pairs in a heap with the freq as the value
    3. pop k times from heap
- Buckets: O(n)
    1. put all occurances of items in a map
    2. create a occurances to list of elements array
    3. starting from the end put elements into result until the length is k
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return []
