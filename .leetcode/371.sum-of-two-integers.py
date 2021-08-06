# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Medium (50.66%)
# Likes:    1886
# Dislikes: 2952
# Total Accepted:    239.2K
# Total Submissions: 472.1K
# Testcase Example:  '1\n2'
#
# Given two integers a and b, return the sum of the two integers without using
# the operators + and -.
#
#
# Example 1:
# Input: a = 1, b = 2
# Output: 3
# Example 2:
# Input: a = 2, b = 3
# Output: 5
#
#
# Constraints:
#
#
# -1000 <= a, b <= 1000
#
#
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 使用位操作，计算两个值的和。
#
# @lc idea=end

# @lc group=bit-manipulation

# @lc rank=8


# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xffffffff
        a, b = a & mask, b & mask
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return ~(a ^ mask) if a > 0x7fffffff else a


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().getSum(1, -1)))
    print(str(Solution().getSum(-8, -12)))
    print(str(Solution().getSum(-12, -8)))
    print('Example 1:')
    print('Input : ')
    print('a = 1, b = 2')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().getSum(1, 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('a = 2, b = 3')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().getSum(2, 3)))
    print()

    pass
# @lc main=end