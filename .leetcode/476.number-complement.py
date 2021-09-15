# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#
# https://leetcode.com/problems/number-complement/description/
#
# algorithms
# Easy (65.38%)
# Likes:    1300
# Dislikes: 90
# Total Accepted:    220.6K
# Total Submissions: 337.3K
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
# Given an integer num, return its complement.
#
#
# Example 1:
#
#
# Input: num = 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
#
#
# Example 2:
#
#
# Input: num = 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and
# its complement is 0. So you need to output 0.
#
#
#
# Constraints:
#
#
# 1 <= num < 2^31
#
#
#
# Note: This question is the same as 1009:
# https://leetcode.com/problems/complement-of-base-10-integer/
#
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 补数，取反。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        mask = 0
        while mask < num:
            mask = (mask << 1) + 1
        return (~num) & mask

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num = 5')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findComplement(5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('num = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().findComplement(1)))
    print()

    pass
# @lc main=end