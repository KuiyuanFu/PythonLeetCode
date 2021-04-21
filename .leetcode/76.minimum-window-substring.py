# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (36.26%)
# Likes:    6444
# Dislikes: 436
# Total Accepted:    524.5K
# Total Submissions: 1.4M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t, return the minimum window in s which will contain
# all the characters in t. If there is no such window in s that covers all
# characters in t, return the empty string "".
#
# Note that If there is such a window, it is guaranteed that there will always
# be only one unique minimum window in s.
#
#
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 10^5
# s and t consist of English letters.
#
#
#
# Follow up: Could you find an algorithm that runs in O(n) time?
#

# @lc tags=hash-table;two-pointers;string;sliding-window

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个字符串，满足第一个字符串包含所有第二个字符串中的字符。
# 求第一个字符串中最短的字串，满足包含所有第二个字符串中的字符。
# 滑动窗口。
# @lc idea=end

# @lc group=sliding-window

# @lc rank=5


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # t 中字符个数统计
        chars = {}
        for c in t:
            chars[c] = chars.get(c,0)+1

        l = 0
        number = len(chars.keys())
        result = ''

        # 依次遍历
        for r in range(len(s)):
            # 如果在内，说明这个字符是有效的
            if s[r] in chars:
                chars[s[r]] -= 1
                # 说明这个字符个数已经满足了
                if chars[s[r]] == 0:
                    number -= 1
                # 所有字符都已经满足了
                if number == 0:
                    # 移除左侧多余字符的边界条件
                    while number != 1:
                        if s[l] in chars:
                            chars[s[l]] += 1
                            if chars[s[l]] == 1:
                                number += 1
                            # 达到边界条件
                            if number == 1:
                                t = s[l:r + 1]
                                # 判断是否是最短的
                                if len(result) == 0 or len(result) > len(t):
                                    result = t
                        l += 1
        return result
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    print('Example 1:')
    print('Input : ')
    print('s = "ADOBECODEBANC", t = "ABC"')
    print('Output :')
    print(str(Solution().minWindow("ADOBECODEBANC", "ABC")))
    print('Exception :')
    print('"BANC"')
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "a", t = "a"')
    print('Output :')
    print(str(Solution().minWindow("a", "a")))
    print('Exception :')
    print('"a"')
    print()

    pass
# @lc main=end