# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (26.36%)
# Likes:    1212
# Dislikes: 1460
# Total Accepted:    203.4K
# Total Submissions: 771K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string s and an array of strings words of the same length.
# Return all starting indices of substring(s) in s that is a concatenation of
# each word in words exactly once, in any order, and without any intervening
# characters.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
#
#
# Example 2:
#
#
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
#
#
# Example 3:
#
#
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of lower-case English letters.
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# words[i] consists of lower-case English letters.
#
#
#
#
#

# @lc tags=hash-table;two-pointers;string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定了一个字符串，和一个字符串数组，返回字符串中，用这一系列相同长度的词组成的字符串的首字符索引值。
# 用一个字典存储当前窗口内的单词及个数，每次间隔单词的长度来修改当前单词对应的数量。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        wordLength = len(words[0])

        # 不够位数
        if len(s) < len(words) * wordLength:
            return result

        d = {}
        for w in words:
            d[w] = d.get(w, 0) + 1

        target = len(d)
        # 子字符串的首位索引与最后一个词的首字符索引的差值
        lengthSum = (len(words) - 1) * wordLength
        for i in range(wordLength):
            dCopy = d.copy()
            j = i
            now = 0
            while j + wordLength <= len(s):
                # 在内且等于0，说明这一个词在这正好满足个数了，计数器加一
                word = s[j:j + wordLength]
                if word in dCopy:
                    dCopy[word] -= 1
                    if dCopy[word] == 0:
                        now += 1
                if now == target:
                    result.append(j - lengthSum)
                # 在内且等于1，说明这一个词在这正好不满足个数了，计数器减一

                if j - lengthSum >= 0:
                    wordOld = s[j - lengthSum:j - lengthSum + wordLength]
                    if wordOld in dCopy:
                        dCopy[wordOld] += 1
                        if dCopy[wordOld] == 1:
                            now -= 1
                j += wordLength

        return result


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "barfoothefoobarman", words = ["foo","bar"]')
    print('Output :')
    print(str(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])))
    print('Exception :')
    print('[0,9]')
    print()

    print('Example 2:')
    print('Input : ')
    print(
        's = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]'
    )
    print('Output :')
    print(
        str(Solution().findSubstring("wordgoodgoodgoodbestword",
                                     ["word", "good", "best", "word"])))
    print('Exception :')
    print('[]')
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]')
    print('Output :')
    print(
        str(Solution().findSubstring("barfoofoobarthefoobarman",
                                     ["bar", "foo", "the"])))
    print('Exception :')
    print('[6,9,12]')
    print()

    pass
# @lc main=end