# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (54.78%)
# Likes:    4566
# Dislikes: 168
# Total Accepted:    360.1K
# Total Submissions: 657.2K
# Testcase Example:  '3'
#
# Given an integer n, return the number of structurally unique BST's (binary
# search trees) which has exactly n nodes of unique values from 1 to n.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 5
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 19
#
#
#

# @lc tags=dynamic-programming;tree

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定一个整数 n，求1至n，这n个数能构成的所有二叉搜索树的个数。
# 是上一道题的简化版。
# 这里使用动态规划思想，即从最小子问题开始，如n为0，得到0；若为1，返回1；若为其他情况，依次选择一个元素，作为根节点，分别取其左右两个范围的个数，作积，得到结果。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def numTrees(self, n: int) -> List[TreeNode]:
        nums = list(range(1, n + 1))
        dp = [[1 for _ in range(n + 1)] for _ in range(n + 1)]

        for step in range(n):
            for j in range(n - step):
                l = j
                r = j + step
                result = 0
                for i in range(j, j + step + 1):
                    lNodes = dp[l][i - 1]
                    rNodes = dp[i + 1][r]
                    result += lNodes * rNodes

                dp[l][r] = result
        return dp[0][n - 1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Output :')
    print(str(Solution().numTrees(3)))
    print('Exception :')
    print('5')
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Output :')
    print(str(Solution().numTrees(1)))
    print('Exception :')
    print('1')
    print()

    pass
# @lc main=end