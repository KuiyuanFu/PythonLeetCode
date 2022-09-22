# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#
# https://leetcode.com/problems/broken-calculator/description/
#
# algorithms
# Medium (54.11%)
# Likes:    2392
# Dislikes: 197
# Total Accepted:    90.1K
# Total Submissions: 166.5K
# Testcase Example:  '2\n3'
#
# There is a broken calculator that has the integer startValue on its display
# initially. In one operation, you can:
#
#
# multiply the number on display by 2, or
# subtract 1 from the number on display.
#
#
# Given two integers startValue and target, return the minimum number of
# operations needed to display target on the calculator.
#
#
# Example 1:
#
#
# Input: startValue = 2, target = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 ->
# 3}.
#
#
# Example 2:
#
#
# Input: startValue = 5, target = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.
#
#
# Example 3:
#
#
# Input: startValue = 3, target = 10
# Output: 3
# Explanation: Use double, decrement and double {3 -> 6 -> 5 -> 10}.
#
#
#
# Constraints:
#
#
# 1 <= startValue, target <= 10^9
#
#
#

# @lc tags=array;hash-table

# @lc imports=start
from difflib import restore
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个初始值，和一个目标值，可以对初始值加倍，或减一，求最少步数。
#
# 2的指数，求常数
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def brokenCalc(self, n: int, t: int) -> int:

        res = 0
        ns = [1]
        while n < t:
            ns.append(ns[-1] * 2)
            n *= 2
            res += 1

        diff = n - t

        for n in reversed(ns):
            t = diff // n
            res += t
            diff -= t * n
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('startValue = 2, target = 3')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().brokenCalc(2, 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('startValue = 5, target = 8')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().brokenCalc(5, 8)))
    print()

    print('Example 3:')
    print('Input : ')
    print('startValue = 3, target = 10')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().brokenCalc(3, 10)))
    print()

    pass
# @lc main=end