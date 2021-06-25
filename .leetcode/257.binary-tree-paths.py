# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (54.67%)
# Likes:    2722
# Dislikes: 142
# Total Accepted:    409.9K
# Total Submissions: 745K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: ["1"]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定二叉树，求从根节点到所有叶子结点的路径。
# 直接递归。
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ret = []
        pres = []

        def rBinaryTreePaths(root: TreeNode, ):
            pres.append(str(root.val))
            if not root.left and not root.right:
                ret.append('->'.join(pres))
            if root.left:
                rBinaryTreePaths(root.left)
            if root.right:
                rBinaryTreePaths(root.right)
            pres.pop()

        rBinaryTreePaths(root)
        return ret


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,3,null,5]')
    print('Exception :')
    print('["1->2->5","1->3"]')
    print('Output :')
    print(str(Solution().binaryTreePaths(listToTreeNode([1, 2, 3, None, 5]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('["1"]')
    print('Output :')
    print(str(Solution().binaryTreePaths(listToTreeNode([1]))))
    print()

    pass
# @lc main=end