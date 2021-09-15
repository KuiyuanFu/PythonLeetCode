# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#
# https://leetcode.com/problems/concatenated-words/description/
#
# algorithms
# Hard (43.80%)
# Likes:    1471
# Dislikes: 178
# Total Accepted:    107.8K
# Total Submissions: 247K
# Testcase Example:  '["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]'
#
# Given an array of strings words (without duplicates), return all the
# concatenated words in the given list of words.
#
# A concatenated word is defined as a string that is comprised entirely of at
# least two shorter words in the given array.
#
#
# Example 1:
#
#
# Input: words =
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
#
# Example 2:
#
#
# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 10^4
# 0 <= words[i].length <= 1000
# words[i] consists of only lowercase English letters.
# 0 <= sum(words[i].length) <= 10^5
#
#
#

# @lc tags=dynamic-programming;depth-first-search;trie

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求字符串数组中，由其他字符串拼接成的字符串。
# 前缀树，备忘录，递归。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Node:
    def __init__(self, c, isLeaf=False) -> None:
        self.c = c
        self.isLeaf = isLeaf
        self.d = {}
        pass


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        root = Node('')
        res = []
        buffer = {}

        def recur(s):
            if s in buffer:
                return buffer[s]
            res = False
            p = root
            if len(s) == 0:
                res = p.isLeaf
            else:
                for i, c in enumerate(s):
                    if c in p.d:
                        p = p.d[c]
                        if p.isLeaf:
                            if i == len(s) - 1:
                                res = 1
                            else:
                                res = recur(s[i + 1:])
                                if res == 1:
                                    res = 2
                            if res:
                                break
                    else:
                        break

            buffer[s] = res
            return res

        for w in words:
            p = root
            for c in w:
                if c not in p.d:
                    p.d[c] = Node(c)
                p = p.d[c]
            p.isLeaf = True
        for w in words:
            if recur(w) == 2:
                res.append(w)
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'words =["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]'
    )
    print('Exception :')
    print('["catsdogcats","dogcatsdog","ratcatdogcat"]')
    print('Output :')
    print(
        str(Solution().findAllConcatenatedWordsInADict([
            "cat", "cats", "catsdogcats", "dog", "dogcatsdog",
            "hippopotamuses", "rat", "ratcatdogcat"
        ])))
    print()

    print('Example 2:')
    print('Input : ')
    print('words = ["cat","dog","catdog"]')
    print('Exception :')
    print('["catdog"]')
    print('Output :')
    print(
        str(Solution().findAllConcatenatedWordsInADict(
            ["cat", "dog", "catdog"])))
    print()

    pass
# @lc main=end