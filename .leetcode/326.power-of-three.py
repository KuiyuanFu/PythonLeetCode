# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (42.60%)
# Likes:    340
# Dislikes: 45
# Total Accepted:    372.3K
# Total Submissions: 873.9K
# Testcase Example:  '27'
#
# Given an integer n, return true if it is a power of three. Otherwise, return
# false.
#
# An integer n is a power of three, if there exists an integer x such that n ==
# 3^x.
#
#
# Example 1:
# Input: n = 27
# Output: true
# Example 2:
# Input: n = 0
# Output: false
# Example 3:
# Input: n = 9
# Output: true
# Example 4:
# Input: n = 45
# Output: false
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

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断一个整数，是否是3的幂。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 3 == 0:
                n = n // 3
            else:
                return False
        return True
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 27')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPowerOfThree(27)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 0')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPowerOfThree(0)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 9')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPowerOfThree(9)))
    print()

    print('Example 4:')
    print('Input : ')
    print('n = 45')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPowerOfThree(45)))
    print()

    pass
# @lc main=end