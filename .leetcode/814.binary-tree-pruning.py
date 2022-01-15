# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#
# https://leetcode.com/problems/binary-tree-pruning/description/
#
# algorithms
# Medium (71.05%)
# Likes:    2216
# Dislikes: 65
# Total Accepted:    132.2K
# Total Submissions: 186.1K
# Testcase Example:  '[1,null,0,0,1]'
#
# Given the root of a binary tree, return the same tree where every subtree (of
# the given tree) not containing a 1 has been removed.
#
# A subtree of a node node is node plus every node that is a descendant of
# node.
#
#
# Example 1:
#
#
# Input: root = [1,null,0,0,1]
# Output: [1,null,0,null,1]
# Explanation:
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
#
#
# Example 2:
#
#
# Input: root = [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
#
#
# Example 3:
#
#
# Input: root = [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 200].
# Node.val is either 0 or 1.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 去掉不包含1的子树。
# 简单递归。
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
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(p: Optional[TreeNode]):
            if not p:
                return p, False
            pl, fl = recur(p.left)
            pr, fr = recur(p.right)
            if not fl and not fr and p.val == 0:
                return None, False
            p.left = pl
            p.right = pr
            return p, True

        root, _ = recur(root)
        return root

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,0,0,1]')
    print('Exception :')
    print('[1,null,0,null,1]')
    print('Output :')
    print(str(Solution().pruneTree(listToTreeNode([1, None, 0, 0, 1]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,0,1,0,0,0,1]')
    print('Exception :')
    print('[1,null,1,null,1]')
    print('Output :')
    print(str(Solution().pruneTree(listToTreeNode([1, 0, 1, 0, 0, 0, 1]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1,1,0,1,1,0,1,0]')
    print('Exception :')
    print('[1,1,0,1,1,null,1]')
    print('Output :')
    print(str(Solution().pruneTree(listToTreeNode([1, 1, 0, 1, 1, 0, 1, 0]))))
    print()

    pass
# @lc main=end