# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#
# https://leetcode.com/problems/fibonacci-number/description/
#
# algorithms
# Easy (67.81%)
# Likes:    1957
# Dislikes: 238
# Total Accepted:    476.1K
# Total Submissions: 702K
# Testcase Example:  '2'
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
# Fibonacci sequence, such that each number is the sum of the two preceding
# ones, starting from 0 and 1. That is,
#
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
#
#
# Given n, calculate F(n).
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#
#
# Example 2:
#
#
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
#
#
# Example 3:
#
#
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#
#
#
# Constraints:
#
#
# 0 <= n <= 30
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# Fibonacci 数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        n1, n2 = 0, 1
        for _ in range(n - 1):
            n1, n2 = n2, n1 + n2
        return n2

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().fib(2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().fib(3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().fib(4)))
    print()

    pass
# @lc main=end