# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (31.92%)
# Likes:    2264
# Dislikes: 1150
# Total Accepted:    369.6K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, rotate the list to the right by k places.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
#
#
# Example 2:
#
#
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
#
#
#
#
#

# @lc tags=linked-list;two-pointers

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定一个链表，在指定位置旋转，即将指定作为头，原头放到尾的位置。
# 两次遍历，得到指定位置的节点，直接旋转。
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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head

        # 链表长度
        pseudo = ListNode()
        pseudo.next = head
        length = 0
        tail = pseudo
        while tail.next:
            length += 1
            tail = tail.next

        # 切断位置
        k = k % length
        if k == 0:
            return head
        p = pseudo
        for _ in range(length - k):
            p = p.next

        # 拼接
        pseudo.next = p.next
        p.next = None
        tail.next = head
        return pseudo.next

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5], k = 2')
    print('Output :')
    print(str(Solution().rotateRight(listToListNode([1, 2, 3, 4, 5]), 2)))
    print('Exception :')
    print('[4,5,1,2,3]')
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [0,1,2], k = 4')
    print('Output :')
    print(str(Solution().rotateRight(listToListNode([0, 1, 2]), 4)))
    print('Exception :')
    print('[2,0,1]')
    print()

    pass
# @lc main=end