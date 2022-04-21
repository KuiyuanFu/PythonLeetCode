# @lc app=leetcode id=893 lang=python3
#
# [893] Groups of Special-Equivalent Strings
#
# https://leetcode.com/problems/groups-of-special-equivalent-strings/description/
#
# algorithms
# Medium (70.51%)
# Likes:    431
# Dislikes: 1386
# Total Accepted:    41K
# Total Submissions: 58.2K
# Testcase Example:  '["abcd","cdab","cbad","xyzz","zzxy","zzyx"]'
#
# You are given an array of strings of the same length words.
#
# In one move, you can swap any two even indexed characters or any two odd
# indexed characters of a string words[i].
#
# Two strings words[i] and words[j] are special-equivalent if after any number
# of moves, words[i] == words[j].
#
#
# For example, words[i] = "zzxy" and words[j] = "xyzz" are special-equivalent
# because we may make the moves "zzxy" -> "xzzy" -> "xyzz".
#
#
# A group of special-equivalent strings from words is a non-empty subset of
# words such that:
#
#
# Every pair of strings in the group are special equivalent, and
# The group is the largest size possible (i.e., there is not a string words[i]
# not in the group such that words[i] is special-equivalent to every string in
# the group).
#
#
# Return the number of groups of special-equivalent strings from words.
#
#
# Example 1:
#
#
# Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
# Output: 3
# Explanation:
# One group is ["abcd", "cdab", "cbad"], since they are all pairwise special
# equivalent, and none of the other strings is all pairwise special equivalent
# to these.
# The other two groups are ["xyzz", "zzxy"] and ["zzyx"].
# Note that in particular, "zzxy" is not special equivalent to "zzyx".
#
#
# Example 2:
#
#
# Input: words = ["abc","acb","bac","bca","cab","cba"]
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 20
# words[i] consist of lowercase English letters.
# All the strings are of the same length.
#
#
#

# @lc tags=tree;depth-first-search;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定字符串数组，每个字符串上的奇数位置元素可以与同样奇数位置元素互换，偶数同样。
# 求所有可以经互换相等的组的个数。
# 直接奇偶分组，排序，组合。之后集合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def numSpecialEquivGroups(self, words: List[str]) -> int:

        def getKey(s: str):

            return ''.join(sorted(s[0::2])) + ''.join(sorted(s[1::2]))

        keys = set(getKey(w) for w in words)
        return len(keys)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]')
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().numSpecialEquivGroups(
            ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('words = ["abc","acb","bac","bca","cab","cba"]')
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().numSpecialEquivGroups(
            ["abc", "acb", "bac", "bca", "cab", "cba"])))
    print()

    pass
# @lc main=end