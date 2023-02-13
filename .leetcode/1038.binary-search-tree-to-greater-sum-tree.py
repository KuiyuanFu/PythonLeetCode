# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/
#
# algorithms
# Medium (85.58%)
# Likes:    3237
# Dislikes: 144
# Total Accepted:    145.1K
# Total Submissions: 169.6K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
#
# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
# such that every key of the original BST is changed to the original key plus
# the sum of all keys greater than the original key in BST.
#
# As a reminder, a binary search tree is a tree that satisfies these
# constraints:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
# Example 1:
#
#
# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
#
#
# Example 2:
#
#
# Input: root = [0,null,1]
# Output: [1,null,1]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val <= 100
# All the values in the tree are unique.
#
#
#
# Note: This question is the same as 538:
# https://leetcode.com/problems/convert-bst-to-greater-tree/
#
#

# @lc tags=math;backtracking;graph

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一个二叉搜索树转换为一个大树，即二叉搜索树中的每一个节点的值，转换为加上所有大于其值的值。
# 递归
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def bstToGst(self, root: TreeNode) -> TreeNode:

        def recur(p: TreeNode, t):
            res = 0
            if p is not None:
                r = recur(p.right, t)
                res += p.val + r
                l = recur(p.left, t + res)
                res += l
                p.val += r + t

            return res

        recur(root, 0)
        return root
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]')
    print('Exception :')
    print('[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]')
    print('Output :')
    print(
        str(Solution().bstToGst(
            listToTreeNode([
                4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8
            ]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [0,null,1]')
    print('Exception :')
    print('[1,null,1]')
    print('Output :')
    print(str(Solution().bstToGst(listToTreeNode([0, None, 1]))))
    print()

    pass
# @lc main=end