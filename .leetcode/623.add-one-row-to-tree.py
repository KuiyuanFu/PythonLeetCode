# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#
# https://leetcode.com/problems/add-one-row-to-tree/description/
#
# algorithms
# Medium (53.37%)
# Likes:    1074
# Dislikes: 168
# Total Accepted:    75.8K
# Total Submissions: 142K
# Testcase Example:  '[4,2,6,3,1,5]\n1\n2'
#
# Given the root of a binary tree and two integers val and depth, add a row of
# nodes with value val at the given depth depth.
#
# Note that the root node is at depth 1.
#
# The adding rule is:
#
#
# Given the integer depth, for each not null tree node cur at the depth depth -
# 1, create two tree nodes with value val as cur's left subtree root and right
# subtree root.
# cur's original left subtree should be the left subtree of the new left
# subtree root.
# cur's original right subtree should be the right subtree of the new right
# subtree root.
# If depth == 1 that means there is no depth depth - 1 at all, then create a
# tree node with value val as the new root of the whole original tree, and the
# original tree is the new root's left subtree.
#
#
#
# Example 1:
#
#
# Input: root = [4,2,6,3,1,5], val = 1, depth = 2
# Output: [4,1,1,2,null,null,6,3,1,5]
#
#
# Example 2:
#
#
# Input: root = [4,2,null,3,1], val = 1, depth = 3
# Output: [4,2,null,1,1,3,null,null,1]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# The depth of the tree is in the range [1, 10^4].
# -100 <= Node.val <= 100
# -10^5 <= val <= 10^5
# 1 <= depth <= the depth of tree + 1
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二叉树，加一行。
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
    def addOneRow(self, root: Optional[TreeNode], val: int,
                  depth: int) -> Optional[TreeNode]:
        def recur(p: Optional[TreeNode], val: int,
                  depth: int) -> Optional[TreeNode]:
            if not p:
                return p
            if depth == 1:
                root = TreeNode(val, left=p)
                return root
            elif depth == 2:
                p.left = TreeNode(val, left=p.left)
                p.right = TreeNode(val, right=p.right)
                return p
            else:
                recur(p.left, val, depth - 1)
                recur(p.right, val, depth - 1)
                return p

        return recur(root, val, depth)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [4,2,6,3,1,5], val = 1, depth = 2')
    print('Exception :')
    print('[4,1,1,2,null,null,6,3,1,5]')
    print('Output :')
    print(str(Solution().addOneRow(listToTreeNode([4, 2, 6, 3, 1, 5]), 1, 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [4,2,null,3,1], val = 1, depth = 3')
    print('Exception :')
    print('[4,2,null,1,1,3,null,null,1]')
    print('Output :')
    print(str(Solution().addOneRow(listToTreeNode([4, 2, None, 3, 1]), 1, 3)))
    print()

    pass
# @lc main=end