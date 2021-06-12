# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (39.78%)
# Likes:    1430
# Dislikes: 148
# Total Accepted:    173.6K
# Total Submissions: 436.2K
# Testcase Example:  '5\n7'
#
# Given two integers left and right that represent the range [left, right],
# return the bitwise AND of all numbers in this range, inclusive.
#
#
# Example 1:
#
#
# Input: left = 5, right = 7
# Output: 4
#
#
# Example 2:
#
#
# Input: left = 0, right = 0
# Output: 0
#
#
# Example 3:
#
#
# Input: left = 1, right = 2147483647
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= left <= right <= 2^31 - 1
#
#
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个数，求这个闭区间所有值的二进制与的结果。
# 直接依次读取两个数的位，之后看最后改变位的位置,剩下的位就是与的结果了。
#
# @lc idea=end

# @lc group=bit-manipulation

# @lc rank=4


# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        length = 0
        while left != right:
            left >>= 1
            right >>= 1
            length += 1
        return left << length


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('left = 5, right = 7')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().rangeBitwiseAnd(5, 7)))
    print()

    print('Example 2:')
    print('Input : ')
    print('left = 0, right = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().rangeBitwiseAnd(0, 0)))
    print()

    print('Example 3:')
    print('Input : ')
    print('left = 1, right = 2147483647')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().rangeBitwiseAnd(1, 2147483647)))
    print()

    pass
# @lc main=end