# @lc app=leetcode id=1003 lang=python3
#
# [1003] Check If Word Is Valid After Substitutions
#
# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/description/
#
# algorithms
# Medium (58.16%)
# Likes:    698
# Dislikes: 450
# Total Accepted:    45.2K
# Total Submissions: 77.8K
# Testcase Example:  '"aabcbc"'
#
# Given a string s, determine if it is valid.
#
# A string s is valid if, starting with an empty string t = "", you can
# transform t into s after performing the following operation any number of
# times:
#
#
# Insert string "abc" into any position in t. More formally, t becomes tleft +
# "abc" + tright, where t == tleft + tright. Note that tleft and tright may be
# empty.
#
#
# Return true if s is a valid string, otherwise, return false.
#
#
# Example 1:
#
#
# Input: s = "aabcbc"
# Output: true
# Explanation:
# "" -> "abc" -> "aabcbc"
# Thus, "aabcbc" is valid.
#
# Example 2:
#
#
# Input: s = "abcabcababcc"
# Output: true
# Explanation:
# "" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
# Thus, "abcabcababcc" is valid.
#
#
# Example 3:
#
#
# Input: s = "abccba"
# Output: false
# Explanation: It is impossible to get "abccba" using the operation.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^4
# s consists of letters 'a', 'b', and 'c'
#
#
#

# @lc tags=math;geometry

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断一个字符串是否合法，及由空字符串开始任意位置插入 abc 字符串，迭代多次。
# 栈
#
# @lc idea=end

# @lc group=

# @lc rank=10


# @lc code=start
class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == 'a':
                stack.append('a')
            elif c == 'b':
                if len(stack) == 0 or stack[-1] != 'a':
                    return False
                stack.append('b')
            else:
                if len(stack) < 2 or stack[-1] != 'b' or stack[-2] != 'a':
                    return False
                stack.pop()
                stack.pop()

        return len(stack) == 0

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "aabcbc"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isValid("aabcbc")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "abcabcababcc"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isValid("abcabcababcc")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "abccba"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isValid("abccba")))
    print()

    pass
# @lc main=end