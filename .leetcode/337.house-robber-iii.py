# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#
# https://leetcode.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (52.19%)
# Likes:    4487
# Dislikes: 73
# Total Accepted:    223.3K
# Total Submissions: 427.7K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called root.
#
# Besides the root, each house has one and only one parent house. After a tour,
# the smart thief realized that all houses in this place form a binary tree. It
# will automatically contact the police if two directly-linked houses were
# broken into on the same night.
#
# Given the root of the binary tree, return the maximum amount of money the
# thief can rob without alerting the police.
#
#
# Example 1:
#
#
# Input: root = [3,2,3,null,3,null,1]
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
#
#
# Example 2:
#
#
# Input: root = [3,4,5,1,3,null,1]
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# 0 <= Node.val <= 10^4
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 抢劫，给定一个二叉树，为小区房屋排列的方式，不能抢相邻的房屋，求最大的金额。
# 动态规划，递归的方式。
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
    def rob(self, root: TreeNode) -> int:
        def recursion(p: TreeNode):
            if not p:
                return 0, 0, 0
            maximum = 0

            leftPro, leftLeftPro, leftRightPro = recursion(p.left)
            rightPro, rightLeftPro, rightRightPro = recursion(p.right)

            # contain p
            m = p.val + leftLeftPro + leftRightPro + rightLeftPro + rightRightPro
            maximum = m if m > maximum else maximum

            # not contain p
            m = leftPro + rightPro
            maximum = m if m > maximum else maximum

            #       p     p.left  p.right
            return maximum, leftPro, rightPro
            pass

        return recursion(root)[0]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,2,3,null,3,null,1]')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().rob(listToTreeNode([3, 2, 3, None, 3, None, 1]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [3,4,5,1,3,null,1]')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().rob(listToTreeNode([3, 4, 5, 1, 3, None, 1]))))
    print()

    pass
# @lc main=end