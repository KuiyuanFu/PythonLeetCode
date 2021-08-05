# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (42.46%)
# Likes:    1441
# Dislikes: 197
# Total Accepted:    288.9K
# Total Submissions: 680K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
#
# Follow up: Do not use any built-in library function such as sqrt.
#
#
# Example 1:
# Input: num = 16
# Output: true
# Example 2:
# Input: num = 14
# Output: false
#
#
# Constraints:
#
#
# 1 <= num <= 2^31 - 1
#
#
#

# @lc tags=math;binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 确定一个数是否是平方数。
# 二分法。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            m = l + (r - l) // 2
            square = m * m
            if square == num:
                return True
            elif square < num:
                l = m + 1
            else:
                r = m - 1
        return False


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num = 16')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPerfectSquare(16)))
    print()

    print('Example 2:')
    print('Input : ')
    print('num = 14')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPerfectSquare(14)))
    print()

    pass
# @lc main=end