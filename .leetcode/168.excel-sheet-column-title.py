# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (32.13%)
# Likes:    1757
# Dislikes: 315
# Total Accepted:    258.9K
# Total Submissions: 804.4K
# Testcase Example:  '1'
#
# Given an integer columnNumber, return its corresponding column title as it
# appears in an Excel sheet.
#
# For example:
#
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
#
#
#
# Example 1:
#
#
# Input: columnNumber = 1
# Output: "A"
#
#
# Example 2:
#
#
# Input: columnNumber = 28
# Output: "AB"
#
#
# Example 3:
#
#
# Input: columnNumber = 701
# Output: "ZY"
#
#
# Example 4:
#
#
# Input: columnNumber = 2147483647
# Output: "FXSHRXW"
#
#
#
# Constraints:
#
#
# 1 <= columnNumber <= 2^31 - 1
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个数字，求字母表示形式，即26进制，最低值为1。
# 直接递归。
# 改写成迭代算法。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        buf = ''
        while columnNumber != 0:
            columnNumber -= 1
            buf = chr(65 + columnNumber % 26) + buf
            columnNumber = columnNumber // 26
        return buf


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('columnNumber = 1')
    print('Exception :')
    print('"A"')
    print('Output :')
    print(str(Solution().convertToTitle(1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('columnNumber = 28')
    print('Exception :')
    print('"AB"')
    print('Output :')
    print(str(Solution().convertToTitle(28)))
    print()

    print('Example 3:')
    print('Input : ')
    print('columnNumber = 701')
    print('Exception :')
    print('"ZY"')
    print('Output :')
    print(str(Solution().convertToTitle(701)))
    print()

    print('Example 4:')
    print('Input : ')
    print('columnNumber = 2147483647')
    print('Exception :')
    print('"FXSHRXW"')
    print('Output :')
    print(str(Solution().convertToTitle(2147483647)))
    print()

    pass
# @lc main=end