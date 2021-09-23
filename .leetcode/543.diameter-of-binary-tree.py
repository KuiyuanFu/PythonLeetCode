# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (51.21%)
# Likes:    5759
# Dislikes: 356
# Total Accepted:    551.5K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the root of a binary tree, return the length of the diameter of the
# tree.
#
# The diameter of a binary tree is the length of the longest path between any
# two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges
# between them.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
#
#
# Example 2:
#
#
# Input: root = [1,2]
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
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
# 二叉树，直径，即最长的路径长度。
# 简单递归。
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recur(p: Optional[TreeNode]):
            if not p:
                return 0, 0
            ll, lm = recur(p.left)
            rl, rm = recur(p.right)
            l = 1 + max(ll, rl)
            m = max(lm, rm, ll + rl + 1)
            return l, m

        return recur(root)[1] - 1

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,4,5]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().diameterOfBinaryTree(listToTreeNode([1, 2, 3, 4,
                                                              5]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().diameterOfBinaryTree(listToTreeNode([1, 2]))))
    print()

    pass
# @lc main=end