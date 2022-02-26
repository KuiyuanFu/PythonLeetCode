# @lc app=leetcode id=833 lang=python3
#
# [833] Find And Replace in String
#
# https://leetcode.com/problems/find-and-replace-in-string/description/
#
# algorithms
# Medium (54.14%)
# Likes:    749
# Dislikes: 735
# Total Accepted:    98.2K
# Total Submissions: 181.1K
# Testcase Example:  '"abcd"\n[0, 2]\n["a", "cd"]\n["eee", "ffff"]'
#
# You are given a 0-indexed string s that you must perform k replacement
# operations on. The replacement operations are given as three 0-indexed
# parallel arrays, indices, sources, and targets, all of length k.
#
# To complete the i^th replacement operation:
#
#
# Check if the substring sources[i] occurs at index indices[i] in the original
# string s.
# If it does not occur, do nothing.
# Otherwise if it does occur, replace that substring with targets[i].
#
#
# For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i]
# = "eee", then the result of this replacement will be "eeecd".
#
# All replacement operations must occur simultaneously, meaning the replacement
# operations should not affect the indexing of each other. The testcases will
# be generated such that the replacements will not overlap.
#
#
# For example, a testcase with s = "abc", indices = [0, 1], and sources =
# ["ab","bc"] will not be generated because the "ab" and "bc" replacements
# overlap.
#
#
# Return the resulting string after performing all replacement operations on
# s.
#
# A substring is a contiguous sequence of characters in a string.
#
#
# Example 1:
#
#
# Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee",
# "ffff"]
# Output: "eeebffff"
# Explanation:
# "a" occurs at index 0 in s, so we replace it with "eee".
# "cd" occurs at index 2 in s, so we replace it with "ffff".
#
#
# Example 2:
#
#
# Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets =
# ["eee","ffff"]
# Output: "eeecd"
# Explanation:
# "ab" occurs at index 0 in s, so we replace it with "eee".
# "ec" does not occur at index 2 in s, so we do nothing.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# k == indices.length == sources.length == targets.length
# 1 <= k <= 100
# 0 <= indexes[i] < s.length
# 1 <= sources[i].length, targets[i].length <= 50
# s consists of only lowercase English letters.
# sources[i] and targets[i] consist of only lowercase English letters.
#
#
#

# @lc tags=breadth-first-search

# @lc imports=start
from textwrap import indent
from imports import *

# @lc imports=end

# @lc idea=start
#
# 替换字符串，垃圾题。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str],
                          targets: List[str]) -> str:
        n = len(indices)

        operations = []

        for idxInOpe in range(n):
            i = indices[idxInOpe]
            l = len(sources[idxInOpe])
            if s[i:i + l] == sources[idxInOpe]:
                operations.append((i, l, targets[idxInOpe]))

        operations.sort()

        res = []

        pre = 0
        for i, l, t in operations:
            res.append(s[pre:i])
            res.append(t)
            pre = i + l
        res.append(s[pre:])

        return ''.join(res)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        's = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee","ffff"]'
    )
    print('Exception :')
    print('"eeebffff"')
    print('Output :')
    print(
        str(Solution().findReplaceString("abcd", [0, 2], ["a", "cd"],
                                         ["eee", "ffff"])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        's = "abcd", indices = [0, 2], sources = ["ab","ec"], targets =["eee","ffff"]'
    )
    print('Exception :')
    print('"eeecd"')
    print('Output :')
    print(
        str(Solution().findReplaceString("abcd", [0, 2], ["ab", "ec"],
                                         ["eee", "ffff"])))
    print()

    pass
# @lc main=end