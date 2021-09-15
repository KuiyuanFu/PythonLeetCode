# @lc app=leetcode id=466 lang=python3
#
# [466] Count The Repetitions
#
# https://leetcode.com/problems/count-the-repetitions/description/
#
# algorithms
# Hard (28.81%)
# Likes:    251
# Dislikes: 230
# Total Accepted:    13.2K
# Total Submissions: 45.8K
# Testcase Example:  '"acb"\n4\n"ab"\n2'
#
# We define str = [s, n] as the string str which consists of the string s
# concatenated n times.
#
#
# For example, str == ["abc", 3] =="abcabcabc".
#
#
# We define that string s1 can be obtained from string s2 if we can remove some
# characters from s2 such that it becomes s1.
#
#
# For example, s1 = "abc" can be obtained from s2 = "abdbec" based on our
# definition by removing the bolded underlined characters.
#
#
# You are given two strings s1 and s2 and two integers n1 and n2. You have the
# two strings str1 = [s1, n1] and str2 = [s2, n2].
#
# Return the maximum integer m such that str = [str2, m] can be obtained from
# str1.
#
#
# Example 1:
# Input: s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
# Output: 2
# Example 2:
# Input: s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
# Output: 1
#
#
# Constraints:
#
#
# 1 <= s1.length, s2.length <= 100
# s1 and s2 consist of lowercase English letters.
# 1 <= n1, n2 <= 10^6
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 问一个字符串删除元素后的子字符串中，最多包含多少个另一个字符串。
# 找循环。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        ss1, ss2 = set(s1), set(s2)
        for c in ss2:
            if c not in ss1:
                return 0
        cors = {}
        c1, c2, i, j = 0, 0, 0, 0
        m = [0]
        f = True
        while c1 < n1:
            t = (i, j)
            if f and t in cors:
                c1p, c2p = cors[t]
                t1, t2 = c1 - c1p, c2 - c2p
                # 剩余还有多少循环
                n = ((n1 - c1 - 1) // t1)
                c1 += n * t1
                c2 += n * t2
                f = False
            cors[t] = (c1, c2)
            if s1[i] == s2[j]:
                j += 1
                if j == len(s2):
                    c2 += 1
                    j = 0
                m[-1] = c2
            i += 1
            if i == len(s1):
                c1 += 1
                i = 0
                m.append(m[-1])
        return c2 // n2
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s1 = "acb", n1 = 4, s2 = "ab", n2 = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().getMaxRepetitions("acb", 4, "ab", 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('s1 = "acb", n1 = 1, s2 = "acb", n2 = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().getMaxRepetitions("acb", 1, "acb", 1)))
    print()
    print('"aaa" 3 " aa"1')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().getMaxRepetitions("aaa", 3, "aa", 1)))
    print()
    print('"aaa"20"aaaaa"1')
    print('Exception :')
    print('12')
    print('Output :')
    print(str(Solution().getMaxRepetitions("aaa", 20, "aaaaa", 1)))
    print()
    print('Exception :')
    print('2')
    print(str(Solution().getMaxRepetitions("bacaba", 3, "abacab", 1)))
    print()
    print('Exception :')
    print('3')
    print(str(Solution().getMaxRepetitions("nlhqgllunmelayl", 2, "lnl", 1)))
    pass
# @lc main=end