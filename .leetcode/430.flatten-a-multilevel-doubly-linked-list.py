# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/
#
# algorithms
# Medium (57.49%)
# Likes:    2618
# Dislikes: 203
# Total Accepted:    176.2K
# Total Submissions: 306.4K
# Testcase Example:  '[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]'
#
# You are given a doubly linked list which in addition to the next and previous
# pointers, it could have a child pointer, which may or may not point to a
# separate doubly linked list. These child lists may have one or more children
# of their own, and so on, to produce a multilevel data structure, as shown in
# the example below.
#
# Flatten the list so that all the nodes appear in a single-level, doubly
# linked list. You are given the head of the first level of the list.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]
# Explanation:
#
# The multilevel linked list in the input is as follows:
#
#
#
# After flattening the multilevel linked list it becomes:
#
#
#
#
# Example 2:
#
#
# Input: head = [1,2,null,3]
# Output: [1,3,2]
# Explanation:
#
# The input multilevel linked list is as follows:
#
# ⁠ 1---2---NULL
# ⁠ |
# ⁠ 3---NULL
#
#
# Example 3:
#
#
# Input: head = []
# Output: []
#
#
#
#
# How multilevel linked list is represented in test case:
#
# We use the multilevel linked list from Example 1 above:
#
#
# ⁠1---2---3---4---5---6--NULL
# ⁠        |
# ⁠        7---8---9---10--NULL
# ⁠            |
# ⁠            11--12--NULL
#
# The serialization of each level is as follows:
#
#
# [1,2,3,4,5,6,null]
# [7,8,9,10,null]
# [11,12,null]
#
#
# To serialize all levels together we will add nulls in each level to signify
# no node connects to the upper node of the previous level. The serialization
# becomes:
#
#
# [1,2,3,4,5,6,null]
# [null,null,7,8,9,10,null]
# [null,11,12,null]
#
#
# Merging the serialization of each level and removing trailing nulls we
# obtain:
#
#
# [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
#
#
# Constraints:
#
#
# The number of Nodes will not exceed 1000.
# 1 <= Node.val <= 10^5
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 抚平一个多层双向链表。
# 栈。
#
# @lc idea=end

# @lc group=


# @lc rank=
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        s = [head] if head else []
        prev = None
        while s:
            p = s.pop()
            p.prev = prev
            if prev:
                prev.next = p
            if p.next:
                s.append(p.next)
            if p.child:
                s.append(p.child)
                p.child = None
            prev = p
        return head


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]')
    print('Exception :')
    print('[1,2,3,7,8,11,12,9,10,4,5,6]')
    print('Output :')
    print(str(Solution().__init__(error, error, error, error)))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2,null,3]')
    print('Exception :')
    print('[1,3,2]')
    print('Output :')
    print(str(Solution().__init__(error, error, error, error)))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = []')
    print('Exception :')
    print(
        '[]How multilevel linked list is represented in test case:We use the multilevel linked list from Example 1 above:⁠1---2---3---4---5---6--NULL⁠        |⁠        7---8---9---10--NULL⁠            |⁠            11--12--NULLThe serialization of each level is as follows:[1,2,3,4,5,6,null][7,8,9,10,null][11,12,null]To serialize all levels together we will add nulls in each level to signifyno node connects to the upper node of the previous level. The serializationbecomes:[1,2,3,4,5,6,null][null,null,7,8,9,10,null][null,11,12,null]Merging the serialization of each level and removing trailing nulls weobtain:[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]'
    )
    print('Output :')
    print(str(Solution().__init__(error, error, error, error)))
    print()

    pass
# @lc main=end