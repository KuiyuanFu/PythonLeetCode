# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#
# https://leetcode.com/problems/map-sum-pairs/description/
#
# algorithms
# Medium (56.93%)
# Likes:    1026
# Dislikes: 114
# Total Accepted:    77.1K
# Total Submissions: 135.6K
# Testcase Example:  '["MapSum","insert","sum","insert","sum"]\n' +
# '[[],["apple",3],["ap"],["app",2],["ap"]]'
#
# Design a map that allows you to do the following:
#
#
# Maps a string key to a given value.
# Returns the sum of the values that have a key with a prefix equal to a given
# string.
#
#
# Implement the MapSum class:
#
#
# MapSum() Initializes the MapSum object.
# void insert(String key, int val) Inserts the key-val pair into the map. If
# the key already existed, the original key-value pair will be overridden to
# the new one.
# int sum(string prefix) Returns the sum of all the pairs' value whose key
# starts with the prefix.
#
#
#
# Example 1:
#
#
# Input
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# Output
# [null, null, 3, null, 5]
#
# Explanation
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);
# mapSum.sum("ap");           // return 3 (apple = 3)
# mapSum.insert("app", 2);
# mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
#
#
#
# Constraints:
#
#
# 1 <= key.length, prefix.length <= 50
# key and prefix consist of only lowercase English letters.
# 1 <= val <= 1000
# At most 50 calls will be made to insert and sum.
#
#
#

# @lc tags=trie

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 创建数据结构，保存字符串与值的对应关系。给定前缀，求所有满足前缀的字符串的值的和。
# 前缀树。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Node:
    def __init__(self, c='', v=0) -> None:
        self.ps = {}
        self.c = c
        self.v = v
        self.f = False


def insert(root: Node, key: str, val: int):
    p = root
    for c in key:
        if c not in p.ps:
            p.ps[c] = Node(c=c)
        p = p.ps[c]
        p.v += val
    v = 0
    if p.f:
        v = p.v - val - sum([p.ps[pk].v for pk in p.ps.keys()])
    p.f = True
    return v


def search(root: Node, key: str):
    p = root
    for c in key:
        if c not in p.ps:
            p.ps[c] = Node(c=c)
        p = p.ps[c]
    return p.v


class MapSum:
    def __init__(self):
        self.root = Node()

    def insert(self, key: str, val: int) -> None:
        v = insert(self.root, key, val)
        if v > 0:
            insert(self.root, key, -v)

    def sum(self, prefix: str) -> int:
        return search(self.root, prefix)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__()))
    print()

    pass
# @lc main=end