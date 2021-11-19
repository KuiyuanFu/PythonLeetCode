# @lc app=leetcode id=762 lang=python3
#
# [762] Prime Number of Set Bits in Binary Representation
#
# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/
#
# algorithms
# Easy (65.43%)
# Likes:    394
# Dislikes: 429
# Total Accepted:    62.3K
# Total Submissions: 94.6K
# Testcase Example:  '6\n10'
#
# Given two integers left and right, return the count of numbers in the
# inclusive range [left, right] having a prime number of set bits in their
# binary representation.
#
# Recall that the number of set bits an integer has is the number of 1's
# present when written in binary.
#
#
# For example, 21 written in binary is 10101, which has 3 set bits.
#
#
#
# Example 1:
#
#
# Input: left = 6, right = 10
# Output: 4
# Explanation:
# 6  -> 110 (2 set bits, 2 is prime)
# 7  -> 111 (3 set bits, 3 is prime)
# 8  -> 1000 (1 set bit, 1 is not prime)
# 9  -> 1001 (2 set bits, 2 is prime)
# 10 -> 1010 (2 set bits, 2 is prime)
# 4 numbers have a prime number of set bits.
#
#
# Example 2:
#
#
# Input: left = 10, right = 15
# Output: 5
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime)
# 11 -> 1011 (3 set bits, 3 is prime)
# 12 -> 1100 (2 set bits, 2 is prime)
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)
# 5 numbers have a prime number of set bits.
#
#
#
# Constraints:
#
#
# 1 <= left <= right <= 10^6
# 0 <= right - left <= 10^4
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 在给定范围内，数字二进制表示中1的个数是素数的个数。
# 直接遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        s = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
        return [bin(n)[2:].count('1') in s
                for n in range(left, right + 1)].count(True)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('left = 6, right = 10')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().countPrimeSetBits(6, 10)))
    print()

    print('Example 2:')
    print('Input : ')
    print('left = 10, right = 15')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().countPrimeSetBits(10, 15)))
    print()

    pass
# @lc main=end