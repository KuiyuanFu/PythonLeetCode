# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Medium (61.21%)
# Likes:    2884
# Dislikes: 146
# Total Accepted:    179.5K
# Total Submissions: 292.7K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
#
# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
# such that every key of the original BST is changed to the original key plus
# sum of all keys greater than the original key in BST.
#
# As a reminder, a binary search tree is a tree that satisfies these
# constraints:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Note: This question is the same as 1038:
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
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
# Example 3:
#
#
# Input: root = [1,0,2]
# Output: [3,3,2]
#
#
# Example 4:
#
#
# Input: root = [3,2,4,1]
# Output: [7,9,4,10]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# -10^4 <= Node.val <= 10^4
# All the values in the tree are unique.
# root is guaranteed to be a valid binary search tree.
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 使二叉搜索树的节点值为大于等于其元素值的和。
# 中序遍历的方向过程。
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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # n is the number bigger than the node
        def recur(p: Optional[TreeNode], n: int):

            nr = recur(p.right, n) if p.right else n
            p.val += nr
            nl = recur(p.left, p.val) if p.left else p.val
            return nl

        if root:
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
        str(Solution().convertBST(
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
    print(str(Solution().convertBST(listToTreeNode([0, None, 1]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1,0,2]')
    print('Exception :')
    print('[3,3,2]')
    print('Output :')
    print(str(Solution().convertBST(listToTreeNode([1, 0, 2]))))
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [3,2,4,1]')
    print('Exception :')
    print('[7,9,4,10]')
    print('Output :')
    print(str(Solution().convertBST(listToTreeNode([3, 2, 4, 1]))))
    print()

    pass
# @lc main=end