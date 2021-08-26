# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (49.38%)
# Likes:    2932
# Dislikes: 130
# Total Accepted:    134.5K
# Total Submissions: 272.1K
# Testcase Example:  '"ABAB"\n2'
#
# You are given a string s and an integer k. You can choose any character of
# the string and change it to any other uppercase English character. You can
# perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can
# get after performing the above operations.
#
#
# Example 1:
#
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
#
#
# Example 2:
#
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length
#
#
#

# @lc tags=two-pointers;sliding-window

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定字符串，在给定一个最大改变次数，求能得到的最长子字符串，满足字符相同。
# 滑动窗口。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        d = defaultdict(int)
        res = 0
        kn = 0
        pre, r = ' ', -1
        length = len(s)
        for l, c in enumerate(s):
            if c != pre:
                pre = c
                kn = (r - l + 1) - d[c]
                while r + 1 < length:
                    rt = r + 1
                    if s[rt] != pre:
                        kn += 1
                    if kn <= k:
                        d[s[rt]] += 1
                        r = rt
                    else:
                        break
            d[c] -= 1
            rest = r - l + 1
            if r + 1 == length:
                rest += min(k - kn, l)
            res = max(res, rest)

        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "ABAB", k = 2')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().characterReplacement("ABAB", 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "AABABBA", k = 1')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().characterReplacement("AABABBA", 1)))
    print()

    print('Exception :')
    print('4')
    print(str(Solution().characterReplacement("ABBB", 2)))

    pass
# @lc main=end