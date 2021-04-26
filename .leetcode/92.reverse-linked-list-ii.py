# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (40.85%)
# Likes:    3565
# Dislikes: 185
# Total Accepted:    346.2K
# Total Submissions: 846.5K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Given the head of a singly linked list and two integers left and right where
# left <= right, reverse the nodes of the list from position left to position
# right, and return the reversed list.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#
#
# Example 2:
#
#
# Input: head = [5], left = 1, right = 1
# Output: [5]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
#
#
# Follow up: Could you do it in one pass?
#

# @lc tags=linked-list

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个链表，再给定左右边界，反转范围内的节点。
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
    def reverseBetween(self, head: ListNode, left: int,
                       right: int) -> ListNode:
        if left == right:
            return head
        pesudo = ListNode(next=head)
        p = pesudo
        for _ in range(left - 1):
            p = p.next
        pNext = p.next

        l = p.next
        r = l.next
        for _ in range(right - left):
            rNext = r.next
            r.next = l
            l, r = r, rNext
            
        p.next = l
        pNext.next = r

        return pesudo.next
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5], left = 2, right = 4')
    print('Output :')
    print(str(Solution().reverseBetween(listToListNode([1, 2, 3, 4, 5]), 2,
                                        4)))
    print('Exception :')
    print('[1,4,3,2,5]')
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [5], left = 1, right = 1')
    print('Output :')
    print(str(Solution().reverseBetween(listToListNode([5]), 1, 1)))
    print('Exception :')
    print('[5]')
    print()

    pass
# @lc main=end