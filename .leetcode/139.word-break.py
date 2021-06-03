# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (42.23%)
# Likes:    6766
# Dislikes: 320
# Total Accepted:    773.6K
# Total Submissions: 1.8M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
#
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start

from unittest import result
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个字符串s，和一个字典wordDict，判断s是否可以由wordDict中的词组成。
# 直接备忘录递归。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def recur(self, s: str):
        if len(s) == 0:
            return True
        if s in self.mem:
            return self.mem[s]
        result = False

        for i in range(1, min(len(s), 20) + 1):
            sub = s[:i]
            if sub in self.wordDict[i - 1] and self.recur(s[i:]):
                result = True
                break
        self.mem[s] = result
        return result
        pass

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.mem = {}
        self.wordDict = [set() for _ in range(20)]
        for word in wordDict:
            self.wordDict[len(word) - 1].add(word)
        return self.recur(s)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "leetcode", wordDict = ["leet","code"]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().wordBreak("leetcode", ["leet", "code"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "applepenapple", wordDict = ["apple","pen"]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().wordBreak("applepenapple", ["apple", "pen"])))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]')
    print('Exception :')
    print('false')
    print('Output :')
    print(
        str(Solution().wordBreak("catsandog",
                                 ["cats", "dog", "sand", "and", "cat"])))
    print()

    pass
# @lc main=end