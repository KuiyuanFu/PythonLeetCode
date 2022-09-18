# @lc app=leetcode id=984 lang=python3
#
# [984] String Without AAA or BBB
#
# https://leetcode.com/problems/string-without-aaa-or-bbb/description/
#
# algorithms
# Medium (42.93%)
# Likes:    573
# Dislikes: 341
# Total Accepted:    37.1K
# Total Submissions: 86.4K
# Testcase Example:  '1\n2'
#
# Given two integers a and b, return any string s such that:
#
#
# s has length a + b and contains exactly a 'a' letters, and exactly b 'b'
# letters,
# The substring 'aaa' does not occur in s, and
# The substring 'bbb' does not occur in s.
#
#
#
# Example 1:
#
#
# Input: a = 1, b = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
#
#
# Example 2:
#
#
# Input: a = 4, b = 1
# Output: "aabaa"
#
#
#
# Constraints:
#
#
# 0 <= a, b <= 100
# It is guaranteed such an s exists for the given a and b.
#
#
#

# @lc tags=depth-first-search;union-find

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定a，b的个数，求符合要求的字符串。不能有三个连续相同字符。
# 那个多先分配那个，直接计算差值，也就是aab的对数，之后看是否平均。若平均直接ab，否者直接加上剩余数量的多数字符。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def strWithout3a3b(self, a: int, b: int) -> str:

        res = ''

        if a > b:
            d = min(a - b, b)
            res += 'aab' * d
            a, b = a - 2 * d, b - d
        elif b > a:
            d = min(b - a, a)
            res += 'bba' * d
            a, b = a - d, b - 2 * d
        if a == b:
            res += 'ab' * a
        else:
            if a > b:
                res += 'a' * a
            else:
                res += 'b' * b
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('a = 1, b = 2')
    print('Exception :')
    print('"abb"')
    print('Output :')
    print(str(Solution().strWithout3a3b(1, 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('a = 4, b = 1')
    print('Exception :')
    print('"aabaa"')
    print('Output :')
    print(str(Solution().strWithout3a3b(4, 1)))
    print()

    pass
# @lc main=end