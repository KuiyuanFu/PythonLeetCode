# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#
# https://leetcode.com/problems/to-lower-case/description/
#
# algorithms
# Easy (80.74%)
# Likes:    855
# Dislikes: 2143
# Total Accepted:    307.2K
# Total Submissions: 380.1K
# Testcase Example:  '"Hello"'
#
# Given a string s, return the string after replacing every uppercase letter
# with the same lowercase letter.
#
#
# Example 1:
#
#
# Input: s = "Hello"
# Output: "hello"
#
#
# Example 2:
#
#
# Input: s = "here"
# Output: "here"
#
#
# Example 3:
#
#
# Input: s = "LOVELY"
# Output: "lovely"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 100
# s consists of printable ASCII characters.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 换小写。
# ASCII 加减。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def toLowerCase(self, s: str) -> str:

        return ''.join(
            chr(ord(c) - ord('A') + ord('a')) if 'A' <= c <= 'Z' else c
            for c in s)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "Hello"')
    print('Exception :')
    print('"hello"')
    print('Output :')
    print(str(Solution().toLowerCase("Hello")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "here"')
    print('Exception :')
    print('"here"')
    print('Output :')
    print(str(Solution().toLowerCase("here")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "LOVELY"')
    print('Exception :')
    print('"lovely"')
    print('Output :')
    print(str(Solution().toLowerCase("LOVELY")))
    print()

    pass
# @lc main=end