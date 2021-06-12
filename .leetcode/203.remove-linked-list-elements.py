# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (39.85%)
# Likes:    2830
# Dislikes: 128
# Total Accepted:    481.7K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Given the head of a linked list and an integer val, remove all the nodes of
# the linked list that has Node.val == val, and return the new head.
#
#
# Example 1:
#
#
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
#
#
# Example 2:
#
#
# Input: head = [], val = 1
# Output: []
#
#
# Example 3:
#
#
# Input: head = [7,7,7,7], val = 7
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 10^4].
# 1 <= Node.val <= 50
# 0 <= val <= 50
#
#
#

# @lc tags=linked-list

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个链表，删除特定元素结点。
# 直接遍历。
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pseudo = ListNode(next=head)
        p = pseudo
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return pseudo.next


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,6,3,4,5,6], val = 6')
    print('Exception :')
    print('[1,2,3,4,5]')
    print('Output :')
    print(
        str(Solution().removeElements(listToListNode([1, 2, 6, 3, 4, 5, 6]),
                                      6)))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [], val = 1')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().removeElements(listToListNode([]), 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = [7,7,7,7], val = 7')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().removeElements(listToListNode([7, 7, 7, 7]), 7)))
    print()

    pass
# @lc main=end