# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
#
# https://leetcode.com/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (79.41%)
# Likes:    2560
# Dislikes: 189
# Total Accepted:    83K
# Total Submissions: 104.5K
# Testcase Example:  '7'
#
# Given an integer n, return a list of all possible full binary trees with n
# nodes. Each node of each tree in the answer must have Node.val == 0.
#
# Each element of the answer is the root node of one possible tree. You may
# return the final list of trees in any order.
#
# A full binary tree is a binary tree where each node has exactly 0 or 2
# children.
#
#
# Example 1:
#
#
# Input: n = 7
# Output:
# [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
#
#
# Example 2:
#
#
# Input: n = 3
# Output: [[0,0,0]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
#
#
#

# @lc tags=hash-table;binary-search;sort;random

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 得到所有指定结点数量的满二叉树。
# 直接迭代。
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
def generate():
    dp = [[TreeNode()]]

    while len(dp) < 20:
        newList = []
        dp.append(None)
        dp.append(newList)
        childNodeNumber = len(dp) - 1
        for lIdx in range(0, childNodeNumber, 2):
            for lRoot, rRoot in product(dp[lIdx],
                                        dp[childNodeNumber - (lIdx + 1) - 1]):
                newList.append(TreeNode(left=lRoot, right=rRoot))
    return dp


dp = generate()


class Solution:

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return dp[n - 1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 7')
    print('Exception :')
    print(
        '[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]'
    )
    print('Output :')
    print(str(Solution().allPossibleFBT(7)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('[[0,0,0]]')
    print('Output :')
    print(str(Solution().allPossibleFBT(3)))
    print()

    pass
# @lc main=end