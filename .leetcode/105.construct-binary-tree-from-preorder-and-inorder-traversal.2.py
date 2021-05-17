# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (52.61%)
# Likes:    5231
# Dislikes: 131
# Total Accepted:    496.1K
# Total Submissions: 938.4K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.
#
#
# Example 1:
#
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
#
# Example 2:
#
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
#
#
# Constraints:
#
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
#
#
#

# @lc tags=array;tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 递归写法，使用同一个数组。
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recur(p, i, length):
            if length == 0:
                return None
            val = preorder[p]
            root = TreeNode(val)
            index = inorder.index(val, i, i + length)

            lLength = index - i
            rLength = i + length - index - 1
            root.left = recur(p + 1, i, lLength)
            root.right = recur(p + lLength + 1, index + 1, rLength)
            return root

        return recur(0, 0, len(preorder))


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]')
    print('Output :')
    print(str(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))
    print('Exception :')
    print('[3,9,20,null,null,15,7]')
    print()

    print('Example 2:')
    print('Input : ')
    print('preorder = [-1], inorder = [-1]')
    print('Output :')
    print(str(Solution().buildTree([-1], [-1])))
    print('Exception :')
    print('[-1]')
    print()

    pass
# @lc main=end