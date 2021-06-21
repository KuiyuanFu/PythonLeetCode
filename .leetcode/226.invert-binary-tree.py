# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (67.82%)
# Likes:    5470
# Dislikes: 79
# Total Accepted:    721.7K
# Total Submissions: 1.1M
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# Given the root of a binary tree, invert the tree, and return its root.
#
#
# Example 1:
#
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
#
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,3,1]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 反转一棵二叉树的结点。
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
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.right, root.left = root.left, root.right
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [4,2,7,1,3,6,9]')
    print('Exception :')
    print('[4,7,2,9,6,3,1]')
    print('Output :')
    print(str(Solution().invertTree(listToTreeNode([4, 2, 7, 1, 3, 6, 9]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [2,1,3]')
    print('Exception :')
    print('[2,3,1]')
    print('Output :')
    print(str(Solution().invertTree(listToTreeNode([2, 1, 3]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().invertTree(listToTreeNode([]))))
    print()

    pass
# @lc main=end