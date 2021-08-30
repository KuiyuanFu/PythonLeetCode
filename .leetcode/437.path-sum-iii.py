# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Medium (48.84%)
# Likes:    5861
# Dislikes: 329
# Total Accepted:    293.3K
# Total Submissions: 600.2K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# Given the root of a binary tree and an integer targetSum, return the number
# of paths where the sum of the values along the path equals targetSum.
#
# The path does not need to start or end at the root or a leaf, but it must go
# downwards (i.e., traveling only from parent nodes to child nodes).
#
#
# Example 1:
#
#
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
#
#
# Example 2:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 1000].
# -10^9 <= Node.val <= 10^9
# -1000 <= targetSum <= 1000
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找二叉树中路径和为指定的个数。
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def recur(p: TreeNode):
            if not p:
                return 0, defaultdict(int)
            ln, ld = recur(p.left)
            rn, rd = recur(p.right)

            d = defaultdict(int)
            for td in [ld, rd]:
                for k in td.keys():
                    d[k + p.val] += td[k]
            d[p.val] += 1
            n = ln + rn + d[targetSum]
            return n, d

        return recur(root)[0]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8')
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().pathSum(
            listToTreeNode([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22')
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().pathSum(
            listToTreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),
            22)))

    print()

    pass
# @lc main=end