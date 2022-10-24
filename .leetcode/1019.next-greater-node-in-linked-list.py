# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#
# https://leetcode.com/problems/next-greater-node-in-linked-list/description/
#
# algorithms
# Medium (59.82%)
# Likes:    2539
# Dislikes: 102
# Total Accepted:    116.5K
# Total Submissions: 194.8K
# Testcase Example:  '[2,1,5]'
#
# You are given the head of a linked list with n nodes.
#
# For each node in the list, find the value of the next greater node. That is,
# for each node, find the value of the first node that is next to it and has a
# strictly larger value than it.
#
# Return an integer array answer where answer[i] is the value of the next
# greater node of the i^th node (1-indexed). If the i^th node does not have a
# next greater node, set answer[i] = 0.
#
#
# Example 1:
#
#
# Input: head = [2,1,5]
# Output: [5,5,0]
#
#
# Example 2:
#
#
# Input: head = [2,7,4,3,5]
# Output: [7,0,5,5,0]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is n.
# 1 <= n <= 10^4
# 1 <= Node.val <= 10^9
#
#
#

# @lc tags=array;two-pointers

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找接下来严格大于其的数
# 直接递减排列
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

    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []

        p = head
        q = []
        i = 0
        while p:
            v = p.val

            res.append(0)

            while q and q[-1][1] < v:
                pi = q[-1][0]
                q.pop()
                res[pi] = v

            q.append((i, v))
            i += 1
            p = p.next

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [2,1,5]')
    print('Exception :')
    print('[5,5,0]')
    print('Output :')
    print(str(Solution().nextLargerNodes(listToListNode([2, 1, 5]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [2,7,4,3,5]')
    print('Exception :')
    print('[7,0,5,5,0]')
    print('Output :')
    print(str(Solution().nextLargerNodes(listToListNode([2, 7, 4, 3, 5]))))
    print()

    pass
# @lc main=end