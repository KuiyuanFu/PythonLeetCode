# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (35.69%)
# Likes:    11336
# Dislikes: 2703
# Total Accepted:    1.9M
# Total Submissions: 5.2M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
#
# Example 1:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
#
# Example 2:
#
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
#
# Example 3:
#
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
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

# @lc tags=linked-list;math

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定两个倒序排列的数字的链表，求和。
# 首先在低位时，直接相加，同时判断进位情况；在超过其中一个链表长度时，需要根据进位情况加到高位上，同时把这一部分链接到之前的根链表上。最后若是较长的链表也读取完了，还有进位，就需要额外建立一个结点，不能利用已有结点了。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    # 整体思想就是相加，得到进位，之后链接剩余的高位，
    # 最后看是否还有进位，若有则再添加一个结点。
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 根为root
        root = l1
        # 最后的非空结点
        left = l1
        # 进位
        a = 0
        while (l1 and l2):
            # 得到值与进位
            i = (l1.val + l2.val + a)
            a = i // 10
            i = i % 10
            # 赋值
            l1.val = i
            # 移动
            left = l1
            l1 = l1.next
            l2 = l2.next

        # 选择剩下的那颗树
        right = l1
        if l2:
            right = l2

        # 读剩下的树
        while (right):
            i = (right.val + a)
            a = i // 10
            i = i % 10
            right.val = i
            # 链接
            left.next = right
            left = right
            right = right.next
        # 进位
        if a == 1:
            left.next = ListNode(a)
        return root
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('l1 = [2,4,3], l2 = [5,6,4]')
    print('Output :')
    print(
        str(Solution().addTwoNumbers(listToListNode([2, 4, 3]),
                                     listToListNode([5, 6, 4]))))
    print('Exception :')
    print('[7,0,8]')
    print()

    print('Example 2:')
    print('Input : ')
    print('l1 = [0], l2 = [0]')
    print('Output :')
    print(
        str(Solution().addTwoNumbers(listToListNode([0]),
                                     listToListNode([0]))))
    print('Exception :')
    print('[0]')
    print()

    print('Example 3:')
    print('Input : ')
    print('l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]')
    print('Output :')
    print(
        str(Solution().addTwoNumbers(listToListNode([9, 9, 9, 9, 9, 9, 9]),
                                     listToListNode([9, 9, 9, 9]))))
    print('Exception :')
    print('[8,9,9,9,0,0,0,1]')
    print()

    pass
# @lc main=end