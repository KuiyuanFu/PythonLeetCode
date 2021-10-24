# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#
# https://leetcode.com/problems/design-hashmap/description/
#
# algorithms
# Easy (63.86%)
# Likes:    1980
# Dislikes: 217
# Total Accepted:    227.9K
# Total Submissions: 357.2K
# Testcase Example:  '["MyHashMap","put","put","get","get","put","get","remove","get"]\n' +
# '[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# Design a HashMap without using any built-in hash table libraries.
#
# Implement the MyHashMap class:
#
#
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If
# the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or
# -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map
# contains the mapping for the key.
#
#
#
# Example 1:
#
#
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]
#
# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1],
# [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the
# existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now
# [[1,1]]
#
#
#
# Constraints:
#
#
# 0 <= key, value <= 10^6
# At most 10^4 calls will be made to put, get, and remove.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 自定义hash
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class MyHashMap:
    def __init__(self):
        self.l = 100000
        self.i = 1049
        self.buffer = [None] * self.l

    def put(self, key: int, value: int) -> None:
        idx = key % self.l

        while self.buffer[idx] is not None and self.buffer[idx][0] != key:
            idx = (idx + (key + 1) * self.i) % self.l
        self.buffer[idx] = [key, True, value]

    def remove(self, key: int) -> None:
        idx = key % self.l

        while self.buffer[idx] is not None:
            t = self.buffer[idx]
            if t[0] == key:
                t[1] = False
                break
            idx = (idx + (key + 1) * self.i) % self.l

    def get(self, key: int) -> bool:

        idx = key % self.l

        while self.buffer[idx] is not None:
            t = self.buffer[idx]
            if t[0] == key:
                if t[1]:
                    return t[2]
                else:
                    return -1
            idx = (idx + (key + 1) * self.i) % self.l
        return -1


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    pass
# @lc main=end