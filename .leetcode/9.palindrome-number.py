# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (50.02%)
# Likes:    3205
# Dislikes: 1725
# Total Accepted:    1.2M
# Total Submissions: 2.4M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward. For
# example, 121 is palindrome while 123 is not.
#
#
# Example 1:
#
#
# Input: x = 121
# Output: true
#
#
# Example 2:
#
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Example 4:
#
#
# Input: x = -101
# Output: false
#
#
#
# Constraints:
#
#
# -2^31 <= x <= 2^31 - 1
#
#
#
# Follow up: Could you solve it without converting the integer to a string?
#
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断数字是否是回文.
# 根据题意，负数一定不是，正数情况下，正常是需要依次求余来确定每一位的数字的，这里直接使用 itoa 来确定字符串，直接比较，很方便。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        s = str(x)
        left = 0
        right = len(s) - 1
        while left < right:
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1

        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('x = 121')
    print('Output :')
    print(str(Solution().isPalindrome(121)))
    print('Exception :')
    print('true')
    print()

    print('Example 2:')
    print('Input : ')
    print('x = -121')
    print('Output :')
    print(str(Solution().isPalindrome(-121)))
    print('Exception :')
    print('false')
    print()

    print('Example 3:')
    print('Input : ')
    print('x = 10')
    print('Output :')
    print(str(Solution().isPalindrome(10)))
    print('Exception :')
    print('false')
    print()

    print('Example 4:')
    print('Input : ')
    print('x = -101')
    print('Output :')
    print(str(Solution().isPalindrome(-101)))
    print('Exception :')
    print('false')
    print()

    pass
# @lc main=end