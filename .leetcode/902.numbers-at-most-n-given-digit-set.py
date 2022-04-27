# @lc app=leetcode id=902 lang=python3
#
# [902] Numbers At Most N Given Digit Set
#
# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/description/
#
# algorithms
# Hard (40.89%)
# Likes:    1043
# Dislikes: 88
# Total Accepted:    35.4K
# Total Submissions: 86.5K
# Testcase Example:  '["1","3","5","7"]\n100'
#
# Given an array of digits which is sorted in non-decreasing order. You can
# write numbers using each digits[i] as many times as we want. For example, if
# digits = ['1','3','5'], we may write numbers such as '13', '551', and
# '1351315'.
#
# Return the number of positive integers that can be generated that are less
# than or equal to a given integer n.
#
#
# Example 1:
#
#
# Input: digits = ["1","3","5","7"], n = 100
# Output: 20
# Explanation:
# The 20 numbers that can be written are:
# 1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
#
#
# Example 2:
#
#
# Input: digits = ["1","4","9"], n = 1000000000
# Output: 29523
# Explanation:
# We can write 3 one digit numbers, 9 two digit numbers, 27 three digit
# numbers,
# 81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
# 2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit
# numbers.
# In total, this is 29523 integers that can be written using the digits
# array.
#
#
# Example 3:
#
#
# Input: digits = ["7"], n = 8
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= digits.length <= 9
# digits[i].length == 1
# digits[i] is a digit from '1' to '9'.
# All the values in digits are unique.
# digits is sorted in non-decreasing order.
# 1 <= n <= 10^9
#
#
#

# @lc tags=dynamic-programming;heap

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 组合个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:

        ns = [c for c in str(n)]
        length = len(ns)
        digitsCounts = len(digits)

        res = sum(digitsCounts**i for i in range(1, length))

        for idx, n in enumerate(ns):
            tailCount = length - 1 - idx
            digitsIdx = bisect_left(digits, n)
            # all lesser
            if digitsIdx == digitsCounts:
                res += digitsCounts * digitsCounts**tailCount
                break
            else:
                res += digitsIdx * digitsCounts**tailCount

                if n == digits[digitsIdx]:
                    if idx == length - 1:
                        res += 1
                else:
                    break

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('digits = ["1","3","5","7"], n = 100')
    print('Exception :')
    print('20')
    print('Output :')
    print(str(Solution().atMostNGivenDigitSet(["1", "3", "5", "7"], 100)))
    print()

    print('Example 2:')
    print('Input : ')
    print('digits = ["1","4","9"], n = 1000000000')
    print('Exception :')
    print('29523')
    print('Output :')
    print(str(Solution().atMostNGivenDigitSet(["1", "4", "9"], 1000000000)))
    print()

    print('Example 3:')
    print('Input : ')
    print('digits = ["7"], n = 8')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().atMostNGivenDigitSet(["7"], 8)))
    print()

    pass
# @lc main=end