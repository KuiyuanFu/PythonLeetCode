# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
#
# algorithms
# Easy (73.79%)
# Likes:    2849
# Dislikes: 164
# Total Accepted:    177.9K
# Total Submissions: 241.1K
# Testcase Example:  '[1,0,1,0,1,0,1]'
#
# You are given the root of a binary tree where each node has a value 0 or 1.
# Each root-to-leaf path represents a binary number starting with the most
# significant bit.
#
#
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent
# 01101 in binary, which is 13.
#
#
# For all leaves in the tree, consider the numbers represented by the path from
# the root to that leaf. Return the sum of these numbers.
#
# The test cases are generated so that the answer fits in a 32-bits integer.
#
#
# Example 1:
#
#
# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
#
#
# Example 2:
#
#
# Input: root = [0]
# Output: 0
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# Node.val is 0 or 1.
#
#
#

# @lc tags=backtracking;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二叉树叶子表示一个二进制数，求总和。
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

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = [(root, 0)]
        while q:
            p, n = q.pop()
            n = n * 2 + p.val
            if not p.left and not p.right:
                res += n
            else:
                if p.left:
                    q.append((p.left, n))
                if p.right:
                    q.append((p.right, n))

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,0,1,0,1,0,1]')
    print('Exception :')
    print('22')
    print('Output :')
    print(str(Solution().sumRootToLeaf(listToTreeNode([1, 0, 1, 0, 1, 0, 1]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [0]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().sumRootToLeaf(listToTreeNode([0]))))
    print()

    pass
# @lc main=end