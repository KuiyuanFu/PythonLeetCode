# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (66.45%)
# Likes:    4592
# Dislikes: 209
# Total Accepted:    966.6K
# Total Submissions: 1.5M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the inorder traversal of its nodes'
# values.
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: [1]
#
#
# Example 4:
#
#
# Input: root = [1,2]
# Output: [2,1]
#
#
# Example 5:
#
#
# Input: root = [1,null,2]
# Output: [1,2]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
#
#
# Follow up:
#
# Recursive solution is trivial, could you do it iteratively?
#
#
#
#

# @lc tags=hash-table;stack;tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二叉树，求中序遍历。
# 使用栈，每次访问节点，先把节点压栈，访问其左节点，直到结束；之后弹栈，访问节点元素，再访问右节点。
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        stack = []
        p = root
        while True:
            if p:
                stack.append(p)
                p = p.left
            elif len(stack) != 0:
                p = stack.pop()
                ret.append(p.val)
                p = p.right
            else:
                break
        return ret


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,2,3]')
    print('Output :')
    print(str(Solution().inorderTraversal(listToTreeNode([1, None, 2, 3]))))
    print('Exception :')
    print('[1,3,2]')
    print()

    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Output :')
    print(str(Solution().inorderTraversal(listToTreeNode([]))))
    print('Exception :')
    print('[]')
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1]')
    print('Output :')
    print(str(Solution().inorderTraversal(listToTreeNode([1]))))
    print('Exception :')
    print('[1]')
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [1,2]')
    print('Output :')
    print(str(Solution().inorderTraversal(listToTreeNode([1, 2]))))
    print('Exception :')
    print('[2,1]')
    print()

    print('Example 5:')
    print('Input : ')
    print('root = [1,null,2]')
    print('Output :')
    print(str(Solution().inorderTraversal(listToTreeNode([1, None, 2]))))
    print('Exception :')
    print('[1,2]')
    print()

    pass
# @lc main=end