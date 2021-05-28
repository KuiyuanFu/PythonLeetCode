# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (38.65%)
# Likes:    2027
# Dislikes: 3878
# Total Accepted:    872K
# Total Submissions: 2.2M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string s, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
#
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#
#

# @lc tags=two-pointers;string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个字符串，判断其是否为回文。
# 直接左右双指针。忽略其他字符。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if l < r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "A man, a plan, a canal: Panama"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPalindrome("A man, a plan, a canal: Panama")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "race a car"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPalindrome("race a car")))
    print()

    pass
# @lc main=end