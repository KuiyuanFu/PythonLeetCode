# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
#
# algorithms
# Medium (80.86%)
# Likes:    4525
# Dislikes: 64
# Total Accepted:    266.5K
# Total Submissions: 329.5K
# Testcase Example:  '[8,5,1,7,10,12]'
#
# Given an array of integers preorder, which represents the preorder traversal
# of a BST (i.e., binary search tree), construct the tree and return its root.
#
# It is guaranteed that there is always possible to find a binary search tree
# with the given requirements for the given test cases.
#
# A binary search tree is a binary tree where for every node, any descendant of
# Node.left has a value strictly less than Node.val, and any descendant of
# Node.right has a value strictly greater than Node.val.
#
# A preorder traversal of a binary tree displays the value of the node first,
# then traverses Node.left, then traverses Node.right.
#
#
# Example 1:
#
#
# Input: preorder = [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
#
#
# Example 2:
#
#
# Input: preorder = [1,3]
# Output: [1,null,3]
#
#
#
# Constraints:
#
#
# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 1000
# All the values of preorder are unique.
#
#
#

# @lc tags=dynamic-programming;tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 从一个先序遍历序列恢复二叉搜索树。
# 根据大小关系，判断左右。使用栈，记录位置。
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

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        pseudo = TreeNode(0)

        s = [pseudo]
        for v in preorder:
            p = TreeNode(v)

            if v < s[-1].val:
                s[-1].left = p
            else:

                while len(s) >= 2 and s[-2].val < v:
                    s.pop()
                s[-1].right = p
                s.pop()
            s.append(p)
        return pseudo.right
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('preorder = [8,5,1,7,10,12]')
    print('Exception :')
    print('[8,5,10,1,7,null,12]')
    print('Output :')
    print(str(Solution().bstFromPreorder([8, 5, 1, 7, 10, 12])))
    print()

    print('Example 2:')
    print('Input : ')
    print('preorder = [1,3]')
    print('Exception :')
    print('[1,null,3]')
    print('Output :')
    print(str(Solution().bstFromPreorder([1, 3])))
    print()

    pass
# @lc main=end