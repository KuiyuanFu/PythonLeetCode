# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (50.94%)
# Likes:    3802
# Dislikes: 163
# Total Accepted:    176.5K
# Total Submissions: 344.4K
# Testcase Example:  '"aab"'
#
# Given a string s, rearrange the characters of s so that any two adjacent
# characters are not the same.
#
# Return any possible rearrangement of s or return "" if not possible.
#
#
# Example 1:
# Input: s = "aab"
# Output: "aba"
# Example 2:
# Input: s = "aaab"
# Output: ""
#
#
# Constraints:
#
#
# 1 <= s.length <= 500
# s consists of lowercase English letters.
#
#
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 使相邻两个字符不相同。
# 排序，判断是否合法。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = [None] * len(s)
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        l = []
        for c in d:
            n = d[c]
            l.append((-n, c))
        l.sort()
        if -l[0][0] * 2 - 1 > len(s):
            return ''
        l = ''.join([c * (-n) for n, c in l])

        idx = 0
        for c in l:
            res[idx] = c
            idx += 2
            if idx >= len(res):
                idx = 1
        return ''.join(res)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "aab"')
    print('Exception :')
    print('"aba"')
    print('Output :')
    print(str(Solution().reorganizeString("aab")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "aaab"')
    print('Exception :')
    print('""')
    print('Output :')
    print(str(Solution().reorganizeString("aaab")))
    print()

    pass
# @lc main=end