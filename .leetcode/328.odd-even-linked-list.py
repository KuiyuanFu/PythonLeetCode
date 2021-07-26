# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (57.80%)
# Likes:    3538
# Dislikes: 347
# Total Accepted:    404.1K
# Total Submissions: 698.9K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, group all the nodes with odd indices
# together followed by the nodes with even indices, and return the reordered
# list.
#
# The first node is considered odd, and the second node is even, and so on.
#
# Note that the relative order inside both the even and odd groups should
# remain as it was in the input.
#
# You must solve the problem in O(1) extra space complexity and O(n) time
# complexity.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
#
#
# Example 2:
#
#
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
#
#
#
# Constraints:
#
#
# n == number of nodes in the linked list
# 0 <= n <= 10^4
# -10^6 <= Node.val <= 10^6
#
#
#

# @lc tags=linked-list

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将链表按照索引奇偶排列，奇的在前。
# 直接假头即可。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        oddTail = head
        evenPseudoHead = ListNode()
        evenTail = evenPseudoHead
        flag = False
        p = head.next
        while p:
            if flag:
                oddTail.next = p
                oddTail = p
            else:
                evenTail.next = p
                evenTail = p
            flag = not flag
            p = p.next
        if evenTail:
            evenTail.next = None
        oddTail.next = evenPseudoHead.next
        return head
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5]')
    print('Exception :')
    print('[1,3,5,2,4]')
    print('Output :')
    print(str(Solution().oddEvenList(listToListNode([1, 2, 3, 4, 5]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [2,1,3,5,6,4,7]')
    print('Exception :')
    print('[2,3,6,7,1,5,4]')
    print('Output :')
    print(str(Solution().oddEvenList(listToListNode([2, 1, 3, 5, 6, 4, 7]))))
    print()

    pass
# @lc main=end