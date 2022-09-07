# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#
# https://leetcode.com/problems/univalued-binary-tree/description/
#
# algorithms
# Easy (69.14%)
# Likes:    1429
# Dislikes: 57
# Total Accepted:    173.3K
# Total Submissions: 250.5K
# Testcase Example:  '[1,1,1,1,1,null,1]'
#
# A binary tree is uni-valued if every node in the tree has the same value.
#
# Given the root of a binary tree, return true if the given tree is uni-valued,
# or false otherwise.
#
#
# Example 1:
#
#
# Input: root = [1,1,1,1,1,null,1]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [2,2,2,5,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 100].
# 0 <= Node.val < 100
#
#
#

# @lc tags=string

# @lc imports=start
from ast import While
import re
from tkinter import W
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断二叉树所有元素是否相同。
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

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        t = root.val

        def recur(r: Optional[TreeNode]):
            return r.val == t and (r.left is None or recur(
                r.left)) and (r.right is None or recur(r.right))

        return recur(root)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,1,1,1,1,null,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().isUnivalTree(listToTreeNode([1, 1, 1, 1, 1, None, 1]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [2,2,2,5,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isUnivalTree(listToTreeNode([2, 2, 2, 5, 2]))))
    print()

    pass
# @lc main=end