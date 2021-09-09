# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (43.44%)
# Likes:    2746
# Dislikes: 262
# Total Accepted:    208.5K
# Total Submissions: 480.1K
# Testcase Example:  '"abab"'
#
# Given a string s, check if it can be constructed by taking a substring of it
# and appending multiple copies of the substring together.
#
#
# Example 1:
#
#
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
#
#
# Example 2:
#
#
# Input: s = "aba"
# Output: false
#
#
# Example 3:
#
#
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc"
# twice.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of lowercase English letters.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断一个字符串，是否由子字符串重复而成。
# 根据位置是否整除和字母是否等于第一个来确定可能重复字符串，之后再用字符串与重复后的字符串比较。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        cf = s[0]
        for i in range(1, length):
            c = s[i]
            if length % i != 0 or c != cf:
                continue
            if s == s[:i] * (length // i):
                return True
        return False

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abab"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().repeatedSubstringPattern("abab")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "aba"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().repeatedSubstringPattern("aba")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "abcabcabcabc"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().repeatedSubstringPattern("abcabcabcabc")))
    print()

    pass
# @lc main=end