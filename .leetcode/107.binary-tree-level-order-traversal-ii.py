# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Medium (55.61%)
# Likes:    2161
# Dislikes: 246
# Total Accepted:    421.5K
# Total Submissions: 755.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the bottom-up level order traversal
# of its nodes' values. (i.e., from left to right, level by level from leaf to
# root).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
#
#
#

# @lc tags=tree;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个二叉树，层次遍历，从叶子到根。
# 广度优先，之后倒序输出。
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        resultAll = []
        currents = []
        nexts = []
        if root:
            nexts.append(root)
        while nexts:
            currents, nexts, resultLevel = nexts, [], []
            for n in currents:
                resultLevel.append(n.val)
                if n.left:
                    nexts.append(n.left)
                if n.right:
                    nexts.append(n.right)
            resultAll.append(resultLevel)
        return list(reversed(resultAll))
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Output :')
    print(
        str(Solution().levelOrderBottom(
            listToTreeNode([3, 9, 20, None, None, 15, 7]))))
    print('Exception :')
    print('[[15,7],[9,20],[3]]')
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1]')
    print('Output :')
    print(str(Solution().levelOrderBottom(listToTreeNode([1]))))
    print('Exception :')
    print('[[1]]')
    print()

    print('Example 3:')
    print('Input : ')
    print('root = []')
    print('Output :')
    print(str(Solution().levelOrderBottom(listToTreeNode([]))))
    print('Exception :')
    print('[]')
    print()

    pass
# @lc main=end