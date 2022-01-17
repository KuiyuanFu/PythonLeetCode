# @lc app=leetcode id=817 lang=python3
#
# [817] Linked List Components
#

# @lc tags=hash-table;design

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个链表，再给定一个数组，看数组中所有元素在链表中分成几部分。
#
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

    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        res = 0
        s = set(nums)

        f = False
        p = head
        while p:
            if p.val not in s:
                f = False
            else:
                if not f:
                    f = True
                    res += 1

            p = p.next
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [0,1,2,3], nums = [0,1,3]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().numComponents(listToListNode([0, 1, 2, 3]), [0, 1, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [0,1,2,3,4], nums = [0,3,1,4]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().numComponents(listToListNode([0, 1, 2, 3, 4]),
                                     [0, 3, 1, 4])))
    print()

    pass
# @lc main=end