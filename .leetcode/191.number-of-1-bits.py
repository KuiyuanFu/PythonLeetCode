# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#
# https://leetcode.com/problems/number-of-1-bits/description/
#
# algorithms
# Easy (54.85%)
# Likes:    1573
# Dislikes: 649
# Total Accepted:    505.6K
# Total Submissions: 919.1K
# Testcase Example:  '00000000000000000000000000001011'
#
# Write a function that takes an unsigned integer and returns the number of '1'
# bits it has (also known as the Hamming weight).
#
# Note:
#
#
# Note that in some languages, such as Java, there is no unsigned integer type.
# In this case, the input will be given as a signed integer type. It should not
# affect your implementation, as the integer's internal binary representation
# is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement
# notation. Therefore, in Example 3, the input represents the signed integer.
# -3.
#
#
#
# Example 1:
#
#
# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a
# total of three '1' bits.
#
#
# Example 2:
#
#
# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a
# total of one '1' bit.
#
#
# Example 3:
#
#
# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a
# total of thirty one '1' bits.
#
#
#
# Constraints:
#
#
# The input must be a binary string of length 32.
#
#
#
# Follow up: If this function is called many times, how would you optimize it?
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求一个数的二进制表示中，有多少个1。
# 直接循环，移位。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n != 0:
            result += n & 1
            n >>= 1
        return result


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 00000000000000000000000000001011')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().hammingWeight(0b00000000000000000000000000001011)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 00000000000000000000000010000000')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().hammingWeight(0b00000000000000000000000010000000)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 11111111111111111111111111111101')
    print('Exception :')
    print('31')
    print('Output :')
    print(str(Solution().hammingWeight(0b11111111111111111111111111111101)))
    print()

    pass
# @lc main=end