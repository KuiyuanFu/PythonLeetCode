# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (45.33%)
# Likes:    3501
# Dislikes: 400
# Total Accepted:    342.2K
# Total Submissions: 753.9K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes, in
# the end, should remain as it is.
#
# Follow up:
#
#
# Could you solve the problem in O(1) extra memory space?
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
#
#
# Example 3:
#
#
# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
#
#
# Example 4:
#
#
# Input: head = [1], k = 1
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range sz.
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz
#
#
#

# @lc tags=linked-list

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个链表，反转相邻的 n 个结点。
# 需要二次遍历。
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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        pseudo = ListNode()
        pseudo.next = head
        # p 是上一组的最后一个
        p = pseudo
        while p.next and p.next.next:
            # 看是否够 k个
            t = p
            for _ in range(k):
                t = t.next
                if not t:
                    return pseudo.next

            # 反转
            pNext = p.next
            l = pNext
            r = l.next
            rNext = r.next
            for _ in range(1, k):
                rNext = r.next
                r.next = l
                l = r
                r = rNext

            p.next = l
            pNext.next = r
            p = pNext

        return pseudo.next
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5], k = 2')
    print('Output :')
    print(str(Solution().reverseKGroup(listToListNode([1, 2, 3, 4, 5]), 2)))
    print('Exception :')
    print('[2,1,4,3,5]')
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2,3,4,5], k = 3')
    print('Output :')
    print(str(Solution().reverseKGroup(listToListNode([1, 2, 3, 4, 5]), 3)))
    print('Exception :')
    print('[3,2,1,4,5]')
    print()

    print('Example 3:')
    print('Input : ')
    print('head = [1,2,3,4,5], k = 1')
    print('Output :')
    print(str(Solution().reverseKGroup(listToListNode([1, 2, 3, 4, 5]), 1)))
    print('Exception :')
    print('[1,2,3,4,5]')
    print()

    print('Example 4:')
    print('Input : ')
    print('head = [1], k = 1')
    print('Output :')
    print(str(Solution().reverseKGroup(listToListNode([1]), 1)))
    print('Exception :')
    print('[1]')
    print()

    pass
# @lc main=end