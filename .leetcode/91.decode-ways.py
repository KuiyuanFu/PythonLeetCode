# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (26.98%)
# Likes:    4280
# Dislikes: 3438
# Total Accepted:    557K
# Total Submissions: 2.1M
# Testcase Example:  '"12"'
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
# Given a string s containing only digits, return the number of ways to decode
# it.
#
# The answer is guaranteed to fit in a 32-bit integer.
#
#
# Example 1:
#
#
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
#
#
# Example 2:
#
#
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2
# 2 6).
#
#
# Example 3:
#
#
# Input: s = "0"
# Output: 0
# Explanation: There is no character that is mapped to a number starting with
# 0.
# The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of
# which start with 0.
# Hence, there are no valid ways to decode this since all digits need to be
# mapped.
#
#
# Example 4:
#
#
# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is
# different from "06").
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).
#
#
#

# @lc tags=string;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个字符串，这个字符串只包含数字，来源是一个只包含字母的字符串，将字母转化为1-26的索引所组成的。
# 给定的数字字符串可以有多种字母字符串的解释，求一共可以有多少种解释。
# 使用 FSA，与动态规划。根据相邻两位的关系，判断这两位可能的组合
#
# @lc idea=end

# @lc group=dynamic-programming;finite-state-automaton


# @lc rank=10


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:

        # 0 不能组合
        # 1 必须两个分开解释
        # 2 必须连在一起解释
        # 3 可以分开也剋以连在一起
        table = [
            # 0 1 2 3-6 7-9

            # 0
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],

            # 1
            [2, 3, 3, 3, 3, 3, 3, 3, 3, 3],

            # 2
            [2, 3, 3, 3, 3, 3, 3, 1, 1, 1],

            # 3 3-9
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        nums = [int(c) for c in s]

        ni1 = 1
        ni2 = 1
        i = 0
        for n in nums:
            flag = table[i][n]
            if flag == 0:
                ni1 = 0
            elif flag == 1:
                ni2 = ni1
            elif flag == 2:
                ni1, ni2 = ni2, 0
            else:
                ni1, ni2 = ni1 + ni2, ni1
            i = n
            if ni1 ==0 :
                return 0
        return ni1


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "12"')
    print('Output :')
    print(str(Solution().numDecodings("12")))
    print('Exception :')
    print('2')
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "226"')
    print('Output :')
    print(str(Solution().numDecodings("226")))
    print('Exception :')
    print('3')
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "0"')
    print('Output :')
    print(str(Solution().numDecodings("0")))
    print('Exception :')
    print('0')
    print()

    print('Example 4:')
    print('Input : ')
    print('s = "06"')
    print('Output :')
    print(str(Solution().numDecodings("06")))
    print('Exception :')
    print('0')
    print()

    pass
# @lc main=end