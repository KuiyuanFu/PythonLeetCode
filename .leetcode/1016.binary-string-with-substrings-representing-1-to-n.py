# @lc app=leetcode id=1016 lang=python3
#
# [1016] Binary String With Substrings Representing 1 To N
#
# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/description/
#
# algorithms
# Medium (57.58%)
# Likes:    282
# Dislikes: 484
# Total Accepted:    31.4K
# Total Submissions: 54.5K
# Testcase Example:  '"0110"\n3'
#
# Given a binary string s and a positive integer n, return true if the binary
# representation of all the integers in the range [1, n] are substrings of s,
# or false otherwise.
#
# A substring is a contiguous sequence of characters within a string.
#
#
# Example 1:
# Input: s = "0110", n = 3
# Output: true
# Example 2:
# Input: s = "0110", n = 4
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s[i] is either '0' or '1'.
# 1 <= n <= 10^9
#
#
#

# @lc tags=array;hash-table

# @lc imports=start
from importlib.abc import TraversableResources
from tkinter.messagebox import NO
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定二进制字符串s，再给定k，问s的字串是否包含0-k的所有数。
# 二叉树保存
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def queryString(self, s: str, n: int) -> bool:

        buf = set()
        for i in range(len(s)):

            if s[i] == '0':
                continue
            p = 1
            buf.add(p)
            for j in range(i + 1, len(s)):
                p = p * 2 + (1 if s[j] == '1' else 0)
                if p > n:
                    break
                buf.add(p)
        return len(buf) == n


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "1111000101", n = 5')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().queryString("1111000101", 5)))
    print()
    print('Example 1:')
    print('Input : ')
    print('s = "110101011011000011011111000000", n = 15')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().queryString("110101011011000011011111000000", 15)))
    print()
    print('Example 1:')
    print('Input : ')
    print('s = "0110", n = 3')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().queryString("0110", 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "0110", n = 4')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().queryString("0110", 4)))
    print()

    pass
# @lc main=end