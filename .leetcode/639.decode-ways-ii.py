# @lc app=leetcode id=639 lang=python3
#
# [639] Decode Ways II
#
# https://leetcode.com/problems/decode-ways-ii/description/
#
# algorithms
# Hard (30.23%)
# Likes:    906
# Dislikes: 713
# Total Accepted:    56.8K
# Total Submissions: 187.6K
# Testcase Example:  '"*"'
#
# A message containing letters from A-Z can be encoded into numbers using the
# following mapping:
#
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
#
#
# To decode an encoded message, all the digits must be grouped then mapped back
# into letters using the reverse of the mapping above (there may be multiple
# ways). For example, "11106" can be mapped into:
#
#
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
#
#
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped
# into 'F' since "6" is different from "06".
#
# In addition to the mapping above, an encoded message may contain the '*'
# character, which can represent any digit from '1' to '9' ('0' is excluded).
# For example, the encoded message "1*" may represent any of the encoded
# messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding
# "1*" is equivalent to decoding any of the encoded messages it can represent.
#
# Given a string s consisting of digits and '*' characters, return the number
# of ways to decode it.
#
# Since the answer may be very large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: s = "*"
# Output: 9
# Explanation: The encoded message can represent any of the encoded messages
# "1", "2", "3", "4", "5", "6", "7", "8", or "9".
# Each of these can be decoded to the strings "A", "B", "C", "D", "E", "F",
# "G", "H", and "I" respectively.
# Hence, there are a total of 9 ways to decode "*".
#
#
# Example 2:
#
#
# Input: s = "1*"
# Output: 18
# Explanation: The encoded message can represent any of the encoded messages
# "11", "12", "13", "14", "15", "16", "17", "18", or "19".
# Each of these encoded messages have 2 ways to be decoded (e.g. "11" can be
# decoded to "AA" or "K").
# Hence, there are a total of 9 * 2 = 18 ways to decode "1*".
#
#
# Example 3:
#
#
# Input: s = "2*"
# Output: 15
# Explanation: The encoded message can represent any of the encoded messages
# "21", "22", "23", "24", "25", "26", "27", "28", or "29".
# "21", "22", "23", "24", "25", and "26" have 2 ways of being decoded, but
# "27", "28", and "29" only have 1 way.
# Hence, there are a total of (6 * 2) + (3 * 1) = 12 + 3 = 15 ways to decode
# "2*".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s[i] is a digit or '*'.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 解码字符串。
# 直接按照状态来，动态规划。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        res = [0, 1]
        counts = [[0, 0, 0], [1, 0, 0]]
        for c in s:
            countso = counts[-1]
            countsn = [0, 0, 0]
            resn = 0
            # type must be 1 or 2
            if c == '0':
                countsn[0] = countso[1] + countso[2]
                resn += (countso[1] + countso[2]) * res[-2]
            if c == '1' or c == '*':
                countsn[1] = 1
                resn += res[-1] + (countso[1] + countso[2]) * res[-2]
            if c == '2' or c == '*':
                countsn[2] = 1
                resn += res[-1] + (countso[1] + countso[2]) * res[-2]
            if '3' <= c <= '6' or c == '*':
                times = 1 if c != '*' else 4
                resn += times * (res[-1] + (countso[1] + countso[2]) * res[-2])
                countsn[0] += times
            if '7' <= c <= '9' or c == '*':
                times = 1 if c != '*' else 3
                resn += times * (res[-1] + countso[1] * res[-2])
                countsn[0] += times
            counts.append(countsn)
            res.append(resn % 1000000007)
        return res[-1]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    # print(str(Solution().numDecodings("*")))
    # print(str(Solution().numDecodings("1*")))
    # print(str(Solution().numDecodings("2*")))
    # print(str(Solution().numDecodings("3*")))
    # print(str(Solution().numDecodings("4*")))
    # print(str(Solution().numDecodings("**")))

    print('Example 1:')
    print('Input : ')
    print('s = "*"')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().numDecodings("*")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "1*"')
    print('Exception :')
    print('18')
    print('Output :')
    print(str(Solution().numDecodings("1*")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "2*"')
    print('Exception :')
    print('15')
    print('Output :')
    print(str(Solution().numDecodings("2*")))
    print()
    print(str(Solution().numDecodings("11106")))
    print('Input : ')
    print('s = "***"')
    print('Exception :')
    print('999')
    print('Output :')
    print(str(Solution().numDecodings("***")))
    pass
# @lc main=end