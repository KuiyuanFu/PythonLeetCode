# @lc app=leetcode id=1015 lang=python3
#
# [1015] Smallest Integer Divisible by K
#
# https://leetcode.com/problems/smallest-integer-divisible-by-k/description/
#
# algorithms
# Medium (47.05%)
# Likes:    1011
# Dislikes: 828
# Total Accepted:    57.4K
# Total Submissions: 122K
# Testcase Example:  '1'
#
# Given a positive integer k, you need to find the length of the smallest
# positive integer n such that n is divisible by k, and n only contains the
# digit 1.
#
# Return the length of n. If there is no such n, return -1.
#
# Note: n may not fit in a 64-bit signed integer.
#
#
# Example 1:
#
#
# Input: k = 1
# Output: 1
# Explanation: The smallest answer is n = 1, which has length 1.
#
#
# Example 2:
#
#
# Input: k = 2
# Output: -1
# Explanation: There is no such positive integer n divisible by 2.
#
#
# Example 3:
#
#
# Input: k = 3
# Output: 3
# Explanation: The smallest answer is n = 111, which has length 3.
#
#
#
# Constraints:
#
#
# 1 <= k <= 10^5
#
#
#

# @lc tags=Unknown

# @lc imports=start
from re import T
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定k，求所有数字都是1的数，可以整除k的，最小长度。
# 余数判断。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def smallestRepunitDivByK(self, k: int) -> int:

        visited = set()
        t = 0
        for i in range(1, 0xffffffff):
            t = (t * 10 + 1) % k
            if t == 0:
                return i
            elif t in visited:
                return -1
            visited.add(t)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('k = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().smallestRepunitDivByK(1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('k = 2')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().smallestRepunitDivByK(2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('k = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().smallestRepunitDivByK(3)))
    print()

    pass
# @lc main=end