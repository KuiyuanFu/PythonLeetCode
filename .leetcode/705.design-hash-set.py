# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#
# https://leetcode.com/problems/design-hashset/description/
#
# algorithms
# Easy (63.93%)
# Likes:    961
# Dislikes: 133
# Total Accepted:    145.3K
# Total Submissions: 227.4K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +
# '[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# Design a HashSet without using any built-in hash table libraries.
#
# Implement MyHashSet class:
#
#
# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or
# not.
# void remove(key) Removes the value key in the HashSet. If key does not exist
# in the HashSet, do nothing.
#
#
#
# Example 1:
#
#
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains",
# "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]
#
# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
#
#
# Constraints:
#
#
# 0 <= key <= 10^6
# At most 10^4 calls will be made to add, remove, and contains.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 自定义hash。
# 模p。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class MyHashSet:
    def __init__(self):
        self.l = 9973
        self.i = 1049
        self.buffer = [None] * self.l

    def add(self, key: int) -> None:
        idx = key % self.l

        while self.buffer[idx] is not None:
            idx = (idx + self.i) % self.l
        self.buffer[idx] = [key, True]

    def remove(self, key: int) -> None:
        idx = key % self.l

        while self.buffer[idx] is not None:
            t = self.buffer[idx]
            if t[0] == key and t[1] == True:
                t[1] = False
            idx = (idx + self.i) % self.l

    def contains(self, key: int) -> bool:

        idx = key % self.l

        while self.buffer[idx] is not None:
            t = self.buffer[idx]
            if t[0] == key and t[1] == True:
                return True
            idx = (idx + self.i) % self.l
        return False


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    o = MyHashSet()
    print(o.add(9))
    print(o.remove(19))
    print(o.add(14))
    print(o.remove(19))
    print(o.remove(9))
    print(o.add(0))
    print(o.add(3))
    print(o.add(4))
    print(o.add(0))
    print(o.remove(9))
    pass
# @lc main=end