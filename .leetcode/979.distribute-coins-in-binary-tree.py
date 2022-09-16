# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
#
# https://leetcode.com/problems/distribute-coins-in-binary-tree/description/
#
# algorithms
# Medium (71.99%)
# Likes:    4131
# Dislikes: 139
# Total Accepted:    93.8K
# Total Submissions: 130.3K
# Testcase Example:  '[3,0,0]'
#
# You are given the root of a binary tree with n nodes where each node in the
# tree has node.val coins. There are n coins in total throughout the whole
# tree.
#
# In one move, we may choose two adjacent nodes and move one coin from one node
# to another. A move may be from parent to child, or from child to parent.
#
# Return the minimum number of moves required to make every node have exactly
# one coin.
#
#
# Example 1:
#
#
# Input: root = [3,0,0]
# Output: 2
# Explanation: From the root of the tree, we move one coin to its left child,
# and one coin to its right child.
#
#
# Example 2:
#
#
# Input: root = [0,3,0]
# Output: 3
# Explanation: From the left child of the root, we move two coins to the root
# [taking two moves]. Then, we move one coin from the root of the tree to the
# right child.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is n.
# 1 <= n <= 100
# 0 <= Node.val <= n
# The sum of all Node.val is n.
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二叉树，每个节点有一个金币数，可以分给相邻节点，求最少移动次数，使每个节点都有一个金币。
# 直接递归。求当前已经移动的次数，及还差多少硬币使其平衡。
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

    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        def recur(p: Optional[TreeNode]):
            if p is None:
                return 0, 0
            lm, ld = recur(p.left)
            rm, rd = recur(p.right)
            m = lm + rm + abs(ld) + abs(rd)
            d = ld + rd + (p.val - 1)
            return m, d

        m, d = recur(root)
        return m

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,0,0]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().distributeCoins(listToTreeNode([3, 0, 0]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [0,3,0]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().distributeCoins(listToTreeNode([0, 3, 0]))))
    print()

    pass
# @lc main=end