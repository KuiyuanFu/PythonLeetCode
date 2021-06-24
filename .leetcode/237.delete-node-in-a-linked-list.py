# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#
# https://leetcode.com/problems/delete-node-in-a-linked-list/description/
#
# algorithms
# Easy (68.10%)
# Likes:    2815
# Dislikes: 9449
# Total Accepted:    630.8K
# Total Submissions: 921K
# Testcase Example:  '[4,5,1,9]\n5'
#
# Write a function to delete a node in a singly-linked list. You will not be
# given access to the head of the list, instead you will be given access to the
# node to be deleted directly.
#
# It is guaranteed that the node to be deleted is not a tail node in the
# list.
#
#
# Example 1:
#
#
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list
# should become 4 -> 1 -> 9 after calling your function.
#
#
# Example 2:
#
#
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list
# should become 4 -> 5 -> 9 after calling your function.
#
#
# Example 3:
#
#
# Input: head = [1,2,3,4], node = 3
# Output: [1,2,4]
#
#
# Example 4:
#
#
# Input: head = [0,1], node = 0
# Output: [1]
#
#
# Example 5:
#
#
# Input: head = [-3,5,-99], node = -3
# Output: [5,-99]
#
#
#
# Constraints:
#
#
# The number of the nodes in the given list is in the range [2, 1000].
# -1000 <= Node.val <= 1000
# The value of each node in the list is unique.
# The node to be deleted is in the list and is not a tail node
#
#
#

# @lc tags=linked-list

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 删除一个结点，直接给结点的指针。
# 删除后一个结点，将此节点的值改为下一个节点的。
#
# @lc idea=end

# @lc group=linked-list

# @lc rank=10

# @lc code=start


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [4,5,1,9], node = 5')
    print('Exception :')
    print('[4,1,9]')
    print('Output :')
    print(str(Solution().deleteNode(5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('head = [4,5,1,9], node = 1')
    print('Exception :')
    print('[4,5,9]')
    print('Output :')
    print(str(Solution().deleteNode(1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('head = [1,2,3,4], node = 3')
    print('Exception :')
    print('[1,2,4]')
    print('Output :')
    print(str(Solution().deleteNode(3)))
    print()

    print('Example 4:')
    print('Input : ')
    print('head = [0,1], node = 0')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().deleteNode(0)))
    print()

    print('Example 5:')
    print('Input : ')
    print('head = [-3,5,-99], node = -3')
    print('Exception :')
    print('[5,-99]')
    print('Output :')
    print(str(Solution().deleteNode(-3)))
    print()

    pass
# @lc main=end