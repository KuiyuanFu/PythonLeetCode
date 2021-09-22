# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (55.59%)
# Likes:    1558
# Dislikes: 103
# Total Accepted:    130.2K
# Total Submissions: 234.1K
# Testcase Example:  '[4,2,6,1,3]'
#
# Given the root of a Binary Search Tree (BST), return the minimum absolute
# difference between the values of any two different nodes in the tree.
#
#
# Example 1:
#
#
# Input: root = [4,2,6,1,3]
# Output: 1
#
#
# Example 2:
#
#
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 10^4].
# 0 <= Node.val <= 10^5
#
#
#
# Note: This question is the same as 783:
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二叉搜索树，返回任意两节点最小差。
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        preV = -100000

        s = [(root, True)]
        res = 100000
        while s:
            p, f = s.pop()
            if f:
                if p.right:
                    s.append((p.right, True))
                s.append((p, False))
                if p.left:
                    s.append((p.left, True))
            else:
                res = min(res, p.val - preV)
                preV = p.val

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [4,2,6,1,3]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().getMinimumDifference(listToTreeNode([4, 2, 6, 1,
                                                              3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,0,48,null,null,12,49]')
    print('Exception :')
    print('1')
    print('Output :')
    print(
        str(Solution().getMinimumDifference(
            listToTreeNode([1, 0, 48, None, None, 12, 49]))))
    print()

    pass
# @lc main=end