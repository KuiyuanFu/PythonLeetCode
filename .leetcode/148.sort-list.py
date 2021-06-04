# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (47.21%)
# Likes:    4344
# Dislikes: 179
# Total Accepted:    360.9K
# Total Submissions: 763.4K
# Testcase Example:  '[4,2,1,3]'
#
# Given the head of a linked list, return the list after sorting it in
# ascending order.
#
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory
# (i.e. constant space)?
#
#
# Example 1:
#
#
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#
#
# Example 2:
#
#
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
#
#
# Example 3:
#
#
# Input: head = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 5 * 10^4].
# -10^5 <= Node.val <= 10^5
#
#
#

# @lc tags=linked-list;sort

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 排序一个链表，要求 O nlgn。
# 那就归并排序了。
# 比较高级的做法是从下至上的动态规划做法。
# 首先以步长为2，来划分组，合并。之后将步长翻倍，重复操作。知道步长大于了两倍的长度，这样就没有需要合并的了，也就结束了。
#
# @lc idea=end

# @lc group=linked-list;sort

# @lc rank=10


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(pseudo, endL, endR) -> ListNode:
            beginL = pseudo.next
            beginR = endL.next
            tail = endR.next
            p = pseudo
            while True:
                # select smaller
                if beginL.val < beginR.val:
                    # move
                    p.next = beginL
                    p = p.next
                    # end
                    if beginL == endL:
                        p.next = beginR
                        endR.next = tail
                        # return the last node
                        return endR
                    else:
                        beginL = beginL.next
                else:
                    p.next = beginR
                    p = p.next

                    if beginR == endR:
                        p.next = beginL
                        endL.next = tail
                        return endL
                    else:
                        beginR = beginR.next

        pseudo = ListNode(next=head)
        step = 2
        while True:
            half = step // 2
            p = pseudo
            flag = True
            flagT = False
            while p.next:
                if flag:
                    ps = p
                else:
                    # left sub list end node
                    endL = p
                for _ in range(half):
                    if p.next:
                        p = p.next
                    else:
                        break
                if not flag:
                    # right sub list end node
                    endR = p
                    p = merge(ps, endL, endR)
                    flagT = True
                flag = not flag

            if not flagT:
                break
            step *= 2
        return pseudo.next
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [4,2,1,3]')
    print('Exception :')
    print('[1,2,3,4]')
    print('Output :')
    print(str(Solution().sortList(listToListNode([4, 2, 1, 3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [-1,5,3,4,0]')
    print('Exception :')
    print('[-1,0,3,4,5]')
    print('Output :')
    print(str(Solution().sortList(listToListNode([-1, 5, 3, 4, 0]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().sortList(listToListNode([]))))
    print()

    pass
# @lc main=end