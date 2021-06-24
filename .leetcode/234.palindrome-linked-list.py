# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (42.68%)
# Likes:    5646
# Dislikes: 449
# Total Accepted:    684.3K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome.
#
#
# Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
#
#
#
# Follow up: Could you do it in O(n) time and O(1) space?
#

# @lc tags=linked-list;two-pointers

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断一个链表是否是回文。
# 先找到中间位置，之后将一半链表翻转，之后比较。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        pPre, pSlow, pFast = None, head, head
        while pFast:

            pFast = pFast.next
            if not pFast:
                pSlow = pSlow.next
                break
            pFast = pFast.next
            pSlowNext = pSlow.next
            pSlow.next = pPre
            pPre, pSlow = pSlow, pSlowNext

        while pPre:
            if pPre.val != pSlow.val:
                return False
            pPre, pSlow = pPre.next, pSlow.next
        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,2,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPalindrome(listToListNode([1, 2, 2, 1]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [1,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPalindrome(listToListNode([1, 2]))))
    print()

    pass
# @lc main=end