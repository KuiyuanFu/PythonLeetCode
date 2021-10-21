# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#
# https://leetcode.com/problems/count-binary-substrings/description/
#
# algorithms
# Easy (61.96%)
# Likes:    2132
# Dislikes: 380
# Total Accepted:    101.4K
# Total Submissions: 161.5K
# Testcase Example:  '"00110011"'
#
# Give a binary string s, return the number of non-empty substrings that have
# the same number of 0's and 1's, and all the 0's and all the 1's in these
# substrings are grouped consecutively.
#
# Substrings that occur multiple times are counted the number of times they
# occur.
#
#
# Example 1:
#
#
# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's
# and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of
# times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are
# not grouped together.
#
#
# Example 2:
#
#
# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal
# number of consecutive 1's and 0's.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s[i] is either '0' or '1'.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 统计01数量相等且同样字符是相邻的子串的个数。
# 加首位，之后统计连续个数，每次变符号，就可以获得前面两个长度的最小值个子串。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = ' ' + s + ' '
        pl, l = 0, 0
        res = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                l += 1
            else:
                res += min(l, pl)
                pl, l = l, 1
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "00110011"')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().countBinarySubstrings("00110011")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "10101"')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().countBinarySubstrings("10101")))
    print()

    pass
# @lc main=end