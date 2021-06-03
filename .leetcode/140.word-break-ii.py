# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (36.24%)
# Likes:    3250
# Dislikes: 445
# Total Accepted:    331.2K
# Total Submissions: 912.5K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a string s and a dictionary of strings wordDict, add spaces in s to
# construct a sentence where each word is a valid dictionary word. Return all
# such possible sentences in any order.
#
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
#
#
# Example 1:
#
#
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
#
#
# Example 2:
#
#
# Input: s = "pineapplepenapple", wordDict =
# ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
#
#
#

# @lc tags=dynamic-programming;backtracking

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个字符串s，和一个字典wordDict，求s由wordDict中的词组成的分割，以空格分割。
# 直接备忘录递归。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def recur(self, s: str):
        if len(s) == 0:
            return ['']
        if s in self.mem:
            return self.mem[s]
        results = []

        for i in range(1, min(len(s), 20) + 1):
            sub = s[:i]
            if sub in self.wordDict[i - 1]:
                rs = self.recur(s[i:])
                for r in rs:
                    result = sub + ' ' + r
                    results.append(result.strip())

        self.mem[s] = results
        return results
        pass

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
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
    print('s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]')
    print('Exception :')
    print('["cats and dog","cat sand dog"]')
    print('Output :')
    print(
        str(Solution().wordBreak("catsanddog",
                                 ["cat", "cats", "and", "sand", "dog"])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        's = "pineapplepenapple", wordDict =["apple","pen","applepen","pine","pineapple"]'
    )
    print('Exception :')
    print(
        '["pine apple pen apple","pineapple pen apple","pine applepen apple"]')
    print('Output :')
    print(
        str(Solution().wordBreak(
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"])))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(
        str(Solution().wordBreak("catsandog",
                                 ["cats", "dog", "sand", "and", "cat"])))
    print()

    pass
# @lc main=end