# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (50.05%)
# Likes:    6152
# Dislikes: 210
# Total Accepted:    681.1K
# Total Submissions: 1.4M
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
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
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
#
# Example 2:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
#
#
# Example 3:
#
#
# Input: root = [1,2], p = 1, q = 2
# Output: 1
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
# p and q will exist in the tree.
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 找二叉中两个结点的公共最小的祖先节点。
# 直接递归，遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        def rLowestCommonAncestor(root: 'TreeNode'):
            if not root:
                return 0, None
            nL, pL = rLowestCommonAncestor(root.left)
            if nL == 2:
                return nL, pL
            nR, pR = rLowestCommonAncestor(root.right)
            if nR == 2:
                return nR, pR
            n = nL + nR + (1 if  root.val == p.val else 0 )\
            + (1 if  root.val == q.val else 0 )
            return n, root

        return rLowestCommonAncestor(root)[1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    pass
# @lc main=end