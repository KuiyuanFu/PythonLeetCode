# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (46.73%)
# Likes:    2455
# Dislikes: 147
# Total Accepted:    583.9K
# Total Submissions: 1.2M
# Testcase Example:  '[1,1,2]'
#
# Given the head of a sorted linked list, delete all duplicates such that each
# element appears only once. Return the linked list sorted as well.
#
#
# Example 1:
#
#
# Input: head = [1,1,2]
# Output: [1,2]
#
#
# Example 2:
#
#
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
#
#
#

# @lc tags=linked-list

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个有序数组，删除重复元素，每个元素只能有一个。
# 类似双指针，直接判断是否重复。
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pseudo = ListNode(next=head)
        p = pseudo.next
        while p.next:
            if p.val != p.next.val:
                p = p.next
            else:
                p.next = p.next.next

        return pseudo.next


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,1,2]')
    print('Output :')
    print(str(Solution().deleteDuplicates(listToListNode([1, 1, 2]))))
    print('Exception :')
    print('[1,2]')
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,1,2,3,3]')
    print('Output :')
    print(str(Solution().deleteDuplicates(listToListNode([1, 1, 2, 3, 3]))))
    print('Exception :')
    print('[1,2,3]')
    print()

    pass
# @lc main=end