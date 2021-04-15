#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (47.27%)
# Likes:    2688
# Dislikes: 338
# Total Accepted:    590.6K
# Total Submissions: 1.2M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
#
#
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
#
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
#
#
#
#
#
# @lc idea=start
#
# 二进制串求和，正序。
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if len(a) < len(b):
            a, b = b, a
        result = [0] * len(a)
        mod = 0
        for i in range(-1, - len(b) - 1, -1):
            t = ord(a[i]) - 48 + ord(b[i]) - 48 + mod
            result[i] = str(t % 2)
            mod = t // 2

        for i in range(-len(b) - 1, -len(a) - 1, -1):
            t = ord(a[i]) - 48 + mod
            result[i] = str(t % 2)
            mod = t // 2

        if mod == 1:
           result = ['1'] + result
        return ''.join(result)


# @lc code=end
if __name__ == '__main__':
    print(Solution().addBinary("11",  "1"))
    print(Solution().addBinary("1010", "1011"))

