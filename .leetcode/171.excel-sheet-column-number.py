# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (57.44%)
# Likes:    1754
# Dislikes: 207
# Total Accepted:    383.5K
# Total Submissions: 666.7K
# Testcase Example:  '"A"'
#
# Given a string columnTitle that represents the column title as appear in an
# Excel sheet, return its corresponding column number.
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
# Input: columnTitle = "A"
# Output: 1
#
#
# Example 2:
#
#
# Input: columnTitle = "AB"
# Output: 28
#
#
# Example 3:
#
#
# Input: columnTitle = "ZY"
# Output: 701
#
#
# Example 4:
#
#
# Input: columnTitle = "FXSHRXW"
# Output: 2147483647
#
#
#
# Constraints:
#
#
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# Excel表头数值，转化为数字。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        from functools import reduce
        return reduce(lambda x, y: x * 26 + y,
                      [(ord(c) - 64) for c in columnTitle])

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('columnTitle = "A"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().titleToNumber("A")))
    print()

    print('Example 2:')
    print('Input : ')
    print('columnTitle = "AB"')
    print('Exception :')
    print('28')
    print('Output :')
    print(str(Solution().titleToNumber("AB")))
    print()

    print('Example 3:')
    print('Input : ')
    print('columnTitle = "ZY"')
    print('Exception :')
    print('701')
    print('Output :')
    print(str(Solution().titleToNumber("ZY")))
    print()

    print('Example 4:')
    print('Input : ')
    print('columnTitle = "FXSHRXW"')
    print('Exception :')
    print('2147483647')
    print('Output :')
    print(str(Solution().titleToNumber("FXSHRXW")))
    print()

    pass
# @lc main=end