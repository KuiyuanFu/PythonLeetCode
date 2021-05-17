# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个二叉树，求最大深度。
# 直接深度遍历。
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
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        depth = 0
        while stack:
            p, d = stack.pop()
            depth = max(depth, d)
            if p.right:
                stack.append((p.right, d + 1))
            if p.left:
                stack.append((p.left, d + 1))
        return depth


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Output :')
    print(
        str(Solution().maxDepth(listToTreeNode([3, 9, 20, None, None, 15,
                                                7]))))
    print('Exception :')
    print('3')
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,null,2]')
    print('Output :')
    print(str(Solution().maxDepth(listToTreeNode([1, None, 2]))))
    print('Exception :')
    print('2')
    print()

    print('Example 3:')
    print('Input : ')
    print('root = []')
    print('Output :')
    print(str(Solution().maxDepth(listToTreeNode([]))))
    print('Exception :')
    print('0')
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [0]')
    print('Output :')
    print(str(Solution().maxDepth(listToTreeNode([0]))))
    print('Exception :')
    print('1')
    print()

    pass
# @lc main=end