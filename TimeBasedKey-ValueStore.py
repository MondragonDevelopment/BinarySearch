"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
"""
class TimeMap:
    def __init__(self):
        self.dic = {}
        return None

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic.keys(): 
            self.dic[key] = []
        self.dic[key].append([timestamp, value])
        return None
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic.keys(): return ""
        #print(self.dic[key])
        l, r = 0, len(self.dic[key]) - 1
        if self.dic[key][l][0] > timestamp: return ""
        else:
            while l<=r:
                m = (l+r)//2
                if timestamp == self.dic[key][m][0]: return self.dic[key][m][1]
                elif timestamp < self.dic[key][m][0]: r = m - 1
                else: l = m + 1
            return self.dic[key][r][1]
        
"""
Faster get function:

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.dic.get(key, [])     # dictionary.get(key, value) where value is optional. A value to return if the specified key does not exist. Default value None
        l, r = 0, len(values) - 1                   # If dic[key] == [] then r = -1 so it returns
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
"""


tm = TimeMap()

print(tm.set("foo", "bar", 1))
print(tm.get("foo", 1))
print(tm.get("foo", 3))
print(tm.set("foo", "bar2", 4))
print(tm.get("foo", 4))
print(tm.get("foo", 5))
