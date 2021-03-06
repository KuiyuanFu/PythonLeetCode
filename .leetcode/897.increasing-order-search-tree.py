# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#
# https://leetcode.com/problems/increasing-order-search-tree/description/
#
# algorithms
# Easy (77.74%)
# Likes:    3165
# Dislikes: 629
# Total Accepted:    210.1K
# Total Submissions: 268.4K
# Testcase Example:  '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
#
# Given the root of a binary search tree, rearrange the tree in in-order so
# that the leftmost node in the tree is now the root of the tree, and every
# node has no left child and only one right child.
#
#
# Example 1:
#
#
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#
# Example 2:
#
#
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]
#
#
#
# Constraints:
#
#
# The number of nodes in the given tree will be in the range [1, 100].
# 0 <= Node.val <= 1000
#
#

# @lc tags=math

# @lc imports=start
from tkinter.messagebox import NO
from imports import *

# @lc imports=end

# @lc idea=start
#
# 展开搜索二叉树。
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

    def increasingBST(self, root: TreeNode) -> TreeNode:

        def recur(p: TreeNode):
            pl, pr = p, p
            if p.right:
                prt = recur(p.right)
                p.right = prt[0]
                pr = prt[1]
            if p.left:
                plt = recur(p.left)
                p.left = None
                plt[1].right = p
                pl = plt[0]
            return pl, pr

        return recur(root)[0]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [5,3,6,2,4,null,8,1,null,null,null,7,9]')
    print('Exception :')
    print('[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]')
    print('Output :')
    print(
        str(Solution().increasingBST(
            listToTreeNode([5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7,
                            9]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [5,1,7]')
    print('Exception :')
    print('[1,null,5,null,7]')
    print('Output :')
    print(str(Solution().increasingBST(listToTreeNode([5, 1, 7]))))
    print()

    pass
# @lc main=end