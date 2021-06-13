# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (40.77%)
# Likes:    2129
# Dislikes: 485
# Total Accepted:    370.1K
# Total Submissions: 906.1K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to
# get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character, but a character may map to itself.
#
#
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
# Input: s = "paper", t = "title"
# Output: true
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s and t consist of any valid ascii character.
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个字符串，判断时候可以相互转化，规则为同一字符必须转换到相同的字符，且每个字符只能被转化一次。
# 先记录源每个字符出现的位置，之后看目标中对应位置字符是否相同，再看是否不同字符的位置不同。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        from collections import defaultdict
        dict = defaultdict(list)
        for i, c in enumerate(s):
            dict[c].append(i)
        chars = set()
        for c in dict.keys():
            ls = [t[i] for i in dict[c]]
            ct = ls[0]
            chars.add(ct)
            if ls.count(ct) != len(ls):
                return False
        if len(chars) != len(dict):
            return False
        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "egg", t = "add"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isIsomorphic("egg", "add")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "foo", t = "bar"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isIsomorphic("foo", "bar")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "paper", t = "title"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isIsomorphic("paper", "title")))
    print()

    pass
# @lc main=end