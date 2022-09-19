# @lc app=leetcode id=988 lang=python3
#
# [988] Smallest String Starting From Leaf
#
# https://leetcode.com/problems/smallest-string-starting-from-leaf/description/
#
# algorithms
# Medium (49.42%)
# Likes:    1264
# Dislikes: 188
# Total Accepted:    59.3K
# Total Submissions: 120.1K
# Testcase Example:  '[0,1,2,3,4,3,4]'
#
# You are given the root of a binary tree where each node has a value in the
# range [0, 25] representing the letters 'a' to 'z'.
#
# Return the lexicographically smallest string that starts at a leaf of this
# tree and ends at the root.
#
# As a reminder, any shorter prefix of a string is lexicographically
# smaller.
#
#
# For example, "ab" is lexicographically smaller than "aba".
#
#
# A leaf of a node is a node that has no children.
#
#
# Example 1:
#
#
# Input: root = [0,1,2,3,4,3,4]
# Output: "dba"
#
#
# Example 2:
#
#
# Input: root = [25,1,3,1,3,0,2]
# Output: "adz"
#
#
# Example 3:
#
#
# Input: root = [2,2,1,null,1,0,null,0]
# Output: "abc"
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 8500].
# 0 <= Node.val <= 25
#
#
#

# @lc tags=tree

# @lc imports=start
from tkinter.messagebox import NO
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定二叉树，求从叶子节点到根节点字典序最小的路径。
# 直接递归。
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

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = ''
        if root.left is None and root.right is None:
            pass
        elif root.left is None:
            res = self.smallestFromLeaf(root.right)
        elif root.right is None:
            res = self.smallestFromLeaf(root.left)
        else:
            res = min(self.smallestFromLeaf(root.left),
                      self.smallestFromLeaf(root.right))
        return res + chr(root.val + ord('a'))

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [0,1,2,3,4,3,4]')
    print('Exception :')
    print('"dba"')
    print('Output :')
    print(
        str(Solution().smallestFromLeaf(listToTreeNode([0, 1, 2, 3, 4, 3,
                                                        4]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [25,1,3,1,3,0,2]')
    print('Exception :')
    print('"adz"')
    print('Output :')
    print(
        str(Solution().smallestFromLeaf(listToTreeNode([25, 1, 3, 1, 3, 0,
                                                        2]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [2,2,1,null,1,0,null,0]')
    print('Exception :')
    print('"abc"')
    print('Output :')
    print(
        str(Solution().smallestFromLeaf(
            listToTreeNode([2, 2, 1, None, 1, 0, None, 0]))))
    print()

    pass
# @lc main=end