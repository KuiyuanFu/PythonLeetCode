# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (38.56%)
# Likes:    1987
# Dislikes: 233
# Total Accepted:    263.3K
# Total Submissions: 681.2K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s.
#
#
# Example 1:
#
#
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#
#
# Example 2:
#
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#
#
# Example 3:
#
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#
#
# Example 4:
#
#
# Input: pattern = "abba", s = "dog dog dog dog"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lower-case English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 模式匹配，给定一个模式，和一个字符串，字符串中有一系列单词，判断是否与模式匹配。
# 直接字典。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        pDict = {}
        wSet = set()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i, p in enumerate(pattern):
            w = words[i]
            if p not in pDict:
                pDict[p] = w
                if w in wSet:
                    return False
                wSet.add(w)
            else:
                if pDict[p] != w:
                    return False
        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('pattern = "abba", s = "dog cat cat dog"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().wordPattern("abba", "dog cat cat dog")))
    print()

    print('Example 2:')
    print('Input : ')
    print('pattern = "abba", s = "dog cat cat fish"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().wordPattern("abba", "dog cat cat fish")))
    print()

    print('Example 3:')
    print('Input : ')
    print('pattern = "aaaa", s = "dog cat cat dog"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().wordPattern("aaaa", "dog cat cat dog")))
    print()

    print('Example 4:')
    print('Input : ')
    print('pattern = "abba", s = "dog dog dog dog"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().wordPattern("abba", "dog dog dog dog")))
    print()

    pass
# @lc main=end