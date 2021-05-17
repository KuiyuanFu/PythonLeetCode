# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (50.79%)
# Likes:    3192
# Dislikes: 99
# Total Accepted:    309.5K
# Total Submissions: 595K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given the head of a singly linked list where elements are sorted in ascending
# order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
#
#
# Example 1:
#
#
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the
# shown height balanced BST.
#
#
# Example 2:
#
#
# Input: head = []
# Output: []
#
#
# Example 3:
#
#
# Input: head = [0]
# Output: [0]
#
#
# Example 4:
#
#
# Input: head = [1,3]
# Output: [3,1]
#
#
#
# Constraints:
#
#
# The number of nodes in head is in the range [0, 2 * 10^4].
# -10^5 <= Node.val <= 10^5
#
#
#

# @lc tags=linked-list;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个有序链表，构造一个平衡二叉搜索树。
# O nlgn 的算法很简单，能达到 O n。
# 因为需要直到总长度，所有先遍历一遍，得到 n。
# 之后需要找到中间结点，不能直接遍历，如此就会达到 O nlgn 。
# 朴素的思想是，直接找中间节点，作为根节点，在对左右子节点进行递归构造。
# 现在对这种思想进行修改，先获得左侧的子节点，再获得中间根节点，最后获得右侧子节点。这样就不用特意找到中间节点了。因为构造左侧子节点的时候，必然遍历到了中间节点的上一个节点。
#
# @lc idea=end

# @lc group=linked-list;depth-first-search

# @lc rank=10


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        # return root node and next node
        def recur(node: ListNode, length) -> Tuple[TreeNode, TreeNode]:
            if length == 0:
                return (None, node)
            if length == 1:
                return (TreeNode(node.val), node.next)

            m = length // 2
            left, node = recur(node, m)
            root = TreeNode(node.val)
            node = node.next
            right, node = recur(node, length - m - 1)
            root.left = left
            root.right = right
            return root, node

        length = 0
        p = head
        while p:
            p = p.next
            length += 1
        return recur(head, length)[0]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [-10,-3,0,5,9]')
    print('Output :')
    print(str(Solution().sortedListToBST(listToListNode([-10, -3, 0, 5, 9]))))
    print('Exception :')
    print('[0,-3,9,-10,null,5]')
    print()

    print('Example 2:')
    print('Input : ')
    print('head = []')
    print('Output :')
    print(str(Solution().sortedListToBST(listToListNode([]))))
    print('Exception :')
    print('[]')
    print()

    print('Example 3:')
    print('Input : ')
    print('head = [0]')
    print('Output :')
    print(str(Solution().sortedListToBST(listToListNode([0]))))
    print('Exception :')
    print('[0]')
    print()

    print('Example 4:')
    print('Input : ')
    print('head = [1,3]')
    print('Output :')
    print(str(Solution().sortedListToBST(listToListNode([1, 3]))))
    print('Exception :')
    print('[3,1]')
    print()

    pass
# @lc main=end