# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (35.85%)
# Likes:    5066
# Dislikes: 299
# Total Accepted:    832.3K
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
#
# Follow up: Could you do this in one pass?
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
#
# Example 2:
#
#
# Input: head = [1], n = 1
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
#

# @lc tags=linked-list;two-pointers

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 还有一种方法，就是让一个指针先移动指定的次数，之后再与另一个指针同时遍历，这样当先移动的指针遍历结束，另一个指针就到指定的位置。
# 是一个很好的想法，但是实际复杂度是一样的。
# (32 ms) 74.87 %
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pseudo = ListNode()
        pseudo.next = head
        fast = pseudo
        for _ in range(n + 1):
            fast = fast.next
        slow = pseudo
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return pseudo.next
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5], n = 2')
    print('Output :')
    print(str(Solution().removeNthFromEnd(listToListNode([1, 2, 3, 4, 5]), 2)))
    print('Exception :')
    print('[1,2,3,5]')
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1], n = 1')
    print('Output :')
    print(str(Solution().removeNthFromEnd(listToListNode([1]), 1)))
    print('Exception :')
    print('[]')
    print()

    print('Example 3:')
    print('Input : ')
    print('head = [1,2], n = 1')
    print('Output :')
    print(str(Solution().removeNthFromEnd(listToListNode([1, 2]), 1)))
    print('Exception :')
    print('[1]')
    print()

    pass
# @lc main=end