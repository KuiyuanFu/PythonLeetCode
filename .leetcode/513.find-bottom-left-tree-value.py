# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (63.77%)
# Likes:    1642
# Dislikes: 191
# Total Accepted:    146.5K
# Total Submissions: 229.4K
# Testcase Example:  '[2,1,3]'
#
# Given the root of a binary tree, return the leftmost value in the last row of
# the tree.
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: 1
#
#
# Example 2:
#
#
# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
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

# @lc tags=tree;depth-first-search;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求树最低层，最左侧的值。
# bfs。
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = [root]
        r = 0
        while q:
            qn = []
            r = q[0].val
            for p in q:
                if p.left:
                    qn.append(p.left)
                if p.right:
                    qn.append(p.right)
            q = qn
        return r

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [2,1,3]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findBottomLeftValue(listToTreeNode([2, 1, 3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,3,4,null,5,6,null,null,7]')
    print('Exception :')
    print('7')
    print('Output :')
    print(
        str(Solution().findBottomLeftValue(
            listToTreeNode([1, 2, 3, 4, None, 5, 6, None, None, 7]))))
    print()

    pass
# @lc main=end