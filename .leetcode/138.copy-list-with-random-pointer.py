# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (42.20%)
# Likes:    5294
# Dislikes: 826
# Total Accepted:    576K
# Total Submissions: 1.4M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# A linked list of length n is given such that each node contains an additional
# random pointer, which could point to any node in the list, or null.
#
# Construct a deep copy of the list. The deep copy should consist of exactly n
# brand new nodes, where each new node has its value set to the value of its
# corresponding original node. Both the next and random pointer of the new
# nodes should point to new nodes in the copied list such that the pointers in
# the original list and copied list represent the same list state. None of the
# pointers in the new list should point to nodes in the original list.
#
# For example, if there are two nodes X and Y in the original list, where
# X.random --> Y, then for the corresponding two nodes x and y in the copied
# list, x.random --> y.
#
# Return the head of the copied linked list.
#
# The linked list is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
#
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random
# pointer points to, or null if it does not point to any node.
#
#
# Your code will only be given the head of the original linked list.
#
#
# Example 1:
#
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
# Example 2:
#
#
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
#
#
# Example 3:
#
#
#
#
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
#
#
# Example 4:
#
#
# Input: head = []
# Output: []
# Explanation: The given linked list is empty (null pointer), so return
# null.
#
#
#
# Constraints:
#
#
# 0 <= n <= 1000
# -10000 <= Node.val <= 10000
# Node.random is null or is pointing to some node in the linked list.
#
#
#

# @lc tags=hash-table;linked-list

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定一个链表，每一个结点除了next指针，还包括一个random指针。
# random指针指向任意结点或None。
# 创建此链表的一个深拷贝。
# 要求不使用额外空间，那就必须要利用已有的空间。
# 但现在，只有一个链表，其没有所有空间的值都是有意义的，那么怎么做呢。
# 想到复制一个链表，那么副本与原件是一样的结构，所以可以把副本的结点连接在原件结点后，这样保持了结构不变，并根据原件的random指针，来确定副本中random指针应该指向的位置。
#
#
# @lc idea=end

# @lc group=linked-list

# @lc rank=10

# @lc code=start


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        p = head
        while p:
            new = Node(p.val, next=p.next)
            p.next = new
            p = p.next.next

        dupl = None if not head else head.next
        p = head
        while p:
            # next p node
            pNext = p.next.next
            # the duplication node's random point to p's random corresponding duplication node.
            if p.random:
                p.next.random = p.random.next
            # the duplication node's next point to pNext's next.
            # there is the new next node.
            p.next.next = pNext.next if pNext else None
            p = pNext
        return dupl
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    pass
# @lc main=end