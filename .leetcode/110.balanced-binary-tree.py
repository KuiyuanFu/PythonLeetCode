# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (44.89%)
# Likes:    3539
# Dislikes: 232
# Total Accepted:    571.5K
# Total Submissions: 1.3M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
#
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
#
# Example 3:
#
#
# Input: root = []
# Output: true
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一棵二叉树，判断是否是高度平衡的。
# 后序遍历，判断深度。
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
    def isBalanced(self, root: TreeNode) -> bool:
        # return isBalance and height
        def recur(node: TreeNode) -> Tuple[bool, int]:
            if not node:
                return True, 0
            fl, heightL = recur(node.left)
            fr, heightR = recur(node.right)
            if not (fl and fr) or abs(heightR - heightL) > 1:
                return False, 0

            return (True, max(heightR, heightL) + 1)

        return recur(root)[0]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Output :')
    print(
        str(Solution().isBalanced(listToTreeNode([3, 9, 20, None, None, 15,
                                                  7]))))
    print('Exception :')
    print('true')
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,2,3,3,null,null,4,4]')
    print('Output :')
    print(
        str(Solution().isBalanced(
            listToTreeNode([1, 2, 2, 3, 3, None, None, 4, 4]))))
    print('Exception :')
    print('false')
    print()

    print('Example 3:')
    print('Input : ')
    print('root = []')
    print('Output :')
    print(str(Solution().isBalanced(listToTreeNode([]))))
    print('Exception :')
    print('true')
    print()

    pass
# @lc main=end