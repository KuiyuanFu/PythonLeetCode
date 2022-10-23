# @lc app=leetcode id=1017 lang=python3
#
# [1017] Convert to Base -2
#
# https://leetcode.com/problems/convert-to-base-2/description/
#
# algorithms
# Medium (60.90%)
# Likes:    399
# Dislikes: 254
# Total Accepted:    21K
# Total Submissions: 34.5K
# Testcase Example:  '2'
#
# Given an integer n, return a binary string representing its representation in
# base -2.
#
# Note that the returned string should not have leading zeros unless the string
# is "0".
#
#
# Example 1:
#
#
# Input: n = 2
# Output: "110"
# Explantion: (-2)^2 + (-2)^1 = 2
#
#
# Example 2:
#
#
# Input: n = 3
# Output: "111"
# Explantion: (-2)^2 + (-2)^1 + (-2)^0 = 3
#
#
# Example 3:
#
#
# Input: n = 4
# Output: "100"
# Explantion: (-2)^2 = 4
#
#
#
# Constraints:
#
#
# 0 <= n <= 10^9
#
#
#

# @lc tags=dynamic-programming;stack;ordered-map

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一个数转化为-2进制。
# 进位
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def baseNeg2(self, n: int) -> str:

        res = []

        l = list(map(int, reversed(bin(n)[2:])))
        i = 0
        while i < len(l):
            n = l[i]
            r = 0
            if n >= 2:
                r = n // 2
                n = n % 2
            res.append(n)
            if i % 2 == 1 and n != 0:
                r += 1
            i += 1
            if r != 0:
                if i == len(l):
                    l.append(0)
                l[i] += r
        return ''.join(map(str, reversed(res)))
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('"110"Explantion: (-2)^2 + (-2)^1 = 2')
    print('Output :')
    print(str(Solution().baseNeg2(2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('"111"Explantion: (-2)^2 + (-2)^1 + (-2)^0 = 3')
    print('Output :')
    print(str(Solution().baseNeg2(3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('"100"Explantion: (-2)^2 = 4')
    print('Output :')
    print(str(Solution().baseNeg2(4)))
    print()

    pass
# @lc main=end