# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (36.78%)
# Likes:    8648
# Dislikes: 354
# Total Accepted:    774.8K
# Total Submissions: 2.1M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
#  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
#
# Implement the LRUCache class:
#
#
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
#
#
# Follow up:
# Could you do get and put in O(1) time complexity?
#
#
# Example 1:
#
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#
#
#
# Constraints:
#
#
# 1 <= capacity <= 3000
# 0 <= key <= 3000
# 0 <= value <= 10^4
# At most 3 * 10^4 calls will be made to get and put.
#
#
#

# @lc tags=design

# @lc imports=start
from tkinter.messagebox import NO
from imports import *
# @lc imports=end

# @lc idea=start
#
# 实现一个LRU cache，就是保留最近使用的块。
# 使用字典加双向链表。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Node:
    def __init__(self, key=0, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        self.key = key

    def removeSelf(self):
        if self.left:
            self.left.right = self.right
        if self.right:
            self.right.left = self.left

    def insertLeft(self, node):
        if node.right == self:
            return
        self.removeSelf()
        if node.right:
            node.right.left = self
        self.right = node.right
        node.right = self
        self.left = node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.pseudoHead = Node()
        self.pseudoTail = Node()
        self.pseudoHead.right = self.pseudoTail
        self.pseudoTail.left = self.pseudoHead
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            node.insertLeft(self.pseudoHead)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key].val = value
            self.dict[key].insertLeft(self.pseudoHead)
            return

        node = Node(key, value)
        self.dict[key] = node

        if self.capacity == self.count:
            self.dict.pop(self.pseudoTail.left.key)
            self.pseudoTail.left.removeSelf()
        else:
            self.count += 1
        node.insertLeft(self.pseudoHead)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    lru = LRUCache(2)
    r = lru.put(1, 0)
    print(r)
    r = lru.put(2, 2)
    print(r)
    r = lru.get(1)
    print(r)
    r = lru.put(3, 3)
    print(r)
    r = lru.get(2)
    print(r)
    r = lru.put(4, 4)
    print(r)
    r = lru.get(1)
    print(r)
    r = lru.get(3)
    print(r)
    r = lru.get(4)
    print(r)
    pass
# @lc main=end