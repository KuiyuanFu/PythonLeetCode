# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#
# https://leetcode.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (52.97%)
# Likes:    2154
# Dislikes: 39
# Total Accepted:    93.1K
# Total Submissions: 174.8K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings word1 and word2, return the minimum number of steps
# required to make word1 and word2 the same.
#
# In one step, you can delete exactly one character in either string.
#
#
# Example 1:
#
#
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".
#
#
# Example 2:
#
#
# Input: word1 = "leetcode", word2 = "etco"
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= word1.length, word2.length <= 500
# word1 and word2 consist of only lowercase English letters.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 通过删除字符使两字符串相同。
# 动态规划。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1) + 1, len(word2) + 1
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            dp[i][0] = i
        for j in range(cols):
            dp[0][j] = j
        for i in range(1, rows):
            for j in range(1, cols):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = (1 + min(dp[i - 1][j], dp[i][j - 1]))
        return dp[-1][-1]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('word1 = "sea", word2 = "eat"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minDistance("sea", "eat")))
    print()

    print('Example 2:')
    print('Input : ')
    print('word1 = "leetcode", word2 = "etco"')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().minDistance("leetcode", "etco")))
    print()

    pass
# @lc main=end