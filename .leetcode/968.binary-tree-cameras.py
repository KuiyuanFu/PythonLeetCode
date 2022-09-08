# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#
# https://leetcode.com/problems/binary-tree-cameras/description/
#
# algorithms
# Hard (46.80%)
# Likes:    4412
# Dislikes: 55
# Total Accepted:    110.1K
# Total Submissions: 235.2K
# Testcase Example:  '[0,0,null,0,0]'
#
# You are given the root of a binary tree. We install cameras on the tree nodes
# where each camera at a node can monitor its parent, itself, and its immediate
# children.
#
# Return the minimum number of cameras needed to monitor all nodes of the
# tree.
#
#
# Example 1:
#
#
# Input: root = [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
#
#
# Example 2:
#
#
# Input: root = [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the
# tree. The above image shows one of the valid configurations of camera
# placement.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# Node.val == 0
#
#
#

# @lc tags=divide-and-conquer

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定二叉树，插入相机，相机可以监控父节点、自身节点、子节点。求最少相机数量，使所有节点被监控。
# 递归，返回三个值，自身是相机；自身不是相机但满足条件；自身不是相机不满足条件但子树满足条件。
#
# @lc idea=end

# @lc group=recur

# @lc rank=8


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        def recur(p: Optional[TreeNode]):
            # camera，satisfy, not satisfy
            if p == None:
                return inf, 0, 0
            lc, ls, ln = recur(p.left)
            rc, rs, rn = recur(p.right)
            c = 1 + min(lc, ls, ln) + min(rc, rs, rn)
            s = min(lc + min(rc, rs), rc + min(lc, ls))
            n = ls + rs
            return c, s, n

        r = recur(root)

        return min(r[0], r[1])
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [0,0,null,0,0]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minCameraCover(listToTreeNode([0, 0, None, 0, 0]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [0,0,null,0,null,0,null,null,0]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().minCameraCover(
            listToTreeNode([0, 0, None, 0, None, 0, None, None, 0]))))
    print()

    pass
# @lc main=end