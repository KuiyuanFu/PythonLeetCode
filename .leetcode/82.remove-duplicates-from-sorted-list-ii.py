# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (39.58%)
# Likes:    2859
# Dislikes: 125
# Total Accepted:    327.2K
# Total Submissions: 826.1K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the
# linked list sorted as well.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
#
#
# Example 2:
#
#
# Input: head = [1,1,1,2,3]
# Output: [2,3]
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
# 给定一个有序数组，删除重复元素，只剩下没有重复的元素。
# 类似双指针，直接判断是否重复，之后若重复，判断重复的长度。
#。
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
        pseudo = ListNode(next=head)

        p = pseudo
        while p.next:
            # 结束 或 唯一
            if not p.next.next or p.next.val != p.next.next.val:
                p = p.next
            else:
                # 判断重复长度
                pNext = p.next.next
                while pNext.next and pNext.val == pNext.next.val:
                    pNext = pNext.next
                p.next = pNext.next
        return pseudo.next


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,3,4,4,5]')
    print('Output :')
    print(
        str(Solution().deleteDuplicates(listToListNode([1, 2, 3, 3, 4, 4,
                                                        5]))))
    print('Exception :')
    print('[1,2,5]')
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,1,1,2,3]')
    print('Output :')
    print(str(Solution().deleteDuplicates(listToListNode([1, 1, 1, 2, 3]))))
    print('Exception :')
    print('[2,3]')
    print()

    pass
# @lc main=end