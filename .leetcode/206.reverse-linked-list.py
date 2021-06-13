# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (66.26%)
# Likes:    7289
# Dislikes: 138
# Total Accepted:    1.4M
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, reverse the list, and return the
# reversed list.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]
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
# Constraints:
#
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
#
#
#
# Follow up: A linked list can be reversed either iteratively or recursively.
# Could you implement both?
#
#

# @lc tags=linked-list

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 反转链表。
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
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        p = head
        pN = p.next
        p.next = None
        while pN:
            pNN = pN.next
            pN.next = p
            p = pN
            pN = pNN
        return p
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5]')
    print('Exception :')
    print('[5,4,3,2,1]')
    print('Output :')
    print(str(Solution().reverseList(listToListNode([1, 2, 3, 4, 5]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2]')
    print('Exception :')
    print('[2,1]')
    print('Output :')
    print(str(Solution().reverseList(listToListNode([1, 2]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().reverseList(listToListNode([]))))
    print()

    pass
# @lc main=end