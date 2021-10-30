# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#
# https://leetcode.com/problems/split-linked-list-in-parts/description/
#
# algorithms
# Medium (53.87%)
# Likes:    1484
# Dislikes: 176
# Total Accepted:    86K
# Total Submissions: 153.3K
# Testcase Example:  '[1,2,3]\n5'
#
# Given the head of a singly linked list and an integer k, split the linked
# list into k consecutive linked list parts.
#
# The length of each part should be as equal as possible: no two parts should
# have a size differing by more than one. This may lead to some parts being
# null.
#
# The parts should be in the order of occurrence in the input list, and parts
# occurring earlier should always have a size greater than or equal to parts
# occurring later.
#
# Return an array of the k parts.
#
#
# Example 1:
#
#
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a
# ListNode is [].
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most
# 1, and earlier parts are a larger size than the later parts.
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 1000].
# 0 <= Node.val <= 1000
# 1 <= k <= 50
#
#
#

# @lc tags=linked-list

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 分割单链表。
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
    def splitListToParts(self, head: Optional[ListNode],
                         k: int) -> List[Optional[ListNode]]:

        length = 0
        p = head
        while p is not None:
            length += 1
            p = p.next
        partLength = length // k
        longerCount = length - partLength * k

        res = []
        pP = None
        p = head
        for _ in range(longerCount):
            res.append(p)

            for _ in range(partLength + 1):
                pP, p = p, p.next
            if pP:
                pP.next = None
        for _ in range(k - longerCount):
            res.append(p)

            for _ in range(partLength):
                pP, p = p, p.next
            if pP:
                pP.next = None
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3], k = 5')
    print('Exception :')
    print('[[1],[2],[3],[],[]]')
    print('Output :')
    print(str(Solution().splitListToParts(listToListNode([1, 2, 3]), 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2,3,4,5,6,7,8,9,10], k = 3')
    print('Exception :')
    print('[[1,2,3,4],[5,6,7],[8,9,10]]')
    print('Output :')
    print(
        str(Solution().splitListToParts(
            listToListNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)))
    print()

    pass
# @lc main=end