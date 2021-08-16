# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (44.00%)
# Likes:    2994
# Dislikes: 285
# Total Accepted:    132K
# Total Submissions: 299.7K
# Testcase Example:  '"aaabb"\n3'
#
# Given a string s and an integer k, return the length of the longest substring
# of s such that the frequency of each character in this substring is greater
# than or equal to k.
#
#
# Example 1:
#
#
# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
#
#
# Example 2:
#
#
# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and
# 'b' is repeated 3 times.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of only lowercase English letters.
# 1 <= k <= 10^5
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定字母序列，再给定一个个数k，求最长的子序列，满足子序列中所有字符的重复个数大于等于k。
# 使用滑动窗口，如果直接使用滑动窗口，无法确定何时停下来，考虑每一个子序列的字符种类是固定的，所以每次指定一个字符种类个数，来确定滑动窗口。
#
# @lc idea=end

# @lc group=sliding-window

# @lc rank=10


# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        ts = set()
        t = 0
        for c in s:
            if c not in ts:
                t += 1
                ts.add(c)
        td = defaultdict(int)
        res = 0
        ss = list(enumerate(s))
        for nt in range(1, t + 1):
            td.clear()
            nk = 0
            nn = 0
            l = 0
            for r, c in ss:

                tdcv = td[c] + 1
                td[c] = tdcv
                # new char
                if tdcv == 1:
                    nn += 1

                # satisfy k
                if tdcv == k:
                    nk += 1

                # count is to much
                while nn > nt:
                    slv = s[l]
                    tdslv = td[slv] - 1
                    td[slv] = tdslv
                    if tdslv == 0:
                        td.pop(slv)
                        nn -= 1
                    if tdslv == k - 1:
                        nk -= 1
                    l += 1

                # satisfy nt
                if nk == nt:
                    res = max(res, r - l + 1)
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "aaabb", k = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().longestSubstring("aaabb", 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "ababbc", k = 2')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().longestSubstring("ababbc", 2)))
    print()

    pass
# @lc main=end