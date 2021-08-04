# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#
# https://leetcode.com/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (49.48%)
# Likes:    679
# Dislikes: 1083
# Total Accepted:    92.2K
# Total Submissions: 186.1K
# Testcase Example:  '2'
#
# Given an integer n, return the count of all numbers with unique digits, x,
# where 0 <= x < 10^n.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 ≤ x <
# 100, excluding 11,22,33,44,55,66,77,88,99
#
#
# Example 2:
#
#
# Input: n = 0
# Output: 1
#
#
#
# Constraints:
#
#
# 0 <= n <= 8
#
#
#

# @lc tags=math;dynamic-programming;backtracking

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 计算给定位数的没有重复数字的数值的个数。
# 就是排列组合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def __init__(self) -> None:
        dp = [1, 9]
        count = [1, 10]
        n = 9
        for i in range(8):
            dp.append(dp[-1] * n)
            count.append(count[-1] + dp[-1])
            n -= 1
        self.count = count

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return self.count[n]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().countNumbersWithUniqueDigits(3)))
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('91')
    print('Output :')
    print(str(Solution().countNumbersWithUniqueDigits(2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 0')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().countNumbersWithUniqueDigits(0)))
    print()

    pass
# @lc main=end