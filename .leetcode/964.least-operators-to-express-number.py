# @lc app=leetcode id=964 lang=python3
#
# [964] Least Operators to Express Number
#
# https://leetcode.com/problems/least-operators-to-express-number/description/
#
# algorithms
# Hard (47.75%)
# Likes:    270
# Dislikes: 66
# Total Accepted:    8.3K
# Total Submissions: 17.5K
# Testcase Example:  '3\n19'
#
# Given a single positive integer x, we will write an expression of the form x
# (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either
# addition, subtraction, multiplication, or division (+, -, *, or /). For
# example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.
#
# When writing such an expression, we adhere to the following
# conventions:
#
#
# The division operator (/) returns rational numbers.
# There are no parentheses placed anywhere.
# We use the usual order of operations: multiplication and division happen
# before addition and subtraction.
# It is not allowed to use the unary negation operator (-). For example, "x -
# x" is a valid expression as it only uses subtraction, but "-x + x" is not
# because it uses negation.
#
#
# We would like to write an expression with the least number of operators such
# that the expression equals the given target. Return the least number of
# operators used.
#
#
# Example 1:
#
#
# Input: x = 3, target = 19
# Output: 5
# Explanation: 3 * 3 + 3 * 3 + 3 / 3.
# The expression contains 5 operations.
#
#
# Example 2:
#
#
# Input: x = 5, target = 501
# Output: 8
# Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.
# The expression contains 8 operations.
#
#
# Example 3:
#
#
# Input: x = 100, target = 100000000
# Output: 3
# Explanation: 100 * 100 * 100 * 100.
# The expression contains 3 operations.
#
#
#
# Constraints:
#
#
# 2 <= x <= 100
# 1 <= target <= 2 * 10^8
#
#
#

# @lc tags=depth-first-search;union-find;graph

# @lc imports=start
from difflib import restore
from distutils.log import info
from re import T
from shutil import which
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个数字x与一个目标值target，四则运算得到一个目标值。没有括号。求最少的符号数。
# 所以除号的唯一作用就是产生1。
# 且由于正负号可以互换，也就是没有正负区分。
# 层次区分，就是说，对与x的1-n次幂，由大到小排列，n次幂要大于目标值。之后记录得到剩余值时，最少的操作次数。首先剩余target时，操作数为0。遍历，剩余值模除当前幂大小，之后得到商和余数，这时可以看作剩余值处在了商乘幂与商加一乘幂之间，得到两个差值，用在下一次迭代中。
# 最后使用除号得到的1，每差1，需要一个加号，一个除号。
# 最后，剪掉没用的首符号。
#
# @lc idea=end

# @lc group=power

# @lc rank=10


# @lc code=start
class Solution:

    def leastOpsExpressTarget(self, x: int, target: int) -> int:

        arr = [1]
        s = 1
        while s <= target:
            s = s * x
            arr.append(s)
        diffs = {target: 0}
        for times in range(len(arr) - 1, 0, -1):
            n = arr[times]
            diffsNew = defaultdict(lambda: inf)
            for diff, opeNum in diffs.items():
                quo, rem = divmod(diff, n)
                diffsNew[rem] = min(diffsNew[rem], opeNum + quo * times)
                if rem != 0:
                    quo, rem = quo + 1, n - rem
                    diffsNew[rem] = min(diffsNew[rem], opeNum + quo * times)
            diffs = diffsNew

        res = min(diff * 2 + opeNum for diff, opeNum in diffs.items())

        return res - 1


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('x = 3, target = 19')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().leastOpsExpressTarget(3, 19)))
    print()

    print('Example 1:')
    print('Input : ')
    print('x = 11, target = 500041')
    print('Exception :')
    print('41')
    print('Output :')
    print(str(Solution().leastOpsExpressTarget(11, 500041)))
    print()
    print('Example 1:')
    print('Input : ')
    print('x = 3, target = 365')
    print('Exception :')
    print('17')
    print('Output :')
    print(str(Solution().leastOpsExpressTarget(3, 365)))
    print()

    print('Example 2:')
    print('Input : ')
    print('x = 5, target = 501')
    print('Exception :')
    print('8')
    print('Output :')
    print(str(Solution().leastOpsExpressTarget(5, 501)))
    print()

    print('Example 3:')
    print('Input : ')
    print('x = 100, target = 100000000')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().leastOpsExpressTarget(100, 100000000)))
    print()

    pass
# @lc main=end