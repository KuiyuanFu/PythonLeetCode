# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#
# https://leetcode.com/problems/range-sum-of-bst/description/
#
# algorithms
# Easy (85.13%)
# Likes:    4470
# Dislikes: 335
# Total Accepted:    649.1K
# Total Submissions: 761.3K
# Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
#
# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range
# [low, high].
#
#
# Example 1:
#
#
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 =
# 32.
#
#
# Example 2:
#
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 =
# 23.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 2 * 10^4].
# 1 <= Node.val <= 10^5
# 1 <= low <= high <= 10^5
# All Node.val are unique.
#
#
#

# @lc tags=math;dynamic-programming

# @lc imports=start
from platform import node
from turtle import hideturtle
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二叉搜索树，区域和。
# 直接遍历。
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

    def rangeSumBST(self, root: Optional[TreeNode], low: int,
                    high: int) -> int:
        res = 0
        nodes = [root]

        while nodes:
            node = nodes.pop()
            val = node.val
            if low <= val <= high:
                res += val
            if node.right and val < high:
                nodes.append(node.right)
            if node.left and val > low:
                nodes.append(node.left)

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [10,5,15,3,7,null,18], low = 7, high = 15')
    print('Exception :')
    print('32')
    print('Output :')
    print(
        str(Solution().rangeSumBST(listToTreeNode([10, 5, 15, 3, 7, None, 18]),
                                   7, 15)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10')
    print('Exception :')
    print('23')
    print('Output :')
    print(
        str(Solution().rangeSumBST(
            listToTreeNode([10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10)))
    print()

    pass
# @lc main=end