# @lc app=leetcode id=906 lang=python3
#
# [906] Super Palindromes
#
# https://leetcode.com/problems/super-palindromes/description/
#
# algorithms
# Hard (39.38%)
# Likes:    301
# Dislikes: 378
# Total Accepted:    21.4K
# Total Submissions: 54.4K
# Testcase Example:  '"4"\n"1000"'
#
# Let's say a positive integer is a super-palindrome if it is a palindrome, and
# it is also the square of a palindrome.
#
# Given two positive integers left and right represented as strings, return the
# number of super-palindromes integers in the inclusive range [left, right].
#
#
# Example 1:
#
#
# Input: left = "4", right = "1000"
# Output: 4
# Explanation: 4, 9, 121, and 484 are superpalindromes.
# Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a
# palindrome.
#
#
# Example 2:
#
#
# Input: left = "1", right = "2"
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= left.length, right.length <= 18
# left and right consist of only digits.
# left and right cannot have leading zeros.
# left and right represent integers in the range [1, 10^18 - 1].
# left is less than or equal to right.
#
#
#

# @lc tags=greedy

# @lc imports=start
import re
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求回文且是回文的平方的数。
# 直接暴力。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)

        def isPalin(s):
            return s == s[::-1]

        def isValid(s):
            n = int(s)
            return left <= n <= right

        def getPalin(n):
            s = str(n)
            sr = s[::-1]
            return s + sr[1:], s + sr,

        res = 0
        for n in range(1, 10**10):
            ns = getPalin(n)
            if (int(ns[0])**2) > right:
                break
            for s in ns:
                s = str(int(s)**2)
                if isPalin(s) and isValid(s):
                    res += 1
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().superpalindromesInRange("398904669", "13479046850")))
    print(str(Solution().superpalindromesInRange("1", "999999999999999999")))
    print(str(Solution().superpalindromesInRange("1", "213")))
    print('Example 1:')
    print('Input : ')
    print('left = "4", right = "1000"')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().superpalindromesInRange("4", "1000")))
    print()

    print('Example 2:')
    print('Input : ')
    print('left = "1", right = "2"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().superpalindromesInRange("1", "2")))
    print()

    pass
# @lc main=end