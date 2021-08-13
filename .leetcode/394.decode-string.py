# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (53.83%)
# Likes:    5660
# Dislikes: 256
# Total Accepted:    359.3K
# Total Submissions: 665.9K
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example,
# there won't be input like 3a or 2[4].
#
#
# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
#
#
# Constraints:
#
#
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets
# '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].
#
#
#

# @lc tags=stack;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 解码一个压缩的字符串。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        b, n = '', 0
        for c in s:
            if c == '[':
                stack.append((b, n))
                b, n = '', 0
                pass
            elif c == ']':
                bt, nt = stack.pop()
                b, n = bt + b * nt, 0
                pass
            elif '0' <= c <= '9':
                n = n * 10 + int(c)
            else:
                b += c
        return b


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "3[a]2[bc]"')
    print('Exception :')
    print('"aaabcbc"')
    print('Output :')
    print(str(Solution().decodeString("3[a]2[bc]")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "3[a2[c]]"')
    print('Exception :')
    print('"accaccacc"')
    print('Output :')
    print(str(Solution().decodeString("3[a2[c]]")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "2[abc]3[cd]ef"')
    print('Exception :')
    print('"abcabccdcdcdef"')
    print('Output :')
    print(str(Solution().decodeString("2[abc]3[cd]ef")))
    print()

    print('Example 4:')
    print('Input : ')
    print('s = "abc3[cd]xyz"')
    print('Exception :')
    print('"abccdcdcdxyz"')
    print('Output :')
    print(str(Solution().decodeString("abc3[cd]xyz")))
    print()

    pass
# @lc main=end