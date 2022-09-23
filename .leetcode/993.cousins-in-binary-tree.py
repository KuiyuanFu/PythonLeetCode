# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#
# https://leetcode.com/problems/cousins-in-binary-tree/description/
#
# algorithms
# Easy (54.06%)
# Likes:    3123
# Dislikes: 161
# Total Accepted:    223.5K
# Total Submissions: 413.4K
# Testcase Example:  '[1,2,3,4]\n4\n3'
#
# Given the root of a binary tree with unique values and the values of two
# different nodes of the tree x and y, return true if the nodes corresponding
# to the values x and y in the tree are cousins, or false otherwise.
#
# Two nodes of a binary tree are cousins if they have the same depth with
# different parents.
#
# Note that in a binary tree, the root node is at the depth 0, and children of
# each depth k node are at the depth k + 1.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
#
#
# Example 2:
#
#
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
#
#
# Example 3:
#
#
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 100].
# 1 <= Node.val <= 100
# Each node has a unique value.
# x != y
# x and y are exist in the tree.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from tkinter.messagebox import NO
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定二叉树，判断两个节点是否是表兄弟，即深度相同，但父节点不同。
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

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        r1, r2 = None, None

        q = [(root, None, 0)]
        while q:
            t = q.pop()
            p, f, l = t
            if p.val == x:
                r1 = t
                if r2 is not None:
                    break
            elif p.val == y:
                r2 = t
                if r1 is not None:
                    break
            if p.left:
                q.append((p.left, p, l + 1))
            if p.right:
                q.append((p.right, p, l + 1))
        return r1[1] != r2[1] and r1[2] == r2[2]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,4], x = 4, y = 3')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isCousins(listToTreeNode([1, 2, 3, 4]), 4, 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,3,null,4,null,5], x = 5, y = 4')
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().isCousins(listToTreeNode([1, 2, 3, None, 4, None, 5]),
                                 5, 4)))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1,2,3,null,4], x = 2, y = 3')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isCousins(listToTreeNode([1, 2, 3, None, 4]), 2, 3)))
    print()

    pass
# @lc main=end