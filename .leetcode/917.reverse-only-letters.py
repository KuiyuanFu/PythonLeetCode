# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (61.01%)
# Likes:    1451
# Dislikes: 52
# Total Accepted:    133.9K
# Total Submissions: 219.4K
# Testcase Example:  '"ab-cd"'
#
# Given a string s, reverse the string according to the following rules:
#
#
# All the characters that are not English letters remain in the same
# position.
# All the English letters (lowercase or uppercase) should be reversed.
#
#
# Return s after reversing it.
#
#
# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
#
# Constraints:
#
#
# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.
#
#
#

# @lc tags=two-pointers;greedy

# @lc imports=start
from ctypes.wintypes import HWINSTA
from difflib import restore
from tkinter import BROWSE
from imports import *

# @lc imports=end

# @lc idea=start
#
# 反转字母。\
# 双指针。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def reverseOnlyLetters(self, s: str) -> str:

        res = list(s)
        l, r = 0, len(res) - 1
        while l < r:
            while l < r:
                if not res[l].isalpha():
                    l += 1
                else:
                    break
            while l < r:
                if not res[r].isalpha():
                    r -= 1
                else:
                    break
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
        return ''.join(res)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "ab-cd"')
    print('Exception :')
    print('"dc-ba"')
    print('Output :')
    print(str(Solution().reverseOnlyLetters("ab-cd")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "a-bC-dEf-ghIj"')
    print('Exception :')
    print('"j-Ih-gfE-dCba"')
    print('Output :')
    print(str(Solution().reverseOnlyLetters("a-bC-dEf-ghIj")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "Test1ng-Leet=code-Q!"')
    print('Exception :')
    print('"Qedo1ct-eeLg=ntse-T!"')
    print('Output :')
    print(str(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!")))
    print()

    pass
# @lc main=end