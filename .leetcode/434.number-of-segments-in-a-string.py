# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#
# https://leetcode.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (37.78%)
# Likes:    342
# Dislikes: 902
# Total Accepted:    99.8K
# Total Submissions: 264K
# Testcase Example:  '"Hello, my name is John"'
#
# You are given a string s, return the number of segments in the string.
#
# A segment is defined to be a contiguous sequence of non-space characters.
#
#
# Example 1:
#
#
# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
#
#
# Example 2:
#
#
# Input: s = "Hello"
# Output: 1
#
#
# Example 3:
#
#
# Input: s = "love live! mu'sic forever"
# Output: 4
#
#
# Example 4:
#
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 300
# s consists of lower-case and upper-case English letters, digits or one of the
# following characters "!@#$%^&*()_+-=',.:".
# The only space character in s is ' '.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求给定字符出可以被空格分成几段。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "Hello, my name is John"')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().countSegments("Hello, my name is John")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "Hello"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().countSegments("Hello")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "love live! mu\'sic forever"')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().countSegments("love live! mu'sic forever")))
    print()

    print('Example 4:')
    print('Input : ')
    print('s = ""')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().countSegments("")))
    print()

    pass
# @lc main=end