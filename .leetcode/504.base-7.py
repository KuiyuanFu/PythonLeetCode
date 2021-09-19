# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#
# https://leetcode.com/problems/base-7/description/
#
# algorithms
# Easy (46.85%)
# Likes:    377
# Dislikes: 177
# Total Accepted:    74.4K
# Total Submissions: 158.5K
# Testcase Example:  '100'
#
# Given an integer num, return a string of its base 7 representation.
#
#
# Example 1:
# Input: num = 100
# Output: "202"
# Example 2:
# Input: num = -7
# Output: "-10"
#
#
# Constraints:
#
#
# -10^7 <= num <= 10^7
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 7进制。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:

        r = []
        f = num < 0
        if f:
            num = -num
        while num:
            r.append(str(num % 7))
            num //= 7
        if not r:
            r.append('0')
        return ('-' if f else '') + ''.join(reversed(r))
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num = 100')
    print('Exception :')
    print('"202"')
    print('Output :')
    print(str(Solution().convertToBase7(100)))
    print()

    print('Example 2:')
    print('Input : ')
    print('num = -7')
    print('Exception :')
    print('"-10"')
    print('Output :')
    print(str(Solution().convertToBase7(-7)))
    print()

    pass
# @lc main=end