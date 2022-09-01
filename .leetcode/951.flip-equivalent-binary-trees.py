# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
#
# https://leetcode.com/problems/flip-equivalent-binary-trees/description/
#
# algorithms
# Medium (66.78%)
# Likes:    1806
# Dislikes: 80
# Total Accepted:    118.2K
# Total Submissions: 177K
# Testcase Example:  '[1,2,3,4,5,6,null,null,null,7,8]\n[1,3,2,null,6,4,5,null,null,null,null,8,7]'
#
# For a binary tree T, we can define a flip operation as follows: choose any
# node, and swap the left and right child subtrees.
#
# A binary tree X is flip equivalent to a binary tree Y if and only if we can
# make X equal to Y after some number of flip operations.
#
# Given the roots of two binary trees root1 and root2, return true if the two
# trees are flip equivalent or false otherwise.
#
#
# Example 1:
#
#
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 =
# [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.
#
#
# Example 2:
#
#
# Input: root1 = [], root2 = []
# Output: true
#
#
# Example 3:
#
#
# Input: root1 = [], root2 = [1]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in each tree is in the range [0, 100].
# Each tree will have unique node values in the range [0, 99].
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断两个二叉树是否翻转相似。
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

    def flipEquiv(self, root1: Optional[TreeNode],
                  root2: Optional[TreeNode]) -> bool:

        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return (self.flipEquiv(root1.left, root2.right)
                and self.flipEquiv(root2.left, root1.right)) or (
                    self.flipEquiv(root1.left, root2.left)
                    and self.flipEquiv(root2.right, root1.right))


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 =[1,3,2,null,6,4,5,null,null,null,null,8,7]'
    )
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().flipEquiv(
            listToTreeNode([1, 2, 3, 4, 5, 6, None, None, None, 7, 8]),
            listToTreeNode(
                [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root1 = [], root2 = []')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().flipEquiv(listToTreeNode([]), listToTreeNode([]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root1 = [], root2 = [1]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().flipEquiv(listToTreeNode([]), listToTreeNode([1]))))
    print()

    pass
# @lc main=end