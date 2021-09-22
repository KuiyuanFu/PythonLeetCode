# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#
# https://leetcode.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (49.88%)
# Likes:    720
# Dislikes: 1930
# Total Accepted:    128.5K
# Total Submissions: 257.6K
# Testcase Example:  '"abcdefg"\n2'
#
# Given a string s and an integer k, reverse the first k characters for every
# 2k characters counting from the start of the string.
#
# If there are fewer than k characters left, reverse all of them. If there are
# less than 2k but greater than or equal to k characters, then reverse the
# first k characters and left the other as original.
#
#
# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of only lowercase English letters.
# 1 <= k <= 10^4
#
#
#

# @lc tags=string

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
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        for l in range(0, len(s), 2 * k):
            res.append(s[l:l + k][::-1])
            res.append(s[l + k:l + 2 * k])
        return ''.join(res)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abcdefg", k = 2')
    print('Exception :')
    print('"bacdfeg"')
    print('Output :')
    print(str(Solution().reverseStr("abcdefg", 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "abcd", k = 2')
    print('Exception :')
    print('"bacd"')
    print('Output :')
    print(str(Solution().reverseStr("abcd", 2)))
    print()
    print(str(Solution().reverseStr("a", 1)))
    pass
# @lc main=end