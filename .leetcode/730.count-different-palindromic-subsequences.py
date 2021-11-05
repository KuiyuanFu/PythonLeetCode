# @lc app=leetcode id=730 lang=python3
#
# [730] Count Different Palindromic Subsequences
#
# https://leetcode.com/problems/count-different-palindromic-subsequences/description/
#
# algorithms
# Hard (43.48%)
# Likes:    1078
# Dislikes: 56
# Total Accepted:    23.9K
# Total Submissions: 54.5K
# Testcase Example:  '"bccb"'
#
# Given a string s, return the number of different non-empty palindromic
# subsequences in s. Since the answer may be very large, return it modulo 10^9
# + 7.
#
# A subsequence of a string is obtained by deleting zero or more characters
# from the string.
#
# A sequence is palindromic if it is equal to the sequence reversed.
#
# Two sequences a1, a2, ... and b1, b2, ... are different if there is some i
# for which ai != bi.
#
#
# Example 1:
#
#
# Input: s = "bccb"
# Output: 6
# Explanation: The 6 different non-empty palindromic subsequences are 'b', 'c',
# 'bb', 'cc', 'bcb', 'bccb'.
# Note that 'bcb' is counted only once, even though it occurs twice.
#
#
# Example 2:
#
#
# Input: s = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
# Output: 104860361
# Explanation: There are 3104860382 different non-empty palindromic
# subsequences, which is 104860361 modulo 10^9 + 7.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s[i] is either 'a', 'b', 'c', or 'd'.
#
#
#

# @lc tags=string;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 子序列是回文的个数。
# DP，主要问题是如何去重。
# 向内搜索最大范围的相同边界字符，之后去掉这个区间内的。
#
# @lc idea=end

# @lc group=string;dynamic-programming

# @lc rank=10


# @lc code=start
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for stepLength in range(1, length):
            for l in range(length - stepLength):
                r = l + stepLength

                if s[l] != s[r]:
                    t = dp[l][r - 1] + dp[l + 1][r] - dp[l + 1][r - 1]
                else:
                    c = s[l]
                    t = 2 * dp[l + 1][r - 1]

                    li, ri = l + 1, r - 1
                    while li <= ri and s[li] != c:
                        li += 1
                    while li <= ri and s[ri] != c:
                        ri -= 1

                    if li > ri:
                        t += 2
                    elif li == ri:
                        t += 1
                    else:
                        t -= dp[li + 1][ri - 1]

                dp[l][r] = t % 1000000007
        return dp[0][-1]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "bccb"')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().countPalindromicSubsequences("bccb")))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        's = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"'
    )
    print('Exception :')
    print('104860361')
    print('Output :')
    print(
        str(Solution().countPalindromicSubsequences(
            "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba")
            ))
    print()

    pass
# @lc main=end