# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (55.02%)
# Likes:    1368
# Dislikes: 290
# Total Accepted:    107.4K
# Total Submissions: 193.9K
# Testcase Example:  '[4,2,6,1,3]'
#
# Given the root of a Binary Search Tree (BST), return the minimum difference
# between the values of any two different nodes in the tree.
#
#
# Example 1:
#
#
# Input: root = [4,2,6,1,3]
# Output: 1
#
#
# Example 2:
#
#
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 100].
# 0 <= Node.val <= 10^5
#
#
#
# Note: This question is the same as 530:
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找BST的两个元素的最小差。
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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.res = 100000
        self.pre = -100000
        self.recur(root)
        return self.res

    def recur(self, p: Optional[TreeNode]):
        if p.left:
            self.recur(p.left)
        v = p.val
        self.res = min(self.res, v - self.pre)
        self.pre = v
        if p.right:
            self.recur(p.right)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [4,2,6,1,3]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minDiffInBST(listToTreeNode([4, 2, 6, 1, 3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,0,48,null,null,12,49]')
    print('Exception :')
    print('1')
    print('Output :')
    print(
        str(Solution().minDiffInBST(
            listToTreeNode([1, 0, 48, None, None, 12, 49]))))
    print()

    pass
# @lc main=end