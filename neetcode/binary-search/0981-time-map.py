"""
Design a time-based key-value data structure that can store multiple
values for the same key at different time stamps and retrieve the key's
value at a certain timestamp.

Implement the TimeMap class:

- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores
the key key with the value value at the given time timestamp.
- String get(String key, int timestamp) Returns a value 
such that set was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the value associated
with the largest timestamp_prev. If there are no values, it returns "".

Constraints:
- 1 <= key.length, value.length <= 100
- key and value consist of lowercase English letters and digits.
- 1 <= timestamp <= 10^7
- All the timestamps "timestamp" of "set" are strictly increasing.
- At most 2 * 10^5 calls will be made to set and get.

"""

class TimeMap:
    def __init__(self):
        self.myDict: dict[str, list[tuple[str, int]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.myDict.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.myDict:
            return ""
            
        arr = self.myDict[key]

        l = 0
        r = len(arr) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][1] <= timestamp:
                result = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)