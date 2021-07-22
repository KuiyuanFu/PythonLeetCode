# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (55.51%)
# Likes:    1379
# Dislikes: 88
# Total Accepted:    130.5K
# Total Submissions: 235.1K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# Given a string array words, return the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. If no such
# two words exist, return 0.
#
#
# Example 1:
#
#
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
#
#
# Example 2:
#
#
# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
#
#
# Example 3:
#
#
# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.
#
#
#
# Constraints:
#
#
# 2 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# words[i] consists only of lowercase English letters.
#
#
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一系列单词，求没有相同字母的两个单词的长度乘积的最大值。
# 使用位信号，记录出现的字符，之后记录每个位信号最大的长度，之后二重循环遍历每一对组合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        from collections import defaultdict
        kl = defaultdict(int)
        for word in words:
            k = 0
            for c in word:
                k = k | 2**(ord(c) - ord('a'))
            kl[k] = max(kl[k], len(word))
        keys = list(kl)
        res = 0
        for i in range(len(keys)):
            ki = keys[i]
            for j in range(i + 1, len(keys)):
                kj = keys[j]
                if ki & kj == 0:
                    res = max(res, kl[ki] * kl[kj])

        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('words = ["abcw","baz","foo","bar","xtfn","abcdef"]')
    print('Exception :')
    print('16')
    print('Output :')
    print(
        str(Solution().maxProduct(
            ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('words = ["a","ab","abc","d","cd","bcd","abcd"]')
    print('Exception :')
    print('4')
    print('Output :')
    print(
        str(Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd",
                                   "abcd"])))
    print()

    print('Example 3:')
    print('Input : ')
    print('words = ["a","aa","aaa","aaaa"]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maxProduct(["a", "aa", "aaa", "aaaa"])))
    print()

    pass
# @lc main=end