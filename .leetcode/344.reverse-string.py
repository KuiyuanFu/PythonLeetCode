# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (71.54%)
# Likes:    2732
# Dislikes: 808
# Total Accepted:    1.1M
# Total Submissions: 1.6M
# Testcase Example:  '["h","e","l","l","o"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters s.
#
#
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s[i] is a printable ascii character.
#
#
#
# Follow up: Do not allocate extra space for another array. You must do this by
# modifying the input array in-place with O(1) extra memory.
#
#

# @lc tags=two-pointers;string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 翻转字符串。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
        return s


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = ["h","e","l","l","o"]')
    print('Exception :')
    print('["o","l","l","e","h"]')
    print('Output :')
    print(str(Solution().reverseString(["h", "e", "l", "l", "o"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = ["H","a","n","n","a","h"]')
    print('Exception :')
    print('["h","a","n","n","a","H"]')
    print('Output :')
    print(str(Solution().reverseString(["H", "a", "n", "n", "a", "h"])))
    print()

    pass
# @lc main=end