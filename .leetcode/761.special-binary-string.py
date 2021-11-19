# @lc app=leetcode id=761 lang=python3
#
# [761] Special Binary String
#
# https://leetcode.com/problems/special-binary-string/description/
#
# algorithms
# Hard (59.30%)
# Likes:    483
# Dislikes: 160
# Total Accepted:    12.5K
# Total Submissions: 21.1K
# Testcase Example:  '"11011000"'
#
# Special binary strings are binary strings with the following two
# properties:
#
#
# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
#
#
# You are given a special binary string s.
#
# A move consists of choosing two consecutive, non-empty, special substrings of
# s, and swapping them. Two strings are consecutive if the last character of
# the first string is exactly one index before the first character of the
# second string.
#
# Return the lexicographically largest resulting string possible after applying
# the mentioned operations on the string.
#
#
# Example 1:
#
#
# Input: s = "11011000"
# Output: "11100100"
# Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are
# swapped.
# This is the lexicographically largest string possible after some number of
# swaps.
#
#
# Example 2:
#
#
# Input: s = "10"
# Output: "10"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 50
# s[i] is either '0' or '1'.
# s is a special binary string.
#
#
#

# @lc tags=heap;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 特殊二进制串，交换两个连续的，形成的最大的串。
# 递归。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = i = 0
        res = []
        for j, v in enumerate(s):
            count = count + 1 if v == '1' else count - 1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(s[i + 1:j]) + '0')
                i = j + 1
        return ''.join(sorted(res)[::-1])


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "11011000"')
    print('Exception :')
    print('"11100100"')
    print('Output :')
    print(str(Solution().makeLargestSpecial("11011000")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "10"')
    print('Exception :')
    print('"10"')
    print('Output :')
    print(str(Solution().makeLargestSpecial("10")))
    print()
    print('Example 2:')
    print('Input : ')
    print('s = "101100101100"')
    print('Exception :')
    print('"110011001010"')
    print('Output :')
    print(str(Solution().makeLargestSpecial("101100101100")))
    print()
    pass
# @lc main=end