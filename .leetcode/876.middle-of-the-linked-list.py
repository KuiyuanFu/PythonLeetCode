# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
# https://leetcode.com/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (72.50%)
# Likes:    5063
# Dislikes: 127
# Total Accepted:    618.3K
# Total Submissions: 852.4K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, return the middle node of the linked
# list.
#
# If there are two middle nodes, return the second middle node.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we
# return the second one.
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100
#
#
#

# @lc tags=ordered-map

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找链表中间元素，直接两个指针。
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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left, right = head, head
        while right.next:
            right = right.next
            if right.next:
                right = right.next
            left = left.next
        return left
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5]')
    print('Exception :')
    print('[3,4,5]')
    print('Output :')
    print(str(Solution().middleNode(listToListNode([1, 2, 3, 4, 5]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2,3,4,5,6]')
    print('Exception :')
    print('[4,5,6]')
    print('Output :')
    print(str(Solution().middleNode(listToListNode([1, 2, 3, 4, 5, 6]))))
    print()

    pass
# @lc main=end