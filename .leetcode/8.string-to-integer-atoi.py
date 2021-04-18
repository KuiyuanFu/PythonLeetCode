# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
# https://leetcode.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (15.72%)
# Likes:    192
# Dislikes: 488
# Total Accepted:    716.6K
# Total Submissions: 4.6M
# Testcase Example:  '"42"'
#
# Implement the myAtoi(string s) function, which converts a string to a 32-bit
# signed integer (similar to C/C++'s atoi function).
#
# The algorithm for myAtoi(string s) is as follows:
#
#
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-'
# or '+'. Read this character in if it is either. This determines if the final
# result is negative or positive respectively. Assume the result is positive if
# neither is present.
# Read in next the characters until the next non-digit charcter or the end of
# the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no
# digits were read, then the integer is 0. Change the sign as necessary (from
# step 2).
# If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1],
# then clamp the integer so that it remains in the range. Specifically,
# integers less than -2^31 should be clamped to -2^31, and integers greater
# than 2^31 - 1 should be clamped to 2^31 - 1.
# Return the integer as the final result.
#
#
# Note:
#
#
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of
# the string after the digits.
#
#
#
# Example 1:
#
#
# Input: s = "42"
# Output: 42
# Explanation: The underlined characters are what is read in, the caret is the
# current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
# ⁠        ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
# ⁠        ^
# Step 3: "42" ("42" is read in)
# ⁠          ^
# The parsed integer is 42.
# Since 42 is in the range [-2^31, 2^31 - 1], the final result is 42.
#
#
# Example 2:
#
#
# Input: s = "   -42"
# Output: -42
# Explanation:
# Step 1: "   -42" (leading whitespace is read and ignored)
# ⁠           ^
# Step 2: "   -42" ('-' is read, so the result should be negative)
# ⁠            ^
# Step 3: "   -42" ("42" is read in)
# ⁠              ^
# The parsed integer is -42.
# Since -42 is in the range [-2^31, 2^31 - 1], the final result is -42.
#
#
# Example 3:
#
#
# Input: s = "4193 with words"
# Output: 4193
# Explanation:
# Step 1: "4193 with words" (no characters read because there is no leading
# whitespace)
# ⁠        ^
# Step 2: "4193 with words" (no characters read because there is neither a '-'
# nor '+')
# ⁠        ^
# Step 3: "4193 with words" ("4193" is read in; reading stops because the next
# character is a non-digit)
# ⁠            ^
# The parsed integer is 4193.
# Since 4193 is in the range [-2^31, 2^31 - 1], the final result is 4193.
#
#
# Example 4:
#
#
# Input: s = "words and 987"
# Output: 0
# Explanation:
# Step 1: "words and 987" (no characters read because there is no leading
# whitespace)
# ⁠        ^
# Step 2: "words and 987" (no characters read because there is neither a '-'
# nor '+')
# ⁠        ^
# Step 3: "words and 987" (reading stops immediately because there is a
# non-digit 'w')
# ⁠        ^
# The parsed integer is 0 because no digits were read.
# Since 0 is in the range [-2^31, 2^31 - 1], the final result is 0.
#
#
# Example 5:
#
#
# Input: s = "-91283472332"
# Output: -2147483648
# Explanation:
# Step 1: "-91283472332" (no characters read because there is no leading
# whitespace)
# ⁠        ^
# Step 2: "-91283472332" ('-' is read, so the result should be negative)
# ⁠         ^
# Step 3: "-91283472332" ("91283472332" is read in)
# ⁠                    ^
# The parsed integer is -91283472332.
# Since -91283472332 is less than the lower bound of the range [-2^31, 2^31 -
# 1], the final result is clamped to -2^31 = -2147483648.
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 200
# s consists of English letters (lower-case and upper-case), digits (0-9), ' ',
# '+', '-', and '.'.
#
#
#
#
#
#

# @lc tags=math;string

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 字符串转数字，就是状态有点多，所以使用自动状态机来避免麻烦的状态标记。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        states = [
            # 空格  正负号 数字 其他字符

            # 初始状态
            [0, 1, 2, 3],
            # 已经读取正负号
            [3, 3, 2, 3],
            # 已经读取数字
            [3, 3, 2, 3],


        ]
        positive = 1
        i = 0
        j = 0
        num = ''
        for c in s:

            if c == ' ':
                j = 0
            elif c == '+' or c == '-':
                j = 1
                if i == 0 and c == '-':
                    positive = -1
            elif '0' <= c <= '9':
                j = 2
                num += c
            else:
                j = 3
            i = states[i][j]
            if i == 3:
                break

        num = num.lstrip('0')
        num = '0' if len(num) == 0 else num
        if positive == 1:
            if len(num) > len('2147483647') or len(num) == len('2147483647') and num > '2147483647':
                return 2147483647
        else:
            if len(num) > len('2147483648') or len(num) == len('2147483648') and num > '2147483648':
                return -2147483648

        return positive * int(num)


        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "42"')
    print('Output :')
    print(str(Solution().myAtoi("42")))
    print('Exception :')
    print('42')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "   -42"')
    print('Output :')
    print(str(Solution().myAtoi("   -42")))
    print('Exception :')
    print('-42')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "4193 with words"')
    print('Output :')
    print(str(Solution().myAtoi("4193 with words")))
    print('Exception :')
    print('4193')
    print()
    
    print('Example 4:')
    print('Input : ')
    print('s = "words and 987"')
    print('Output :')
    print(str(Solution().myAtoi("words and 987")))
    print('Exception :')
    print('0')
    print()
    
    print('Example 5:')
    print('Input : ')
    print('s = "-91283472332"')
    print('Output :')
    print(str(Solution().myAtoi("-91283472332")))
    print('Exception :')
    print('-2147483648')
    print()
    
    pass
# @lc main=end