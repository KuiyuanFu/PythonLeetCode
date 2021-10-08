# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (63.36%)
# Likes:    5179
# Dislikes: 144
# Total Accepted:    329.3K
# Total Submissions: 518.4K
# Testcase Example:  '"abc"'
#
# Given a string s, return the number of palindromic substrings in it.
#
# A string is a palindrome when it reads the same backward as forward.
#
# A substring is a contiguous sequence of characters within the string.
#
#
# Example 1:
#
#
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
# Example 2:
#
#
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
#
#
#

# @lc tags=string;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求回文子字符串的个数。
# 直接遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)

        def p(l, r):
            res = 0
            while l >= 0 and r < length:
                if s[l] == s[r]:
                    res += 1
                else:
                    break
                l, r = l - 1, r + 1
            return res

        res = 0
        for i in range(len(s)):
            res += p(i, i)
            res += p(i, i + 1)

        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abc"')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().countSubstrings("abc")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "aaa"')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().countSubstrings("aaa")))
    print()

    pass
# @lc main=end