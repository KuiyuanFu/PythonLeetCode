# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (43.19%)
# Likes:    3011
# Dislikes: 207
# Total Accepted:    228.1K
# Total Submissions: 528K
# Testcase Example:  '3'
#
# Given an integer n, return all the structurally unique BST's (binary search
# trees), which has exactly n nodes of unique values from 1 to n. Return the
# answer in any order.
#
#
# Example 1:
#
#
# Input: n = 3
# Output:
# [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 8
#
#
#

# @lc tags=dynamic-programming;tree

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个整数 n，求1至n，这n个数能构成的所有二叉搜索树。
# 这里使用动态规划思想，即从最小子问题开始，如n为0，得到空数组；若为1，返回只含有一个节点的数组；若为其他情况，依次选择一个元素，作为根节点，分别取其左右两个范围的解，作笛卡尔积，之后将结构存放到数组中。
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=8


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        nums = list(range(1, n + 1))
        dp = [[[None] for _ in range(n + 1)] for _ in range(n + 1)]

        for step in range(n):
            for j in range(n - step):
                l = j
                r = j + step
                result = []
                for i in range(j, j + step + 1):
                    lNodes = dp[l][i - 1]
                    rNodes = dp[i + 1][r]

                    for ln in lNodes:
                        for rn in rNodes:
                            root = TreeNode(
                                val=nums[i],
                                left=ln,
                                right=rn,
                            )
                            result.append(root)
                dp[l][r] = result
        return dp[0][n - 1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Output :')
    print(str(Solution().generateTrees(3)))
    print('Exception :')
    print(
        '[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]'
    )
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Output :')
    print(str(Solution().generateTrees(1)))
    print('Exception :')
    print('[[1]]')
    print()

    pass
# @lc main=end