# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (49.67%)
# Likes:    2799
# Dislikes: 85
# Total Accepted:    416.5K
# Total Submissions: 834.9K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given the root of a binary tree and an integer targetSum, return all
# root-to-leaf paths where each path's sum equals targetSum.
#
# A leaf is a node with no children.
#
#
# Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
#
#
# Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: []
#
#
# Example 3:
#
#
# Input: root = [1,2], targetSum = 0
# Output: []
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
# 给定一个二叉树，从root到叶子结点的路径上结点值的和等于目标值的路径。
# 回溯遍历。
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
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []

        stack = []
        path = []
        if root:
            stack.append((root, 0))

        s = 0
        while stack:
            node, t = stack.pop()
            if t == 0:
                s += node.val
                path.append(node.val)

                if not node.left and not node.right:
                    if s == targetSum:
                        result.append(path.copy())
                    s -= node.val
                    path.pop()
                else:
                    stack.append((node, 1))
                    if node.left:
                        stack.append((node.left, 0))

            elif t == 1:
                stack.append((node, 2))
                if node.right:
                    stack.append((node.right, 0))
            elif t == 2:
                s -= node.val
                path.pop()
        return result
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22')
    print('Output :')
    print(
        str(Solution().pathSum(
            listToTreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),
            22)))
    print('Exception :')
    print('[[5,4,11,2],[5,8,4,5]]')
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,3], targetSum = 5')
    print('Output :')
    print(str(Solution().pathSum(listToTreeNode([1, 2, 3]), 5)))
    print('Exception :')
    print('[]')
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1,2], targetSum = 0')
    print('Output :')
    print(str(Solution().pathSum(listToTreeNode([1, 2]), 0)))
    print('Exception :')
    print('[]')
    print()

    pass
# @lc main=end