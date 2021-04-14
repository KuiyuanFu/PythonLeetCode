#
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
# @lc idea=start
#
# 将链表向下一位旋转，也就是将尾变成头，头变成第二个节点。
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
        pseudo .next = p.next
        p .next = None
        tail.next = head
        return pseudo .next


# @lc code=end
