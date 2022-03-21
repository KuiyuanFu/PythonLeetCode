# @lc app=leetcode id=854 lang=python3
#
# [854] K-Similar Strings
#
# https://leetcode.com/problems/k-similar-strings/description/
#
# algorithms
# Hard (39.16%)
# Likes:    788
# Dislikes: 47
# Total Accepted:    31.3K
# Total Submissions: 79.8K
# Testcase Example:  '"ab"\n"ba"'
#
# Strings s1 and s2 are k-similar (for some non-negative integer k) if we can
# swap the positions of two letters in s1 exactly k times so that the resulting
# string equals s2.
#
# Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are
# k-similar.
#
#
# Example 1:
#
#
# Input: s1 = "ab", s2 = "ba"
# Output: 1
#
#
# Example 2:
#
#
# Input: s1 = "abc", s2 = "bca"
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= s1.length <= 20
# s2.length == s1.length
# s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd',
# 'e', 'f'}.
# s2 is an anagram of s1.
#
#
#

# @lc tags=depth-first-search

# @lc imports=start
from mimetypes import init
from imports import *

# @lc imports=end

# @lc idea=start
#
# k similar，就是一个字符串经过k次两个字母互换，可以变成另一个字符串。
# 求最少的k值。
# 直接暴力迭代。
#
# @lc idea=end

# @lc group=depth-first-search

# @lc rank=9


# @lc code=start
class Solution:
    def kSimilarity(self, s: str, t: str) -> int:
        def generateNewSAndT():
            sn, tn = [], []
            for i in range(len(s)):
                if s[i] == t[i]:
                    continue
                sn.append(ord(s[i]) - ord('a'))
                tn.append(ord(t[i]) - ord('a'))
            return sn, tn

        s, t = generateNewSAndT()

        def removeStepOne(s, t):

            dp = {}
            for i in range(len(s)):
                sc, tc = s[i], t[i]
                dp[sc * 6 + tc] = i
                if tc * 6 + sc in dp:
                    si, ti = dp[tc * 6 + sc], i
                    if si < ti:
                        sn = s[:si] + s[si + 1:ti] + s[ti + 1:]
                        tn = t[:si] + t[si + 1:ti] + t[ti + 1:]
                        return True, sn, tn
                    else:
                        sn = s[:ti] + s[ti + 1:si] + s[si + 1:]
                        tn = t[:ti] + t[ti + 1:si] + t[si + 1:]
                        return True, sn, tn
            return False, s, t

        step = 0

        while True:
            f, s, t = removeStepOne(s, t)
            if not f:
                break
            step += 1

        length = len(s)

        def recur(idx):
            if idx == length:
                return 0
            if s[idx] == t[idx]:
                return recur(idx + 1)
            res = length
            for i in range(idx + 1, length):
                if t[i] == s[idx]:
                    t[idx], t[i] = t[i], t[idx]
                    res = min(res, recur(idx + 1))
                    t[idx], t[i] = t[i], t[idx]
            return 1 + res

        return step + recur(0)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s1 = "ab", s2 = "ba"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().kSimilarity("ab", "ba")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s1 = "abc", s2 = "bca"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().kSimilarity("abc", "bca")))
    print()
    print('Example 2:')
    print('Input : ')
    print('s1 = "abccaacceecdeea" "bcaacceeccdeaae"')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().kSimilarity("abccaacceecdeea", "bcaacceeccdeaae")))
    print()

    print(
        str(Solution().kSimilarity("abcdefabcdefabcdef",
                                   "edcfbebceafcfdabad")))
    print(
        str(Solution().kSimilarity("babcccabcbcbcbbaaabb",
                                   "bbcbabbaaacccacbbbcb")))
    pass
# @lc main=end