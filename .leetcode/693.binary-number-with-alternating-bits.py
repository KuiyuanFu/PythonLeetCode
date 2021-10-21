# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (60.40%)
# Likes:    756
# Dislikes: 98
# Total Accepted:    82.9K
# Total Submissions: 137.1K
# Testcase Example:  '5'
#
# Given a positive integer, check whether it has alternating bits: namely, if
# two adjacent bits will always have different values.
#
#
# Example 1:
#
#
# Input: n = 5
# Output: true
# Explanation: The binary representation of 5 is: 101
#
#
# Example 2:
#
#
# Input: n = 7
# Output: false
# Explanation: The binary representation of 7 is: 111.
#
# Example 3:
#
#
# Input: n = 11
# Output: false
# Explanation: The binary representation of 11 is: 1011.
#
# Example 4:
#
#
# Input: n = 10
# Output: true
# Explanation: The binary representation of 10 is: 1010.
#
# Example 5:
#
#
# Input: n = 3
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断给定数字的二进制表示中零一是交错的。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        s = bin(n)[2:]
        return s.count('11') + s.count('00') == 0
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().hasAlternatingBits(5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 7')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().hasAlternatingBits(7)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 11')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().hasAlternatingBits(11)))
    print()

    print('Example 4:')
    print('Input : ')
    print('n = 10')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().hasAlternatingBits(10)))
    print()

    print('Example 5:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().hasAlternatingBits(3)))
    print()

    pass
# @lc main=end