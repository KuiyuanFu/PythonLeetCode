# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (53.48%)
# Likes:    3491
# Dislikes: 209
# Total Accepted:    596.2K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#
#
# Example 2:
#
#
# Input: head = []
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1]
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
#
#
#
# Follow up: Can you solve the problem without modifying the values in the
# list's nodes? (i.e., Only nodes themselves may be changed.)
#

# @lc tags=linked-list

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定一个链表，反转相邻的两个节点。
# 直接操作就行。
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
    def swapPairs(self, head: ListNode) -> ListNode:
        pseudo = ListNode()
        pseudo.next = head
        p = pseudo
        while p.next:
            if p.next.next:
                l = p.next
                r = l.next
                l.next = r.next
                r.next = l
                p.next = r
                p = l
            else:
                break
        return pseudo.next

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4]')
    print('Output :')
    print(str(Solution().swapPairs(listToListNode([1, 2, 3, 4]))))
    print('Exception :')
    print('[2,1,4,3]')
    print()

    print('Example 2:')
    print('Input : ')
    print('head = []')
    print('Output :')
    print(str(Solution().swapPairs(listToListNode([]))))
    print('Exception :')
    print('[]')
    print()

    print('Example 3:')
    print('Input : ')
    print('head = [1]')
    print('Output :')
    print(str(Solution().swapPairs(listToListNode([1]))))
    print('Exception :')
    print('[1]')
    print()

    pass
# @lc main=end