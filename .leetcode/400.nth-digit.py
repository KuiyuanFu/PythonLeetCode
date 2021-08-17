# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Medium (32.67%)
# Likes:    519
# Dislikes: 1304
# Total Accepted:    68.6K
# Total Submissions: 209.6K
# Testcase Example:  '3'
#
# Given an integer n, return the n^th digit of the infinite integer sequence
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 3
#
#
# Example 2:
#
#
# Input: n = 11
# Output: 0
# Explanation: The 11^th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# 11, ... is a 0, which is part of the number 10.
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 从1开始的无限序列，求第n个位上是多少。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def __init__(self) -> None:
        maximum = 2**31 - 1
        dp = [0]
        n = 0
        width = 1
        count = 9
        while dp[-1] < maximum:
            dp.append(count * width + dp[-1])
            count *= 10
            width += 1
        self.dp = dp

    def findNthDigit(self, n: int) -> int:
        idx = bisect_left(self.dp, n)
        b = 10**(idx - 1) + (n - self.dp[idx - 1] - 1) // idx
        return str(b)[(n - self.dp[idx - 1] - 1) % idx]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findNthDigit(3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 11')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().findNthDigit(11)))
    print()

    pass
# @lc main=end