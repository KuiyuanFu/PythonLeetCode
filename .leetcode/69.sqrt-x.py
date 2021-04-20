# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (35.44%)
# Likes:    1935
# Dislikes: 2332
# Total Accepted:    712.1K
# Total Submissions: 2M
# Testcase Example:  '4'
#
# Given a non-negative integer x, compute and return the square root of x.
#
# Since the return type is an integer, the decimal digits are truncated, and
# only the integer part of the result is returned.
#
#
# Example 1:
#
#
# Input: x = 4
# Output: 2
#
#
# Example 2:
#
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part
# is truncated, 2 is returned.
#
#
# Constraints:
#
#
# 0 <= x <= 2^31 - 1
#
#
#


# @lc tags=math;binary-search

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定一个32位的非负整数 x ，求其平方根的整数部分。
# 朴素思想是从0开始，以此求其二次幂，之后判断是否大于 x 。
# 这样时间复杂度是不可接受的。就使用二分搜索，加速这个过程。
# 还有一个问题，就是直接计算二次幂的话，很可能会溢出，虽然在 Python 中不会出现这个情况，但也需要考虑，将 m*m > x 改为 m > x / m。
#
# @lc idea=end

# @lc group=binary-search

# @lc rank=10

# @lc code=start


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l != r:
            # m 为较右的一个
            m = l + (r-l+1) // 2
            if m > x / m:
                r = m-1
            else:
                l = m
        return l


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('x = 4')
    print('Output :')
    print(str(Solution().mySqrt(4)))
    print('Exception :')
    print('2')
    print()

    print('Example 2:')
    print('Input : ')
    print('x = 8')
    print('Output :')
    print(str(Solution().mySqrt(8)))
    print('Exception :')
    print('2')
    print()

    pass
# @lc main=end
