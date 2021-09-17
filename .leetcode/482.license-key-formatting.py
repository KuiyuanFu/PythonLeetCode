# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#
# https://leetcode.com/problems/license-key-formatting/description/
#
# algorithms
# Easy (43.15%)
# Likes:    659
# Dislikes: 950
# Total Accepted:    182.3K
# Total Submissions: 422.3K
# Testcase Example:  '"5F3Z-2e-9-w"\n4'
#
# You are given a license key represented as a string s that consists of only
# alphanumeric characters and dashes. The string is separated into n + 1 groups
# by n dashes. You are also given an integer k.
#
# We want to reformat the string s such that each group contains exactly k
# characters, except for the first group, which could be shorter than k but
# still must contain at least one character. Furthermore, there must be a dash
# inserted between two groups, and you should convert all lowercase letters to
# uppercase.
#
# Return the reformatted license key.
#
#
# Example 1:
#
#
# Input: s = "5F3Z-2e-9-w", k = 4
# Output: "5F3Z-2E9W"
# Explanation: The string s has been split into two parts, each part has 4
# characters.
# Note that the two extra dashes are not needed and can be removed.
#
#
# Example 2:
#
#
# Input: s = "2-5g-3-J", k = 2
# Output: "2-5G-3J"
# Explanation: The string s has been split into three parts, each part has 2
# characters except the first part as it could be shorter as mentioned
# above.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of English letters, digits, and dashes '-'.
# 1 <= k <= 10^4
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 格式化密钥。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        idx = (len(s) - s.count('-')) % k
        res = []
        if idx != 0:
            res.append('')
        for c in s:
            if c == '-':
                continue
            if c.islower():
                c = c.upper()
            if idx == 0:
                res.append('')
                idx = k
            res[-1] += c
            idx -= 1
        return '-'.join(res)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "5F3Z-2e-9-w", k = 4')
    print('Exception :')
    print('"5F3Z-2E9W"')
    print('Output :')
    print(str(Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "2-5g-3-J", k = 2')
    print('Exception :')
    print('"2-5G-3J"')
    print('Output :')
    print(str(Solution().licenseKeyFormatting("2-5g-3-J", 2)))
    print()
    print(str(Solution().licenseKeyFormatting("2-4A0r7-4k", 3)))
    pass
# @lc main=end