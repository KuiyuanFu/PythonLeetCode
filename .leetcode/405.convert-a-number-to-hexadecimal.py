# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
#
# algorithms
# Easy (44.92%)
# Likes:    702
# Dislikes: 142
# Total Accepted:    85.9K
# Total Submissions: 190.7K
# Testcase Example:  '26'
#
# Given an integer num, return a string representing its hexadecimal
# representation. For negative integers, two’s complement method is used.
#
# All the letters in the answer string should be lowercase characters, and
# there should not be any leading zeros in the answer except for the zero
# itself.
#
# Note: You are not allowed to use any built-in library method to directly
# solve this problem.
#
#
# Example 1:
# Input: num = 26
# Output: "1a"
# Example 2:
# Input: num = -1
# Output: "ffffffff"
#
#
# Constraints:
#
#
# -2^31 <= num <= 2^31 - 1
#
#
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将十进制转化为十六进制。
# 负数取反加一。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:

        num = num & 0xffffffff
        r = ''
        chars = '0123456789abcdef'
        while num:
            r = chars[num & 0xf] + r
            num = num >> 4
        return r if r else '0'

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num = 26')
    print('Exception :')
    print('"1a"')
    print('Output :')
    print(str(Solution().toHex(26)))
    print()

    print('Example 2:')
    print('Input : ')
    print('num = -1')
    print('Exception :')
    print('"ffffffff"')
    print('Output :')
    print(str(Solution().toHex(-1)))
    print()

    pass
# @lc main=end