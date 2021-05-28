# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (35.73%)
# Likes:    5822
# Dislikes: 402
# Total Accepted:    514.6K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3]'
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent
# nodes in the sequence has an edge connecting them. A node can only appear in
# the sequence at most once. Note that the path does not need to pass through
# the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any path.
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 =
# 6.
#
#
# Example 2:
#
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7
# = 42.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -1000 <= Node.val <= 1000
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
import re
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求树上两个结点最长的路径。
# 直接线段树。
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
    def maxPathSum(self, root: TreeNode) -> int:
        def recur(root: TreeNode):
            if not root:
                return 0, 0
            if not root.left and not root.right:
                return root.val, root.val
            if not root.right:
                pl, ml = recur(root.left)
                p = root.val + max(0, pl)
                m = max(p, ml)
                return p, m
            if not root.left:
                pr, mr = recur(root.right)
                p = root.val + max(0, pr)
                m = max(p, mr)
                return p, m

            pl, ml = recur(root.left)
            pr, mr = recur(root.right)
            # root to left path sum
            p = root.val + max(pl, pr, 0)
            # max sum
            m = max(root.val + max(pl, 0) + max(pr, 0), ml, mr)
            return p, m

        return recur(root)[1]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().maxPathSum(listToTreeNode([1, 2, 3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [-10,9,20,null,null,15,7]')
    print('Exception :')
    print('42')
    print('Output :')
    print(
        str(Solution().maxPathSum(
            listToTreeNode([-10, 9, 20, None, None, 15, 7]))))
    print()

    pass
# @lc main=end