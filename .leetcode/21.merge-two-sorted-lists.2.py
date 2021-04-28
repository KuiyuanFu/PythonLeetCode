# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (56.37%)
# Likes:    6491
# Dislikes: 756
# Total Accepted:    1.4M
# Total Submissions: 2.4M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a sorted list. The list should
# be made by splicing together the nodes of the first two lists.
#
#
# Example 1:
#
#
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
#
# Example 2:
#
#
# Input: l1 = [], l2 = []
# Output: []
#
#
# Example 3:
#
#
# Input: l1 = [], l2 = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.
#
#
#
#

# @lc tags=linked-list

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 试一下更快的写法。
# 失败了，虽然写法上，计算起来是快了，但实际上没变。即每一次少一个判断，但实际上，循环可能更消耗时间。
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l2:
            return l1
        if not l1:
            return l2

        pseudo = ListNode()
        p = pseudo
        flag = l1.val < l2.val
        while True:

            if flag:
                p.next = l1
                p = p.next
                l1 = l1.next
                while True:
                    if not l1:
                        p.next = l2
                        return pseudo.next
                    if l1.val < l2.val:
                        p.next = l1
                        p = p.next
                        l1 = l1.next
                    else:
                        flag = not flag
                        break
            else:
                p.next = l2
                p = p.next
                l2 = l2.next
                while True:
                    if not l2:
                        p.next = l1
                        return pseudo.next
                    if l2.val < l1.val:
                        p.next = l2
                        p = p.next
                        l2 = l2.next
                    else:
                        flag = not flag
                        break

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('l1 = [1,2,4], l2 = [1,3,4]')
    print('Output :')
    print(
        str(Solution().mergeTwoLists(listToListNode([1, 2, 4]),
                                     listToListNode([1, 3, 4]))))
    print('Exception :')
    print('[1,1,2,3,4,4]')
    print()

    print('Example 2:')
    print('Input : ')
    print('l1 = [], l2 = []')
    print('Output :')
    print(str(Solution().mergeTwoLists(listToListNode([]),
                                       listToListNode([]))))
    print('Exception :')
    print('[]')
    print()

    print('Example 3:')
    print('Input : ')
    print('l1 = [], l2 = [0]')
    print('Output :')
    print(
        str(Solution().mergeTwoLists(listToListNode([]), listToListNode([0]))))
    print('Exception :')
    print('[0]')
    print()

    pass
# @lc main=end