# @lc app=leetcode id=522 lang=python3
#
# [522] Longest Uncommon Subsequence II
#
# https://leetcode.com/problems/longest-uncommon-subsequence-ii/description/
#
# algorithms
# Medium (39.73%)
# Likes:    333
# Dislikes: 980
# Total Accepted:    40.1K
# Total Submissions: 100.8K
# Testcase Example:  '["aba","cdc","eae"]'
#
# Given an array of strings strs, return the length of the longest uncommon
# subsequence between them. If the longest uncommon subsequence does not exist,
# return -1.
#
# An uncommon subsequence between an array of strings is a string that is a
# subsequence of one string but not the others.
#
# A subsequence of a string s is a string that can be obtained after deleting
# any number of characters from s.
#
#
# For example, "abc" is a subsequence of "aebdc" because you can delete the
# underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc"
# include "aebdc", "aeb", and "" (empty string).
#
#
#
# Example 1:
# Input: strs = ["aba","cdc","eae"]
# Output: 3
# Example 2:
# Input: strs = ["aaa","aaa","aa"]
# Output: -1
#
#
# Constraints:
#
#
# 2 <= strs.length <= 50
# 1 <= strs[i].length <= 10
# strs[i] consists of lowercase English letters.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 一组字符串的最长非公共子字符串长度。
# 以长度排序。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSub(sub, str):
            if len(sub) > len(str):
                return False
            idx, length = 0, len(str)
            for sc in sub:
                while idx < length:
                    if str[idx] == sc:
                        break
                    idx += 1
                if idx == length:
                    return False
                idx += 1
            return True

        strs.sort(key=lambda e: (-len(e), e))
        l = 0
        length = len(strs)
        s = set()
        while l < length:
            str = strs[l]
            r = l + 1
            while r < length and strs[r] == str:
                r += 1
            if l + 1 != r:
                s.add(str)
                l = r
                continue

            f = True
            for strS in s:
                if isSub(str, strS):
                    f = False
                    break
            if f:
                return len(str)
            l += 1
        return -1
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('strs = ["aba","cdc","eae"]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findLUSlength(["aba", "cdc", "eae"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('strs = ["aaa","aaa","aa"]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().findLUSlength(["aaa", "aaa", "aa"])))
    print()

    pass
# @lc main=end