# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (44.84%)
# Likes:    2229
# Dislikes: 400
# Total Accepted:    275K
# Total Submissions: 612.7K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
#
# Example 1:
#
#
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
#
#
# Example 2:
#
#
# Input: head = [2,1], x = 2
# Output: [1,2]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
#
#
#

# @lc tags=linked-list;two-pointers

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个链表，指定一个值，保持顺序情况下，使所有小于其的节点在大于等于其的节点的左侧。
# 一次遍历，两个指针。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pseudoLess = ListNode()
        pseudoGreater = ListNode()
        less = pseudoLess
        greater = pseudoGreater

        p = head
        while p:
            if p.val < x:
                less.next = p
                less = p
            else:
                greater.next = p
                greater = p
            p = p.next
        less.next = pseudoGreater.next
        greater.next = None
        return pseudoLess.next

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,4,3,2,5,2], x = 3')
    print('Output :')
    print(str(Solution().partition(listToListNode([1, 4, 3, 2, 5, 2]), 3)))
    print('Exception :')
    print('[1,2,2,4,3,5]')
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [2,1], x = 2')
    print('Output :')
    print(str(Solution().partition(listToListNode([2, 1]), 2)))
    print('Exception :')
    print('[1,2]')
    print()

    pass
# @lc main=end