# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Medium (38.35%)
# Likes:    2696
# Dislikes: 588
# Total Accepted:    127.5K
# Total Submissions: 330.6K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given the root of a binary tree, return the length of the longest path, where
# each node in the path has the same value. This path may or may not pass
# through the root.
#
# The length of the path between two nodes is represented by the number of
# edges between them.
#
#
# Example 1:
#
#
# Input: root = [5,4,5,1,1,5]
# Output: 2
#
#
# Example 2:
#
#
# Input: root = [1,4,5,4,4,5]
# Output: 2
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
# The depth of the tree will not exceed 1000.
#
#
#

# @lc tags=tree;recursion

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找相同值的最长路径。
# 递归。
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def recur(p: Optional[TreeNode]):
            if p is None:
                return 0, 0
            lm, ll = recur(p.left)
            rm, rl = recur(p.right)
            l = 1
            if p.left is None or p.left.val != p.val:
                ll = 0
            if p.right is None or p.right.val != p.val:
                rl = 0
            return max([lm, rm, l + ll + rl]), l + max(ll, rl)

        return max(recur(root)[0] - 1, 0)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [5,4,5,1,1,5]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().longestUnivaluePath(listToTreeNode([5, 4, 5, 1, 1,
                                                           5]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,4,5,4,4,5]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().longestUnivaluePath(listToTreeNode([1, 4, 5, 4, 4,
                                                           5]))))
    print()

    pass
# @lc main=end