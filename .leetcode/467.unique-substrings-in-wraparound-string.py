# @lc app=leetcode id=467 lang=python3
#
# [467] Unique Substrings in Wraparound String
#
# https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/
#
# algorithms
# Medium (36.68%)
# Likes:    888
# Dislikes: 118
# Total Accepted:    31.8K
# Total Submissions: 86.6K
# Testcase Example:  '"a"'
#
# We define the string s to be the infinite wraparound string of
# "abcdefghijklmnopqrstuvwxyz", so s will look like this:
#
#
# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
#
#
# Given a string p, return the number of unique non-empty substrings of p are
# present in s.
#
#
# Example 1:
#
#
# Input: p = "a"
# Output: 1
# Explanation: Only the substring "a" of p is in s.
#
#
# Example 2:
#
#
# Input: p = "cac"
# Output: 2
# Explanation: There are two substrings ("a", "c") of p in s.
#
#
# Example 3:
#
#
# Input: p = "zab"
# Output: 6
# Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab")
# of p in s.
#
#
#
# Constraints:
#
#
# 1 <= p.length <= 10^5
# p consists of lowercase English letters.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 统计给定的字符串的子字符串有多少种是无限循环字符串的子字符串。
# 直接统计以每个字符开始的最长合法子字符串。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        orda = ord('a')
        p = [ord(c) - orda for c in p]
        p.append(-2)
        buffer = [0] * 26
        pc = -2
        start = pc
        length = 0
        for c in p:
            if pc == (c - 1 + 26) % 26:
                length += 1
            else:
                while buffer[start] < length:
                    buffer[start] = length
                    start = (start + 1) % 26
                    length -= 1
                length = 1
                start = c
            pc = c
        return sum(buffer)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('p = "a"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findSubstringInWraproundString("a")))
    print()

    print('Example 2:')
    print('Input : ')
    print('p = "cac"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findSubstringInWraproundString("cac")))
    print()

    print('Example 3:')
    print('Input : ')
    print('p = "zab"')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().findSubstringInWraproundString("zab")))
    print()

    pass
# @lc main=end