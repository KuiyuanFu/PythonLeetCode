# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (29.00%)
# Likes:    6068
# Dislikes: 691
# Total Accepted:    982.4K
# Total Submissions: 3.4M
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, determine if it is a valid binary search
# tree (BST).
#
# A valid BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 迭代写法。
#
#
# @lc idea=end

# @lc group=depth-first-search

# @lc rank=10


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        buffer = []
        buffer.append((root, None, None))
        while buffer:
            root, l, r = buffer.pop()
            if root.left:
                if root.left.val < root.val and (not l or l < root.left.val):
                    buffer.append((root.left, l, root.val))
                else:
                    return False
            if root.right:
                if root.right.val > root.val and (not r or r > root.right.val):
                    buffer.append((root.right, root.val, r))
                else:
                    return False
        return True
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [2,1,3]')
    print('Output :')
    print(str(Solution().isValidBST(listToTreeNode([2, 1, 3]))))
    print('Exception :')
    print('true')
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [5,1,4,null,null,3,6]')
    print('Output :')
    print(
        str(Solution().isValidBST(listToTreeNode([5, 1, 4, None, None, 3,
                                                  6]))))
    print('Exception :')
    print('false')
    print()

    pass
# @lc main=end