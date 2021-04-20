# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (47.19%)
# Likes:    5485
# Dislikes: 67
# Total Accepted:    349.8K
# Total Submissions: 741.1K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two strings word1 and word2, return the minimum number of operations
# required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
#
# Insert a character
# Delete a character
# Replace a character
#
#
#
# Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
# Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#
#
# Constraints:
#
#
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
#
#
#

# @lc tags=string;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个单词字符串，求从第一个单词转化为第二个单词最小步骤数。每一步可以是插入，删除，替换。
# 动态规划，因为当前需要的转化步骤数依赖于之前的步骤数。
# 初始化一个冗余为1的二位动态规划缓存。第0行与第0列元素值为对应的行号或列号，含义为一个长度为0的单词转化为对应长度单词的步骤数。之后每次迭代，如果对应字符相等，则此位置元素值为左上角的元素值，否则使用替换、删除、插入中较小步骤数的步骤。
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=10


# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        r, c = len(word1) + 1, len(word2) + 1
        dp = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            dp[i][0] = i
        for j in range(c):
            dp[0][j] = j

        for i in range(1, r):
            for j in range(1, c):
                if word2[j - 1] == word1[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 替换， 删除， 插入
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j],
                                   dp[i][j - 1]) + 1

        return dp[-1][-1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('word1 = "horse", word2 = "ros"')
    print('Output :')
    print(str(Solution().minDistance("horse", "ros")))
    print('Exception :')
    print('3')
    print()

    print('Example 2:')
    print('Input : ')
    print('word1 = "intention", word2 = "execution"')
    print('Output :')
    print(str(Solution().minDistance("intention", "execution")))
    print('Exception :')
    print('5')
    print()

    pass
# @lc main=end