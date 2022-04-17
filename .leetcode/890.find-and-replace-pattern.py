# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#
# https://leetcode.com/problems/find-and-replace-pattern/description/
#
# algorithms
# Medium (75.60%)
# Likes:    1792
# Dislikes: 117
# Total Accepted:    97.1K
# Total Submissions: 128.5K
# Testcase Example:  '["abc","deq","mee","aqq","dkd","ccc"]\n"abb"'
#
# Given a list of strings words and a string pattern, return a list of words[i]
# that match pattern. You may return the answer in any order.
#
# A word matches the pattern if there exists a permutation of letters p so that
# after replacing every letter x in the pattern with p(x), we get the desired
# word.
#
# Recall that a permutation of letters is a bijection from letters to letters:
# every letter maps to another letter, and no two letters map to the same
# letter.
#
#
# Example 1:
#
#
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a ->
# m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a
# permutation, since a and b map to the same letter.
#
#
# Example 2:
#
#
# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]
#
#
#
# Constraints:
#
#
# 1 <= pattern.length <= 20
# 1 <= words.length <= 50
# words[i].length == pattern.length
# pattern and words[i] are lowercase English letters.
#
#
#

# @lc tags=greedy

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 获得匹配模式的字符串。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def findAndReplacePattern(self, words: List[str],
                              pattern: str) -> List[str]:
        orda = ord('a')

        def getPattern(s: str):
            mapList = [None] * 26
            res = [None] * len(s)
            nowCharOrd = orda
            for i, c in enumerate(s):
                idx = ord(c) - orda
                if (mapList[idx] is None):
                    mapList[idx] = chr(nowCharOrd + orda)
                    nowCharOrd += 1
                res[i] = mapList[idx]
            return ''.join(res)

        targetPattern = getPattern(pattern)

        res = []

        for word in words:
            if getPattern(word) == targetPattern:
                res.append(word)
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"')
    print('Exception :')
    print('["mee","aqq"]')
    print('Output :')
    print(
        str(Solution().findAndReplacePattern(
            ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb")))
    print()

    print('Example 2:')
    print('Input : ')
    print('words = ["a","b","c"], pattern = "a"')
    print('Exception :')
    print('["a","b","c"]')
    print('Output :')
    print(str(Solution().findAndReplacePattern(["a", "b", "c"], "a")))
    print()

    pass
# @lc main=end