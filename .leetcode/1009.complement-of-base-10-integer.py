# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#
# https://leetcode.com/problems/complement-of-base-10-integer/description/
#
# algorithms
# Easy (62.02%)
# Likes:    1642
# Dislikes: 83
# Total Accepted:    150.7K
# Total Submissions: 243K
# Testcase Example:  '5'
#
# The complement of an integer is the integer you get when you flip all the 0's
# to 1's and all the 1's to 0's in its binary representation.
#
#
# For example, The integer 5 is "101" in binary and its complement is "010"
# which is the integer 2.
#
#
# Given an integer n, return its complement.
#
#
# Example 1:
#
#
# Input: n = 5
# Output: 2
# Explanation: 5 is "101" in binary, with complement "010" in binary, which is
# 2 in base-10.
#
#
# Example 2:
#
#
# Input: n = 7
# Output: 0
# Explanation: 7 is "111" in binary, with complement "000" in binary, which is
# 0 in base-10.
#
#
# Example 3:
#
#
# Input: n = 10
# Output: 5
# Explanation: 10 is "1010" in binary, with complement "0101" in binary, which
# is 5 in base-10.
#
#
#
# Constraints:
#
#
# 0 <= n < 10^9
#
#
#
# Note: This question is the same as 476:
# https://leetcode.com/problems/number-complement/
#
#

# @lc tags=array;sort

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 互补数
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def bitwiseComplement(self, n: int) -> int:

        return (2**(len(bin(n)) - 2) - 1) ^ n

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().bitwiseComplement(5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 7')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().bitwiseComplement(7)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 10')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().bitwiseComplement(10)))
    print()

    pass
# @lc main=end