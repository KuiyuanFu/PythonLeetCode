# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
#
# algorithms
# Medium (73.38%)
# Likes:    2681
# Dislikes: 70
# Total Accepted:    142.3K
# Total Submissions: 193.9K
# Testcase Example:  '[8,3,10,1,6,null,14,null,null,4,7,13]'
#
# Given the root of a binary tree, find the maximum value v for which there
# exist different nodes a and b where v = |a.val - b.val| and a is an ancestor
# of b.
#
# A node a is an ancestor of b if either: any child of a is equal to b or any
# child of a is an ancestor of b.
#
#
# Example 1:
#
#
# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are
# given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1|
# = 7.
#
# Example 2:
#
#
# Input: root = [1,null,2,null,0,3]
# Output: 3
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 5000].
# 0 <= Node.val <= 10^5
#
#
#

# @lc tags=greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定二叉树，找祖先与叶子节点差值最大的值
# 直接递归
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

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        q = [(root, root.val, root.val)]

        res = 0
        while q:
            p, l, r = q.pop()
            v = p.val
            res = max(res, abs(l - v), abs(r - v))
            l, r = min(l, v), max(r, v)
            if p.left:
                q.append((p.left, l, r))
            if p.right:
                q.append((p.right, l, r))
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [8,3,10,1,6,null,14,null,null,4,7,13]')
    print('Exception :')
    print('7')
    print('Output :')
    print(
        str(Solution().maxAncestorDiff(
            listToTreeNode([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,null,2,null,0,3]')
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().maxAncestorDiff(listToTreeNode([1, None, 2, None, 0,
                                                       3]))))
    print()

    pass
# @lc main=end