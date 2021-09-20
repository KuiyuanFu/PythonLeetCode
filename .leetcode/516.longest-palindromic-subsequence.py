# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (57.36%)
# Likes:    3960
# Dislikes: 229
# Total Accepted:    200.1K
# Total Submissions: 347.8K
# Testcase Example:  '"bbbab"'
#
# Given a string s, find the longest palindromic subsequence's length in s.
#
# A subsequence is a sequence that can be derived from another sequence by
# deleting some or no elements without changing the order of the remaining
# elements.
#
#
# Example 1:
#
#
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求最长的子字符串回文。不改变顺序的子字符串。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for step in range(1, len(s)):
            for l in range(0, len(s) - step):
                r = l + step
                if s[l] == s[r]:
                    dp[l][r] = 2 + dp[l + 1][r - 1]
                else:
                    dp[l][r] = max(dp[l][r - 1], dp[l + 1][r])
        return dp[0][-1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "bbbab"')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().longestPalindromeSubseq("bbbab")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "cbbd"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().longestPalindromeSubseq("cbbd")))
    print('Exception :')
    print('999')
    print('Output :')
    print(
        str(Solution().longestPalindromeSubseq(
            "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
        )))
    print()
    print('Exception :')
    print('1000')
    print('Output :')
    print(
        str(Solution().longestPalindromeSubseq(
            "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
        )))
    print()

    pass
# @lc main=end