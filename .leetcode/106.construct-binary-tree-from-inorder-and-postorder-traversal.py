# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (50.31%)
# Likes:    2667
# Dislikes: 53
# Total Accepted:    297.6K
# Total Submissions: 588.7K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given two integer arrays inorder and postorder where inorder is the inorder
# traversal of a binary tree and postorder is the postorder traversal of the
# same tree, construct and return the binary tree.
#
#
# Example 1:
#
#
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
#
#
# Example 2:
#
#
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
#
#
#
# Constraints:
#
#
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.
#
#
#

# @lc tags=array;tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定中序和后序的遍历数组，恢复二叉树。
# 与中序和先序的类似，只不过使用后序的最后一个元素作为依据。
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        if len(postorder) == 0:
            return None
        pseudo = TreeNode()
        stack = [(0, 0, len(postorder), pseudo, True)]
        while stack:
            p, i, length, father, flag = stack.pop()

            val = postorder[p + length - 1]
            root = TreeNode(val)
            if flag:
                father.left = root
            else:
                father.right = root
            index = inorder.index(val, i, i + length)

            lLength = index - i
            rLength = i + length - index - 1
            if lLength != 0:
                stack.append((p, i, lLength, root, True))
            if rLength != 0:
                stack.append((p + lLength, index + 1, rLength, root, False))

        return pseudo.left


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]')
    print('Output :')
    print(str(Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])))
    print('Exception :')
    print('[3,9,20,null,null,15,7]')
    print()

    print('Example 2:')
    print('Input : ')
    print('inorder = [-1], postorder = [-1]')
    print('Output :')
    print(str(Solution().buildTree([-1], [-1])))
    print('Exception :')
    print('[-1]')
    print()

    pass
# @lc main=end