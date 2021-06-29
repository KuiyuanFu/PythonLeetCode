# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (49.55%)
# Likes:    4664
# Dislikes: 244
# Total Accepted:    412.1K
# Total Submissions: 828.1K
# Testcase Example:  '12'
#
# Given an integer n, return the least number of perfect square numbers that
# sum to n.
#
# A perfect square is an integer that is the square of an integer; in other
# words, it is the product of some integer with itself. For example, 1, 4, 9,
# and 16 are perfect squares while 3 and 11 are not.
#
#
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^4
#
#
#

# @lc tags=math;dynamic-programming;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求一个数最少可以由多少个完美的平方数组成。
# 直接备忘录递归。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        mem = {}

        def rNumSquares(n: int, m: int) -> int:
            if n < 4:
                return n
            if n in mem:
                return mem[n]
            count = n
            m = min(m, int(n**0.5))
            for i in range(m, 0, -1):
                squa = i * i
                if n // squa >= count:
                    continue
                count = min(count, rNumSquares(n - squa, i) + 1)
            mem[n] = count
            return count

        ret = rNumSquares(n, n)
        return ret


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().numSquares(280)))

    print('Example 1:')
    print('Input : ')
    print('n = 12')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().numSquares(12)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 13')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numSquares(13)))
    print()

    pass
# @lc main=end