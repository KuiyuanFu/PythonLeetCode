# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (42.76%)
# Likes:    3153
# Dislikes: 614
# Total Accepted:    619.7K
# Total Submissions: 1.4M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given the root of a binary tree and an integer targetSum, return true if the
# tree has a root-to-leaf path such that adding up all the values along the
# path equals targetSum.
#
# A leaf is a node with no children.
#
#
# Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: false
#
#
# Example 3:
#
#
# Input: root = [1,2], targetSum = 0
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
#
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
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        stack = []
        if root:
            stack.append((root, 0))

        while stack:
            node, d = stack.pop()
            d += node.val
            if not node.left and not node.right:
                if d == targetSum:
                    return True
            if node.left:
                stack.append((node.left, d))
            if node.right:
                stack.append((node.right, d))

        return False
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22')
    print('Output :')
    print(
        str(Solution().hasPathSum(
            listToTreeNode(
                [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22)))
    print('Exception :')
    print('true')
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,3], targetSum = 5')
    print('Output :')
    print(str(Solution().hasPathSum(listToTreeNode([1, 2, 3]), 5)))
    print('Exception :')
    print('false')
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1,2], targetSum = 0')
    print('Output :')
    print(str(Solution().hasPathSum(listToTreeNode([1, 2]), 0)))
    print('Exception :')
    print('false')
    print()

    pass
# @lc main=end