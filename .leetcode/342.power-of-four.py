# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (42.27%)
# Likes:    988
# Dislikes: 264
# Total Accepted:    242.7K
# Total Submissions: 573.6K
# Testcase Example:  '16'
#
# Given an integer n, return true if it is a power of four. Otherwise, return
# false.
#
# An integer n is a power of four, if there exists an integer x such that n ==
# 4^x.
#
#
# Example 1:
# Input: n = 16
# Output: true
# Example 2:
# Input: n = 5
# Output: false
# Example 3:
# Input: n = 1
# Output: true
#
#
# Constraints:
#
#
# -2^31 <= n <= 2^31 - 1
#
#
#
# Follow up: Could you solve it without loops/recursion?
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断一个数，是否是4的幂。
# 直接遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n & 3 != 0:
                return False
            n = n >> 2
        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 16')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPowerOfFour(16)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPowerOfFour(5)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPowerOfFour(1)))
    print()

    pass
# @lc main=end