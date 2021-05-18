# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (39.94%)
# Likes:    2420
# Dislikes: 827
# Total Accepted:    559.4K
# Total Submissions: 1.4M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#
#
# Example 2:
#
#
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^5].
# -1000 <= Node.val <= 1000
#
#
#

# @lc tags=tree;depth-first-search;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个二叉树，找最小深度。
# 广度优先遍历。
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
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        nexts = [root]
        depth = 0
        while nexts:
            depth += 1
            currents, nexts = nexts, []
            for node in currents:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    nexts.append(node.left)
                if node.right:
                    nexts.append(node.right)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Output :')
    print(
        str(Solution().minDepth(listToTreeNode([3, 9, 20, None, None, 15,
                                                7]))))
    print('Exception :')
    print('2')
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [2,null,3,null,4,null,5,null,6]')
    print('Output :')
    print(
        str(Solution().minDepth(
            listToTreeNode([2, None, 3, None, 4, None, 5, None, 6]))))
    print('Exception :')
    print('5')
    print()

    pass
# @lc main=end