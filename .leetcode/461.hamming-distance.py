# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (73.57%)
# Likes:    2406
# Dislikes: 182
# Total Accepted:    415.8K
# Total Submissions: 564.9K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
#
# Given two integers x and y, return the Hamming distance between them.
#
#
# Example 1:
#
#
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
# The above arrows point to positions where the corresponding bits are
# different.
#
#
# Example 2:
#
#
# Input: x = 3, y = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 0 <= x, y <= 2^31 - 1
#
#
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求hamming距离，即不同的位的个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        res = 0
        while n:
            if n & 1 != 0:
                res += 1
            n >>= 1
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('x = 1, y = 4')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().hammingDistance(1, 4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('x = 3, y = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().hammingDistance(3, 1)))
    print()

    pass
# @lc main=end