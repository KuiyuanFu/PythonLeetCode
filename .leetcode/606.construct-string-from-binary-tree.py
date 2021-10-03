# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#
# https://leetcode.com/problems/construct-string-from-binary-tree/description/
#
# algorithms
# Easy (56.55%)
# Likes:    1144
# Dislikes: 1507
# Total Accepted:    114.4K
# Total Submissions: 201.8K
# Testcase Example:  '[1,2,3,4]'
#
# Given the root of a binary tree, construct a string consists of parenthesis
# and integers from a binary tree with the preorder traversing way, and return
# it.
#
# Omit all the empty parenthesis pairs that do not affect the one-to-one
# mapping relationship between the string and the original binary tree.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4]
# Output: "1(2(4))(3)"
# Explanation: Originallay it needs to be "1(2(4)())(3()())", but you need to
# omit all the unnecessary empty parenthesis pairs. And it will be
# "1(2(4))(3)"
#
#
# Example 2:
#
#
# Input: root = [1,2,3,null,4]
# Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example, except we cannot omit the
# first parenthesis pair to break the one-to-one mapping relationship between
# the input and the output.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -1000 <= Node.val <= 1000
#
#
#

# @lc tags=string;tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二叉树，中序遍历。
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        l = ('({})'.format(self.tree2str(root.left) if root.left else '')) if (
            root.right or root.left) else ''
        r = ('({})'.format(self.tree2str(root.right))) if root.right else ''
        return str(root.val) + l + r

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,4]')
    print('Exception :')
    print('"1(2(4))(3)"')
    print('Output :')
    print(str(Solution().tree2str(listToTreeNode([1, 2, 3, 4]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,3,null,4]')
    print('Exception :')
    print('"1(2()(4))(3)"')
    print('Output :')
    print(str(Solution().tree2str(listToTreeNode([1, 2, 3, None, 4]))))
    print()

    pass
# @lc main=end