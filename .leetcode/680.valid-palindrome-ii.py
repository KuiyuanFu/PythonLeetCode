# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (37.61%)
# Likes:    3368
# Dislikes: 204
# Total Accepted:    331.5K
# Total Submissions: 875.9K
# Testcase Example:  '"aba"'
#
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.
#
#
# Example 1:
#
#
# Input: s = "aba"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
#
#
# Example 3:
#
#
# Input: s = "abc"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
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
# 判断字符串至多删除一个元素后是否为回文。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def recur(s):
            length = len(s)
            if length < 2:
                return True
            m = (length + 1) // 2
            return s[:m] == s[-1:-(m + 1):-1]

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return recur(s[l:r]) or recur(s[l + 1:r + 1])

        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "aba"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().validPalindrome("aba")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "abca"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().validPalindrome("abca")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "abc"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().validPalindrome("abc")))
    print()
    print(str(Solution().validPalindrome("deeee")))
    pass
# @lc main=end