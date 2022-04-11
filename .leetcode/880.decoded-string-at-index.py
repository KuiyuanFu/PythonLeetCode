# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#
# https://leetcode.com/problems/decoded-string-at-index/description/
#
# algorithms
# Medium (28.28%)
# Likes:    1141
# Dislikes: 186
# Total Accepted:    33.1K
# Total Submissions: 117K
# Testcase Example:  '"leet2code3"\n10'
#
# You are given an encoded string s. To decode the string to a tape, the
# encoded string is read one character at a time and the following steps are
# taken:
#
#
# If the character read is a letter, that letter is written onto the tape.
# If the character read is a digit d, the entire current tape is repeatedly
# written d - 1 more times in total.
#
#
# Given an integer k, return the k^th letter (1-indexed) in the decoded
# string.
#
#
# Example 1:
#
#
# Input: s = "leet2code3", k = 10
# Output: "o"
# Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
# The 10^th letter in the string is "o".
#
#
# Example 2:
#
#
# Input: s = "ha22", k = 5
# Output: "h"
# Explanation: The decoded string is "hahahaha".
# The 5^th letter is "h".
#
#
# Example 3:
#
#
# Input: s = "a2345678999999999999999", k = 1
# Output: "a"
# Explanation: The decoded string is "a" repeated 8301530446056247680 times.
# The 1^st letter is "a".
#
#
#
# Constraints:
#
#
# 2 <= s.length <= 100
# s consists of lowercase English letters and digits 2 through 9.
# s starts with a letter.
# 1 <= k <= 10^9
# It is guaranteed that k is less than or equal to the length of the decoded
# string.
# The decoded string is guaranteed to have less than 2^63 letters.
#
#
#

# @lc tags=segment-tree;line-sweep

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 解码字符串，返回第k个值。
# 统计长度，达到长度后，反向计算字母。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        for i, c in enumerate(s):
            if c.isdigit():
                length *= int(c)
            else:
                length += 1
            if length >= k:

                for c in reversed(s[:i + 1]):
                    if c.isalpha():
                        if k % length == 0:
                            return c
                        else:
                            length -= 1
                    else:
                        length //= int(c)
                        k = k % length

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "leet2code3", k = 10')
    print('Exception :')
    print('"o"')
    print('Output :')
    print(str(Solution().decodeAtIndex("leet2code3", 10)))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "ha22", k = 5')
    print('Exception :')
    print('"h"')
    print('Output :')
    print(str(Solution().decodeAtIndex("ha22", 5)))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "a2345678999999999999999", k = 1')
    print('Exception :')
    print('"a"')
    print('Output :')
    print(str(Solution().decodeAtIndex("a2345678999999999999999", 1)))
    print()

    print('"a"')
    print('Output :')
    print(str(Solution().decodeAtIndex("a23", 6)))
    print()

    pass
# @lc main=end