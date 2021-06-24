# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (52.57%)
# Likes:    3338
# Dislikes: 137
# Total Accepted:    522.3K
# Total Submissions: 987.9K
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of
# itself).”
#
#
# Example 1:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#
#
# Example 2:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.
#
#
# Example 3:
#
#
# Input: root = [2,1], p = 2, q = 1
# Output: 2
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the BST.
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 找二叉搜索树中两个结点的公共最小的祖先节点。
# 直接递归，通过结点值左右分布情况，判断。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        t = (p.val - root.val) * (q.val - root.val)
        if t <= 0:
            return root
        else:
            if p.val > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return self.lowestCommonAncestor(root.left, p, q)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    pass
# @lc main=end