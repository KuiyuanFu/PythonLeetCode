# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (45.22%)
# Likes:    5792
# Dislikes: 652
# Total Accepted:    684.5K
# Total Submissions: 1.5M
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3'
#
# Given the heads of two singly linked-lists headA and headB, return the node
# at which the two lists intersect. If the two linked lists have no
# intersection at all, return null.
#
# For example, the following two linked lists begin to intersect at node c1:
#
# It is guaranteed that there are no cycles anywhere in the entire linked
# structure.
#
# Note that the linked lists must retain their original structure after the
# function returns.
#
#
# Example 1:
#
#
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA =
# 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as
# [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are
# 3 nodes before the intersected node in B.
#
#
# Example 2:
#
#
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3,
# skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as
# [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node
# before the intersected node in B.
#
#
# Example 3:
#
#
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it
# reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0,
# while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
#
#
#
# Constraints:
#
#
# The number of nodes of listA is in the m.
# The number of nodes of listB is in the n.
# 0 <= m, n <= 3 * 10^4
# 1 <= Node.val <= 10^5
# 0 <= skipA <= m
# 0 <= skipB <= n
# intersectVal is 0 if listA and listB do not intersect.
# intersectVal == listA[skipA + 1] == listB[skipB + 1] if listA and listB
# intersect.
#
#
#
# Follow up: Could you write a solution that runs in O(n) time and use only
# O(1) memory?
#

# @lc tags=linked-list

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定两个链表，其链表后部分是重合的，求第一个重合的结点。
# 想法是读取链表长度，之后取其，再判断。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        def getLength(head: ListNode):
            l = 0
            p = head
            while p:
                l += 1
                p = p.next
            return l

        lA = getLength(headA)
        lB = getLength(headB)
        if lA < lB:
            lA, lB = lB, lA
            headA, headB = headB, headA
        for _ in range(lA - lB):
            headA = headA.next
        while headA:
            if headA == headB:
                break
            headA = headA.next
            headB = headB.next
        return headA

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA =2, skipB = 3'
    )
    print('Exception :')
    # print('Intersected at '8'')
    print('Output :')
    a = listToListNode([4])
    b = listToListNode([5, 6])
    c = listToListNode([1, 8, 4, 5])
    a.next = c
    b.next.next = c
    print(str(Solution().getIntersectionNode(a, b)))
    print()

    pass
# @lc main=end