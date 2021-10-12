# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#
# https://leetcode.com/problems/trim-a-binary-search-tree/description/
#
# algorithms
# Medium (64.41%)
# Likes:    3202
# Dislikes: 212
# Total Accepted:    172.6K
# Total Submissions: 267.9K
# Testcase Example:  '[1,0,2]\n1\n2'
#
# Given the root of a binary search tree and the lowest and highest boundaries
# as low and high, trim the tree so that all its elements lies in [low, high].
# Trimming the tree should not change the relative structure of the elements
# that will remain in the tree (i.e., any node's descendant should remain a
# descendant). It can be proven that there is a unique answer.
#
# Return the root of the trimmed binary search tree. Note that the root may
# change depending on the given bounds.
#
#
# Example 1:
#
#
# Input: root = [1,0,2], low = 1, high = 2
# Output: [1,null,2]
#
#
# Example 2:
#
#
# Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
# Output: [3,2,null,1]
#
#
# Example 3:
#
#
# Input: root = [1], low = 1, high = 2
# Output: [1]
#
#
# Example 4:
#
#
# Input: root = [1,null,2], low = 1, high = 3
# Output: [1,null,2]
#
#
# Example 5:
#
#
# Input: root = [1,null,2], low = 2, high = 4
# Output: [2]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree in the range [1, 10^4].
# 0 <= Node.val <= 10^4
# The value of each node in the tree is unique.
# root is guaranteed to be a valid binary search tree.
# 0 <= low <= high <= 10^4
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将搜索二叉树剪枝到给定的范围。
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
    def trimBST(self, root: Optional[TreeNode], low: int,
                high: int) -> Optional[TreeNode]:
        def recur(p: Optional[TreeNode]):
            if not p:
                return None
            if p.val < low:
                return recur(p.right)
            if p.val > high:
                return recur(p.left)
            p.left = recur(p.left)
            p.right = recur(p.right)
            return p

        return recur(root)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,0,2], low = 1, high = 2')
    print('Exception :')
    print('[1,null,2]')
    print('Output :')
    print(str(Solution().trimBST(listToTreeNode([1, 0, 2]), 1, 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [3,0,4,null,2,null,null,1], low = 1, high = 3')
    print('Exception :')
    print('[3,2,null,1]')
    print('Output :')
    print(
        str(Solution().trimBST(
            listToTreeNode([3, 0, 4, None, 2, None, None, 1]), 1, 3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1], low = 1, high = 2')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().trimBST(listToTreeNode([1]), 1, 2)))
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [1,null,2], low = 1, high = 3')
    print('Exception :')
    print('[1,null,2]')
    print('Output :')
    print(str(Solution().trimBST(listToTreeNode([1, None, 2]), 1, 3)))
    print()

    print('Example 5:')
    print('Input : ')
    print('root = [1,null,2], low = 2, high = 4')
    print('Exception :')
    print('[2]')
    print('Output :')
    print(str(Solution().trimBST(listToTreeNode([1, None, 2]), 2, 4)))
    print()

    pass
# @lc main=end