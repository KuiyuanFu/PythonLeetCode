# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list/description/
#
# algorithms
# Medium (41.68%)
# Likes:    3255
# Dislikes: 148
# Total Accepted:    329.8K
# Total Submissions: 790K
# Testcase Example:  '[1,2,3,4]'
#
# You are given the head of a singly linked-list. The list can be represented
# as:
#
#
# L0 → L1 → … → Ln - 1 → Ln
#
#
# Reorder the list to be on the following form:
#
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
#
# You may not modify the values in the list's nodes. Only nodes themselves may
# be changed.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 1000
#
#
#

# @lc tags=linked-list

# @lc imports=start

from email import header
from tkinter.messagebox import NO
from traceback import print_exc
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个链表，重新排序，以索引为标识符，排序为 1，n-1，2，n-2 ...
# 思想是将这个排序过程分步，首先将后半段链表进行反转，第二步再依次插入到前半段中。
# @lc idea=end

# @lc group=linked-list

# @lc rank=10

# @lc code=start


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        # find half position
        pseudo = ListNode(next=head)
        slow = pseudo
        fast = pseudo
        while True:
            if fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                break

        # set reverse value
        p = slow.next
        slow.next = None
        pNext = p.next
        p.next = None
        # reverse
        while pNext:
            pNN = pNext.next
            pNext.next = p
            p = pNext
            pNext = pNN

        # reorder
        pl = head
        pr = p
        while pr:
            plN = pl.next
            pl.next = pr
            prN = pr.next
            pr.next = plN
            pl = plN
            pr = prN

        return head

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().reorderList(listToListNode([1]))))
    print(str(Solution().reorderList(listToListNode([1, 2]))))
    print(str(Solution().reorderList(listToListNode([1, 2, 3]))))
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4]')
    print('Exception :')
    print('[1,4,2,3]')
    print('Output :')
    print(str(Solution().reorderList(listToListNode([1, 2, 3, 4]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2,3,4,5]')
    print('Exception :')
    print('[1,5,2,4,3]')
    print('Output :')
    print(str(Solution().reorderList(listToListNode([1, 2, 3, 4, 5]))))
    print()

    pass
# @lc main=end