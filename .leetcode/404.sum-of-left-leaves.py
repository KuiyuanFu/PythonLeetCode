# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (52.79%)
# Likes:    2163
# Dislikes: 195
# Total Accepted:    266.7K
# Total Submissions: 503.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the sum of all left leaves.
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and
# 15 respectively.
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: 0
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 计算二叉树左侧叶子的和。
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stacks = [(root, False)]
        s = 0
        while stacks:
            p, f = stacks.pop()

            if not p.left and not p.right:
                if f:
                    s += p.val
            else:
                if p.left:
                    stacks.append((p.left, True))
                if p.right:
                    stacks.append((p.right, False))
        return s
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Exception :')
    print('24')
    print('Output :')
    print(
        str(Solution().sumOfLeftLeaves(
            listToTreeNode([3, 9, 20, None, None, 15, 7]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().sumOfLeftLeaves(listToTreeNode([1]))))
    print()

    pass
# @lc main=end