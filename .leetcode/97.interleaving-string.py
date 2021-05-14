# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Medium (32.85%)
# Likes:    2067
# Dislikes: 109
# Total Accepted:    183.5K
# Total Submissions: 557.5K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
# s1 and s2.
#
# An interleaving of two strings s and t is a configuration where they are
# divided into non-empty substrings such that:
#
#
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 +
# t3 + s3 + ...
#
#
# Note: a + b is the concatenation of strings a and b.
#
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#
#
# Example 3:
#
#
# Input: s1 = "", s2 = "", s3 = ""
# Output: true
#
#
#
# Constraints:
#
#
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.
#
#
#
# Follow up: Could you solve it using only O(s2.length) additional memory
# space?
#
#

# @lc tags=string;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定三个字符串，判断第三个是否可以由前两个字符串交错排列构成。
# 动态规划，s1，s2中的位置p1，p2，如果能交替组成s3中的p3，要么s1[p1]==s3[p3] 且 p1-1,p2能组成p3-1；要么s2[p2]==s3[p3] 且 p1,p2-1能组成p3-1；
#
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=10


# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False

        dp = [[True for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        # 不使用s1是否可以匹配
        for j in range(l2):
            dp[0][j + 1] = dp[0][j] and s2[j] == s3[j]

        # i为使用s1的索引
        for i in range(l1):
            # 不使用s2 是否可以匹配
            dp[i + 1][0] = dp[i][0] and s1[i] == s3[i]
            # j使用s2的索引
            for j in range(l2):
                # k是此时比较的s3中的索引
                k = i + j + 1
                # 或则 s1 匹配，或则 s2 匹配
                dp[i + 1][j + 1] = (dp[i][j + 1] and s1[i] == s3[k])\
                    or (dp[i + 1][j]and s2[j] == s3[k])
        return dp[-1][-1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    # print(str(Solution().isInterleave("aabc", "abad", "aabcabad")))
    print(
        str(Solution().isInterleave("aacaac", "aacaaeaac", "aacaacaaeaacaac")))

    print('Example 1:')
    print('Input : ')
    print('s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"')
    print('Output :')
    print(str(Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")))
    print('Exception :')
    print('true')
    print()

    print('Example 2:')
    print('Input : ')
    print('s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"')
    print('Output :')
    print(str(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc")))
    print('Exception :')
    print('false')
    print()

    print('Example 3:')
    print('Input : ')
    print('s1 = "", s2 = "", s3 = ""')
    print('Output :')
    print(str(Solution().isInterleave("", "", "")))
    print('Exception :')
    print('true')
    print()

    pass
# @lc main=end