# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (51.45%)
# Likes:    2359
# Dislikes: 61
# Total Accepted:    334.3K
# Total Submissions: 645.4K
# Testcase Example:  '[1,2,3]'
#
# You are given the root of a binary tree containing digits from 0 to 9 only.
#
# Each root-to-leaf path in the tree represents a number.
#
#
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
#
#
# Return the total sum of all root-to-leaf numbers. Test cases are generated so
# that the answer will fit in a 32-bit integer.
#
# A leaf node is a node with no children.
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
#
#
# Example 2:
#
#
# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from os import curdir
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个二叉树，每个结点存储一个0-9的数字，之后从根到叶结点的路径代表一个数字，求所有数字的和。
# 直接递归求解。
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
    def sumNumbers(self, root: TreeNode) -> int:
        def recur(p: TreeNode, num):
            num = num * 10 + p.val
            if not p.left and not p.right:
                return num
            result = 0
            if p.left:
                result += recur(p.left, num)
            if p.right:
                result += recur(p.right, num)

            return result

        return recur(root, 0)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3]')
    print('Exception :')
    print('25')
    print('Output :')
    print(str(Solution().sumNumbers(listToTreeNode([1, 2, 3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [4,9,0,5,1]')
    print('Exception :')
    print('1026')
    print('Output :')
    print(str(Solution().sumNumbers(listToTreeNode([4, 9, 0, 5, 1]))))
    print()

    pass
# @lc main=end