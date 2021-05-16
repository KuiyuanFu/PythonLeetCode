# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (48.58%)
# Likes:    6148
# Dislikes: 164
# Total Accepted:    889.2K
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
#
#
# Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Could you solve it both recursively and iteratively?
#

# @lc tags=tree;depth-first-search;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个二叉树，判断是否左右对称。
# 直接遍历。迭代写法。
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
    def isSymmetric(self, root: TreeNode) -> bool:
        if (not root):
            return True
        stack = []
        stack.append((root.left, root.right))
        while stack:
            p, q = stack.pop()
            if not p and not q:
                continue
            elif not p or not q:
                return False
            if p.val != q.val:
                return False
            stack.append((p.left, q.right))
            stack.append((p.right, q.left))

        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().isSymmetric(listToTreeNode([2, 3, 3, 4, 5, 4, 5]))))

    print('Example 1:')
    print('Input : ')
    print('root = [1,2,2,3,4,4,3]')
    print('Output :')
    print(str(Solution().isSymmetric(listToTreeNode([1, 2, 2, 3, 4, 4, 3]))))
    print('Exception :')
    print('true')
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,2,null,3,null,3]')
    print('Output :')
    print(
        str(Solution().isSymmetric(listToTreeNode([1, 2, 2, None, 3, None,
                                                   3]))))
    print('Exception :')
    print('false')
    print()

    pass
# @lc main=end