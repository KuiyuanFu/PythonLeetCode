# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (57.09%)
# Likes:    1685
# Dislikes: 3115
# Total Accepted:    475.6K
# Total Submissions: 832.7K
# Testcase Example:  '3'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
#
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
#
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
# Given an integer, convert it to a roman numeral.
#
#
# Example 1:
#
#
# Input: num = 3
# Output: "III"
#
#
# Example 2:
#
#
# Input: num = 4
# Output: "IV"
#
#
# Example 3:
#
#
# Input: num = 9
# Output: "IX"
#
#
# Example 4:
#
#
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
#
#
# Example 5:
#
#
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
#
# Constraints:
#
#
# 1 <= num <= 3999
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
# 整数转为为罗马数字。
# 高级一点的使用循环，避免冗余代码，代码简洁了，内存占用降低，但是运行效率下降了。
#
# @lc idea=end

# @lc group=math

# @lc rank=10

# @lc code=start


class Solution:
    def intToRoman(self, num: int) -> str:
        s = ''
        keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        values = [
            'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV',
            'I'
        ]
        for i in range(len(keys)):
            s += values[i] * (num // keys[i])
            num = num % keys[i]

        return s

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num = 3')
    print('Output :')
    print(str(Solution().intToRoman(3)))
    print('Exception :')
    print('"III"')
    print()

    print('Example 2:')
    print('Input : ')
    print('num = 4')
    print('Output :')
    print(str(Solution().intToRoman(4)))
    print('Exception :')
    print('"IV"')
    print()

    print('Example 3:')
    print('Input : ')
    print('num = 9')
    print('Output :')
    print(str(Solution().intToRoman(9)))
    print('Exception :')
    print('"IX"')
    print()

    print('Example 4:')
    print('Input : ')
    print('num = 58')
    print('Output :')
    print(str(Solution().intToRoman(58)))
    print('Exception :')
    print('"LVIII"')
    print()

    print('Example 5:')
    print('Input : ')
    print('num = 1994')
    print('Output :')
    print(str(Solution().intToRoman(1994)))
    print('Exception :')
    print('"MCMXCIV"')
    print()

    pass
# @lc main=end