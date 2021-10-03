# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#
# https://leetcode.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (76.38%)
# Likes:    5224
# Dislikes: 214
# Total Accepted:    448.3K
# Total Submissions: 584.8K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# You are given two binary trees root1 and root2.
#
# Imagine that when you put one of them to cover the other, some nodes of the
# two trees are overlapped while the others are not. You need to merge the two
# trees into a new binary tree. The merge rule is that if two nodes overlap,
# then sum node values up as the new value of the merged node. Otherwise, the
# NOT null node will be used as the node of the new tree.
#
# Return the merged tree.
#
# Note: The merging process must start from the root nodes of both trees.
#
#
# Example 1:
#
#
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
#
#
# Example 2:
#
#
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
#
#
#
# Constraints:
#
#
# The number of nodes in both trees is in the range [0, 2000].
# -10^4 <= Node.val <= 10^4
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 合并二叉树。
# 简单遍历。
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
    def mergeTrees(self, root1: Optional[TreeNode],
                   root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]')
    print('Exception :')
    print('[3,4,5,5,4,null,7]')
    print('Output :')
    print(
        str(Solution().mergeTrees(listToTreeNode([1, 3, 2, 5]),
                                  listToTreeNode([2, 1, 3, None, 4, None,
                                                  7]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root1 = [1], root2 = [1,2]')
    print('Exception :')
    print('[2,2]')
    print('Output :')
    print(
        str(Solution().mergeTrees(listToTreeNode([1]), listToTreeNode([1,
                                                                       2]))))
    print()

    pass
# @lc main=end