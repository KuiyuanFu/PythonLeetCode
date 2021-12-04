# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (49.19%)
# Likes:    2378
# Dislikes: 129
# Total Accepted:    108.4K
# Total Submissions: 216.8K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given a string s and an array of strings words, return the number of words[i]
# that is a subsequence of s.
#
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
#
#
# For example, "ace" is a subsequence of "abcde".
#
#
#
# Example 1:
#
#
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s:
# "a", "acd", "ace".
#
#
# Example 2:
#
#
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.
#
#
#

# @lc tags=binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 子序列个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        length = len(s)

        buffer = {}

        def valid(sub):
            if sub in buffer:
                return buffer[sub]
            res = True
            idx = 0
            for c in sub:
                while idx < length and s[idx] != c:
                    idx += 1
                if idx == length:
                    res = False
                    break
                idx += 1
            buffer[sub] = res
            return res

        return list(map(valid, words)).count(True)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abcde", words = ["a","bb","acd","ace"]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().numMatchingSubseq("abcde",
                                           ["a", "bb", "acd", "ace"])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        's = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().numMatchingSubseq(
            "dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"])))
    print()

    pass
# @lc main=end