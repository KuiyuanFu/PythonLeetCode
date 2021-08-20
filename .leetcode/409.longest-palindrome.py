# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (52.48%)
# Likes:    1843
# Dislikes: 117
# Total Accepted:    216.5K
# Total Submissions: 412.4K
# Testcase Example:  '"abccccdd"'
#
# Given a string s which consists of lowercase or uppercase letters, return the
# length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome
# here.
#
#
# Example 1:
#
#
# Input: s = "abccccdd"
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#
#
# Example 2:
#
#
# Input: s = "a"
# Output: 1
#
#
# Example 3:
#
#
# Input: s = "bb"
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断给定的字符串组成的回文的最长长度。
# 就是判断重复对数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:

        d = defaultdict(bool)
        n = 0
        for c in s:
            if d[c] == True:
                n += 2
            d[c] = not d[c]

        if len(s) - n > 0:
            n += 1
        return n
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abccccdd"')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().longestPalindrome("abccccdd")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "a"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().longestPalindrome("a")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "bb"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().longestPalindrome("bb")))
    print()

    pass
# @lc main=end