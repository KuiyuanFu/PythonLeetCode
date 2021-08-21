# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (49.45%)
# Likes:    2240
# Dislikes: 438
# Total Accepted:    358.4K
# Total Submissions: 715.2K
# Testcase Example:  '"11"\n"123"'
#
# Given two non-negative integers, num1 and num2 represented as string, return
# the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library for handling
# large integers (such as BigInteger). You must also not convert the inputs to
# integers directly.
#
#
# Example 1:
#
#
# Input: num1 = "11", num2 = "123"
# Output: "134"
#
#
# Example 2:
#
#
# Input: num1 = "456", num2 = "77"
# Output: "533"
#
#
# Example 3:
#
#
# Input: num1 = "0", num2 = "0"
# Output: "0"
#
#
#
# Constraints:
#
#
# 1 <= num1.length, num2.length <= 10^4
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 字符串数字求和。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l = max(len(num1), len(num2)) + 1
        res = [None] * l
        num1, num2 = num1.zfill(l), num2.zfill(l)
        cb = 0
        zord2 = 2 * ord('0')
        for i in reversed(range(l)):
            n = ord(num1[i]) + ord(num2[i]) - zord2 + cb
            cb = n // 10
            res[i] = str(n % 10)

        if res[0] == '0':
            return ''.join(res[1:])
        else:
            return ''.join(res)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num1 = "11", num2 = "123"')
    print('Exception :')
    print('"134"')
    print('Output :')
    print(str(Solution().addStrings("11", "123")))
    print()

    print('Example 2:')
    print('Input : ')
    print('num1 = "456", num2 = "77"')
    print('Exception :')
    print('"533"')
    print('Output :')
    print(str(Solution().addStrings("456", "77")))
    print()

    print('Example 3:')
    print('Input : ')
    print('num1 = "0", num2 = "0"')
    print('Exception :')
    print('"0"')
    print('Output :')
    print(str(Solution().addStrings("0", "0")))
    print()

    pass
# @lc main=end