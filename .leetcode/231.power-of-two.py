# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (43.81%)
# Likes:    1455
# Dislikes: 223
# Total Accepted:    426.8K
# Total Submissions: 974.2K
# Testcase Example:  '1'
#
# Given an integer n, return true if it is a power of two. Otherwise, return
# false.
#
# An integer n is a power of two, if there exists an integer x such that n ==
# 2^x.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: true
# Explanation: 2^0 = 1
#
#
# Example 2:
#
#
# Input: n = 16
# Output: true
# Explanation: 2^4 = 16
#
#
# Example 3:
#
#
# Input: n = 3
# Output: false
#
#
# Example 4:
#
#
# Input: n = 4
# Output: true
#
#
# Example 5:
#
#
# Input: n = 5
# Output: false
#
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

# @lc tags=math;bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断一个数是否是2的幂结果。
# 直接重复模2，看余数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 2 == 1:
                return False
            n = n // 2
        return True
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPowerOfTwo(1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 16')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPowerOfTwo(16)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPowerOfTwo(3)))
    print()

    print('Example 4:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPowerOfTwo(4)))
    print()

    print('Example 5:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPowerOfTwo(5)))
    print()

    pass
# @lc main=end