# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#
# https://leetcode.com/problems/utf-8-validation/description/
#
# algorithms
# Medium (38.53%)
# Likes:    314
# Dislikes: 1337
# Total Accepted:    61K
# Total Submissions: 158K
# Testcase Example:  '[197,130,1]'
#
# Given an integer array data representing the data, return whether it is a
# valid UTF-8 encoding.
#
# A character in UTF8 can be from 1 to 4 bytes long, subjected to the following
# rules:
#
#
# For a 1-byte character, the first bit is a 0, followed by its Unicode
# code.
# For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0,
# followed by n - 1 bytes with the most significant 2 bits being 10.
#
#
# This is how the UTF-8 encoding would work:
#
#
# ⁠  Char. number range  |        UTF-8 octet sequence
# ⁠     (hexadecimal)    |              (binary)
# ⁠  --------------------+---------------------------------------------
# ⁠  0000 0000-0000 007F | 0xxxxxxx
# ⁠  0000 0080-0000 07FF | 110xxxxx 10xxxxxx
# ⁠  0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
# ⁠  0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
#
#
# Note: The input is an array of integers. Only the least significant 8 bits of
# each integer is used to store the data. This means each integer represents
# only 1 byte of data.
#
#
# Example 1:
#
#
# Input: data = [197,130,1]
# Output: true
# Explanation: data represents the octet sequence: 11000101 10000010 00000001.
# It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte
# character.
#
#
# Example 2:
#
#
# Input: data = [235,140,4]
# Output: false
# Explanation: data represented the octet sequence: 11101011 10001100 00000100.
# The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes
# character.
# The next byte is a continuation byte which starts with 10 and that's correct.
# But the second continuation byte does not start with 10, so it is
# invalid.
#
#
#
# Constraints:
#
#
# 1 <= data.length <= 2 * 10^4
# 0 <= data[i] <= 255
#
#
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断一个数字序列是否是合法的UTF8序列。
# 直接二进制操作，判断位即可。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        l = 0
        buffer = [
            # 0b00000000,
            0b10000000,
            0b11000000,
            0b11100000,
            0b11110000,
            0b11111000,
        ]
        for d in reversed(data):
            if (d & 0b11000000) == 0b10000000:
                l += 1

            else:
                if l == 0:
                    if (d & 0b10000000) != 0:
                        return False
                else:
                    if l > 3:
                        return False

                    if (d & buffer[l + 1]) != buffer[l]:
                        return False
                    l = 0

        return l == 0
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().validUtf8([240, 162, 138, 147, 145])))
    print(str(Solution().validUtf8([237])))
    print(str(Solution().validUtf8([145])))
    print('Example 1:')
    print('Input : ')
    print('data = [197,130,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().validUtf8([197, 130, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('data = [235,140,4]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().validUtf8([235, 140, 4])))
    print()

    pass
# @lc main=end