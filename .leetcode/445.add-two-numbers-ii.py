# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (57.35%)
# Likes:    2731
# Dislikes: 212
# Total Accepted:    263.2K
# Total Submissions: 458.1K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
#
# Example 1:
#
#
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
#
#
# Example 2:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
#
#
# Example 3:
#
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
#
#
#
# Follow up: Could you solve it without reversing the input lists?
#
#

# @lc tags=linked-list

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 链表求和。
# 两个栈。
#
# @lc idea=end

# @lc group=

# @lc rank=


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:

        s1, s2 = [], []
        p = l1
        while p:
            s1.append(p.val)
            p = p.next
        p = l2
        while p:
            s2.append(p.val)
            p = p.next
        if len(s1) < len(s2):
            s1, s2 = s2, s1
            l1, l2 = l2, l1
        cb = 0
        rs = []
        length1 = len(s1)
        while cb or s1 or s2:
            n1 = s1.pop() if s1 else 0
            n2 = s2.pop() if s2 else 0
            n = n1 + n2 + cb
            cb = n // 10
            rs.append(n % 10)
        if len(rs) == length1:
            res = l1
        else:
            res = ListNode(next=l1)
        p = res
        for n in reversed(rs):
            p.val = n
            p = p.next
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('l1 = [7,2,4,3], l2 = [5,6,4]')
    print('Exception :')
    print('[7,8,0,7]')
    print('Output :')
    print(str(Solution().addTwoNumbers([7, 2, 4, 3], [5, 6, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('l1 = [2,4,3], l2 = [5,6,4]')
    print('Exception :')
    print('[8,0,7]')
    print('Output :')
    print(str(Solution().addTwoNumbers([2, 4, 3], [5, 6, 4])))
    print()

    print('Example 3:')
    print('Input : ')
    print('l1 = [0], l2 = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().addTwoNumbers([0], [0])))
    print()

    pass
# @lc main=end