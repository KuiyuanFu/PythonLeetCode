# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (54.29%)
# Likes:    3256
# Dislikes: 87
# Total Accepted:    722.9K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given the roots of two binary trees p and q, write a function to check if
# they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
#
#
# Example 1:
#
#
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#
#
# Example 2:
#
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
#
#
# Example 3:
#
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个树，判断是否相同。
# 直接遍历，比较。
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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (not p and not q):
            return True
        if (not p or not q):
            return False
        stack = []
        stack.append((p, q))
        while stack:
            p, q = stack.pop()
            if p.val != q.val:
                return False

            if p.left and q.left:
                stack.append((p.left, q.left))
            elif p.left or q.left:
                return False

            if p.right and q.right:
                stack.append((p.right, q.right))
            elif p.right or q.right:
                return False

        return True
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('p = [1,2,3], q = [1,2,3]')
    print('Output :')
    print(
        str(Solution().isSameTree(listToTreeNode([1, 2, 3]),
                                  listToTreeNode([1, 2, 3]))))
    print('Exception :')
    print('true')
    print()

    print('Example 2:')
    print('Input : ')
    print('p = [1,2], q = [1,null,2]')
    print('Output :')
    print(
        str(Solution().isSameTree(listToTreeNode([1, 2]),
                                  listToTreeNode([1, None, 2]))))
    print('Exception :')
    print('false')
    print()

    print('Example 3:')
    print('Input : ')
    print('p = [1,2,1], q = [1,1,2]')
    print('Output :')
    print(
        str(Solution().isSameTree(listToTreeNode([1, 2, 1]),
                                  listToTreeNode([1, 1, 2]))))
    print('Exception :')
    print('false')
    print()

    pass
# @lc main=end