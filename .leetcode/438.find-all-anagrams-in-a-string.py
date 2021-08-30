# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (46.01%)
# Likes:    4784
# Dislikes: 211
# Total Accepted:    388.3K
# Total Submissions: 843K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
#
#
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
# Example 2:
#
#
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#
#
# Constraints:
#
#
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求字符串s中，与字符串p字符组成相同的索引。
# 滑动窗口。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        d = defaultdict(int)
        for c in p:
            d[c] += 1
        n = len(d.keys())
        l = len(p) - 1
        for i, c in enumerate(s):
            t = d[c] - 1
            d[c] = t
            if t == 0:
                n -= 1
            p = i - l
            if n == 0:
                res.append(p)
            if p >= 0:
                c = s[p]
                t = d[c] + 1
                d[c] = t
                if t == 1:
                    n += 1
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "cbaebabacd", p = "abc"')
    print('Exception :')
    print('[0,6]')
    print('Output :')
    print(str(Solution().findAnagrams("cbaebabacd", "abc")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "abab", p = "ab"')
    print('Exception :')
    print('[0,1,2]')
    print('Output :')
    print(str(Solution().findAnagrams("abab", "ab")))
    print()

    pass
# @lc main=end