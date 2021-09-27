# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (44.70%)
# Likes:    3213
# Dislikes: 88
# Total Accepted:    224K
# Total Submissions: 502.2K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of
# s2.
#
#
# Example 1:
#
#
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
#
# Example 2:
#
#
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
#
#
#

# @lc tags=two-pointers;sliding-window

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断s1的排列是否是s2的一个子字符串。
# 滑动窗口。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1d = defaultdict(int)

        for c in s1:
            s1d[c] += 1
        n = len(s1d.keys())
        for i in range(len(s1) - 1):
            c = s2[i]
            s1d[c] -= 1
            if s1d[c] == 0:
                n -= 1
        for i in range(len(s1) - 1, len(s2)):
            c = s2[i]
            s1d[c] -= 1
            if s1d[c] == 0:
                n -= 1
            if n == 0:
                return True
            cl = s2[i - len(s1) + 1]
            s1d[cl] += 1
            if s1d[cl] == 1:
                n += 1
        return False
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s1 = "ab", s2 = "eidbaooo"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().checkInclusion("ab", "eidbaooo")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s1 = "ab", s2 = "eidboaoo"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().checkInclusion("ab", "eidboaoo")))
    print()

    pass
# @lc main=end