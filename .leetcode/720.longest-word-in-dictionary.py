# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#
# https://leetcode.com/problems/longest-word-in-dictionary/description/
#
# algorithms
# Medium (49.98%)
# Likes:    1128
# Dislikes: 1206
# Total Accepted:    98.8K
# Total Submissions: 196.6K
# Testcase Example:  '["w","wo","wor","worl","world"]'
#
# Given an array of strings words representing an English Dictionary, return
# the longest word in words that can be built one character at a time by other
# words in words.
#
# If there is more than one possible answer, return the longest word with the
# smallest lexicographical order. If there is no answer, return the empty
# string.
#
#
# Example 1:
#
#
# Input: words = ["w","wo","wor","worl","world"]
# Output: "world"
# Explanation: The word "world" can be built one character at a time by "w",
# "wo", "wor", and "worl".
#
#
# Example 2:
#
#
# Input: words = ["a","banana","app","appl","ap","apply","apple"]
# Output: "apple"
# Explanation: Both "apply" and "apple" can be built from other words in the
# dictionary. However, "apple" is lexicographically smaller than "apply".
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 30
# words[i] consists of lowercase English letters.
#
#
#

# @lc tags=hash-table;trie

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 返回最长的字母递增单词。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        res = ''
        dp = {}
        for w in words:
            f = False
            wc = w[:len(w) - 1]
            f = len(w) == 1 or (wc in dp and dp[wc])
            if f and len(w) > len(res):
                res = w
            dp[w] = f
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('words = ["w","wo","wor","worl","world"]')
    print('Exception :')
    print('"world"')
    print('Output :')
    print(str(Solution().longestWord(["w", "wo", "wor", "worl", "world"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('words = ["a","banana","app","appl","ap","apply","apple"]')
    print('Exception :')
    print('"apple"')
    print('Output :')
    print(
        str(Solution().longestWord(
            ["a", "banana", "app", "appl", "ap", "apply", "apple"])))
    print()

    pass
# @lc main=end