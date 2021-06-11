# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#
# https://leetcode.com/problems/reverse-bits/description/
#
# algorithms
# Easy (43.23%)
# Likes:    1822
# Dislikes: 583
# Total Accepted:    349.2K
# Total Submissions: 804.7K
# Testcase Example:  '00000010100101000001111010011100'
#
# Reverse bits of a given 32 bits unsigned integer.
#
# Note:
#
#
# Note that in some languages such as Java, there is no unsigned integer type.
# In this case, both input and output will be given as a signed integer type.
# They should not affect your implementation, as the integer's internal binary
# representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement
# notation. Therefore, in Example 2 above, the input represents the signed
# integer -3 and the output represents the signed integer -1073741825.
#
#
# Follow up:
#
# If this function is called many times, how would you optimize it?
#
#
# Example 1:
#
#
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100
# represents the unsigned integer 43261596, so return 964176192 which its
# binary representation is 00111001011110000010100101000000.
#
#
# Example 2:
#
#
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101
# represents the unsigned integer 4294967293, so return 3221225471 which its
# binary representation is 10111111111111111111111111111111.
#
#
#
# Constraints:
#
#
# The input must be a binary string of length 32
#
#
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 按位反转一个无符号整数。
# 使用分治法，可以从 O(32)缩减到 O(lg32)。
#
# @lc idea=end

# @lc group=bit-manipulation

# @lc rank=10


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:

        # 左右16位，互换
        n = n >> 16 | n << 16
        # 使用掩码，将16位中的左右各八位互换。
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().reverseBits(0b00000010100101000001111010011100)))
    print('Example 1:')
    print('Input : ')
    print('n = 00000010100101000001111010011100')
    print('Exception :')
    print('964176192 (00111001011110000010100101000000)')
    print('Output :')
    print(str(Solution().reverseBits(0b00000010100101000001111010011100)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 11111111111111111111111111111101')
    print('Exception :')
    print('3221225471 (10111111111111111111111111111111)')
    print('Output :')
    print(str(Solution().reverseBits(0b11111111111111111111111111111101)))
    print()

    pass
# @lc main=end