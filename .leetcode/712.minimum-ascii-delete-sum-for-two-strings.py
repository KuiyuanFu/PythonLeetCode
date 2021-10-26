# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
#
# algorithms
# Medium (60.33%)
# Likes:    1651
# Dislikes: 59
# Total Accepted:    54.3K
# Total Submissions: 89.5K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings s1 and s2, return the lowest ASCII sum of deleted
# characters to make two strings equal.
#
#
# Example 1:
#
#
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum
# possible to achieve this.
#
#
# Example 2:
#
#
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d] + 101[e] + 101[e] to the sum.
# Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is
# 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers
# of 433 or 417, which are higher.
#
#
#
# Constraints:
#
#
# 1 <= s1.length, s2.length <= 1000
# s1 and s2 consist of lowercase English letters.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个字符串，求删除字符使其相同的最小ascii码和。
# 动态规划。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for j in range(l2):
            dp[0][j + 1] = dp[0][j] + ord(s2[j])
        for i in range(l1):
            dp[i + 1][0] = dp[i][0] + ord(s1[i])
            for j in range(l2):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(
                        ord(s1[i]) + dp[i][j + 1],
                        ord(s2[j]) + dp[i + 1][j])
        return dp[-1][-1]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s1 = "sea", s2 = "eat"')
    print('Exception :')
    print('231')
    print('Output :')
    print(str(Solution().minimumDeleteSum("sea", "eat")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s1 = "delete", s2 = "leet"')
    print('Exception :')
    print('403')
    print('Output :')
    print(str(Solution().minimumDeleteSum("delete", "leet")))
    print()

    pass
# @lc main=end