# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#
# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
#
# algorithms
# Easy (65.54%)
# Likes:    897
# Dislikes: 137
# Total Accepted:    96.2K
# Total Submissions: 146.7K
# Testcase Example:  '"this apple is sweet"\n"this apple is sour"'
#
# A sentence is a string of single-space separated words where each word
# consists only of lowercase letters.
#
# A word is uncommon if it appears exactly once in one of the sentences, and
# does not appear in the other sentence.
#
# Given two sentences s1 and s2, return a list of all the uncommon words. You
# may return the answer in any order.
#
#
# Example 1:
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:
# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]
#
#
# Constraints:
#
#
# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.
#
#
#

# @lc tags=breadth-first-search;graph

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 返回不寻常的字符串，给定两个句子，若一个单词在一个句子中只出现一次，且不在另一句子中出现，就是不寻常的。
# Counter 统计个数，遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d1 = Counter(s1.split(' '))
        d2 = Counter(s2.split(' '))
        res = []
        for d1, d2 in [(d1, d2), (d2, d1)]:
            for pair in d1.items():
                k, v = pair
                if v == 1 and k not in d2:
                    res.append(k)
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s1 = "this apple is sweet", s2 = "this apple is sour"')
    print('Exception :')
    print('["sweet","sour"]')
    print('Output :')
    print(
        str(Solution().uncommonFromSentences("this apple is sweet",
                                             "this apple is sour")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s1 = "apple apple", s2 = "banana"')
    print('Exception :')
    print('["banana"]')
    print('Output :')
    print(str(Solution().uncommonFromSentences("apple apple", "banana")))
    print()

    pass
# @lc main=end