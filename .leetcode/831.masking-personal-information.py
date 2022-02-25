# @lc app=leetcode id=831 lang=python3
#
# [831] Masking Personal Information
#
# https://leetcode.com/problems/masking-personal-information/description/
#
# algorithms
# Medium (45.73%)
# Likes:    114
# Dislikes: 394
# Total Accepted:    14K
# Total Submissions: 30.5K
# Testcase Example:  '"LeetCode@LeetCode.com"'
#
# You are given a personal information string s, representing either an email
# address or a phone number. Return the masked personal information using the
# below rules.
#
# Email address:
#
# An email address is:
#
#
# A name consisting of uppercase and lowercase English letters, followed by
# The '@' symbol, followed by
# The domain consisting of uppercase and lowercase English letters with a dot
# '.' somewhere in the middle (not the first or last character).
#
#
# To mask an email:
#
#
# The uppercase letters in the name and domain must be converted to lowercase
# letters.
# The middle letters of the name (i.e., all but the first and last letters)
# must be replaced by 5 asterisks "*****".
#
#
# Phone number:
#
# A phone number is formatted as follows:
#
#
# The phone number contains 10-13 digits.
# The last 10 digits make up the local number.
# The remaining 0-3 digits, in the beginning, make up the country code.
# Separation characters from the set {'+', '-', '(', ')', ' '} separate the
# above digits in some way.
#
#
# To mask a phone number:
#
#
# Remove all separation characters.
# The masked phone number should have the form:
#
# "***-***-XXXX" if the country code has 0 digits.
# "+*-***-***-XXXX" if the country code has 1 digit.
# "+**-***-***-XXXX" if the country code has 2 digits.
# "+***-***-***-XXXX" if the country code has 3 digits.
#
#
# "XXXX" is the last 4 digits of the local number.
#
#
#
# Example 1:
#
#
# Input: s = "LeetCode@LeetCode.com"
# Output: "l*****e@leetcode.com"
# Explanation: s is an email address.
# The name and domain are converted to lowercase, and the middle of the name is
# replaced by 5 asterisks.
#
#
# Example 2:
#
#
# Input: s = "AB@qq.com"
# Output: "a*****b@qq.com"
# Explanation: s is an email address.
# The name and domain are converted to lowercase, and the middle of the name is
# replaced by 5 asterisks.
# Note that even though "ab" is 2 characters, it still must have 5 asterisks in
# the middle.
#
#
# Example 3:
#
#
# Input: s = "1(234)567-890"
# Output: "***-***-7890"
# Explanation: s is a phone number.
# There are 10 digits, so the local number is 10 digits and the country code is
# 0 digits.
# Thus, the resulting masked number is "***-***-7890".
#
#
#
# Constraints:
#
#
# s is either a valid email or a phone number.
# If s is an email:
#
# 8 <= s.length <= 40
# s consists of uppercase and lowercase English letters and exactly one '@'
# symbol and '.' symbol.
#
#
# If s is a phone number:
#
# 10 <= s.length <= 20
# s consists of digits, spaces, and the symbols '(', ')', '-', and
# '+'.
#
#
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 按照规则隐藏信息。
# 垃圾题。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            return s[0] + '*****' + s[s.index('@') - 1:]
        else:

            s = ''.join(c if c.isdigit() else '' for c in s)
            l = len(s)
            pre = (('+' + ('*' * (l - 10)) + '-') if l > 10 else '')
            return pre + '***-***-' + s[-4:]
            pass

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "LeetCode@LeetCode.com"')
    print('Exception :')
    print('"l*****e@leetcode.com"')
    print('Output :')
    print(str(Solution().maskPII("LeetCode@LeetCode.com")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "AB@qq.com"')
    print('Exception :')
    print('"a*****b@qq.com"')
    print('Output :')
    print(str(Solution().maskPII("AB@qq.com")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "1(234)567-890"')
    print('Exception :')
    print('"***-***-7890"')
    print('Output :')
    print(str(Solution().maskPII("1(234)567-890")))
    print(str(Solution().maskPII("11(234)567-890")))
    print(str(Solution().maskPII("111(234)567-890")))
    print(str(Solution().maskPII("1111(234)567-890")))
    print()

    pass
# @lc main=end