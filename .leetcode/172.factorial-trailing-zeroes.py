# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (39.07%)
# Likes:    1369
# Dislikes: 1425
# Total Accepted:    264.9K
# Total Submissions: 676.9K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
#
# Follow up: Could you write a solution that works in logarithmic time
# complexity?
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
#
#
# Example 2:
#
#
# Input: n = 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
#
#
# Example 3:
#
#
# Input: n = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= n <= 10^4
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个整数n，返回其阶乘有多少个0。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        numbers = [5]
        values = [1]
        t = n // 5
        while t:
            t //= 5
            numbers.append(numbers[-1] * 5)
            values.append(values[-1] * 5 + 1)
        result = 0
        for i in reversed(range(len(numbers))):
            result += n // numbers[i] * values[i]
            n = n % numbers[i]
        return result


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().trailingZeroes(25)))
    print(str(Solution().trailingZeroes(125)))
    print(str(Solution().trailingZeroes(625)))
    print(str(Solution().trailingZeroes(3015)))
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().trailingZeroes(3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().trailingZeroes(5)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().trailingZeroes(0)))
    print()

    pass
# @lc main=end