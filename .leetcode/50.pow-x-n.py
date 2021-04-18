# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (31.04%)
# Likes:    2280
# Dislikes: 3739
# Total Accepted:    619.6K
# Total Submissions: 2M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
#
#
# Example 1:
#
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
#
#
# Example 2:
#
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
#
#
# Example 3:
#
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
#
#
#
# Constraints:
#
#
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# -10^4 <= x^n <= 10^4
#
#
#
#
#

# @lc tags=math;binary-search

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 幂函数。模重复平方计算法。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1 or n == 0:
            return 1
        minus = n < 0
        if not minus:
            n = -n
        sum = 1
        while n != 0:
            if n % 2:
                sum =sum * x 
            x = x*x
            n = n // -2 * -1
        if minus:
            sum = 1 / sum
        return sum


        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('x = 2.00000, n = 10')
    print('Output :')
    print(str(Solution().myPow(2.00000,10)))
    print('Exception :')
    print('1024.00000')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('x = 2.10000, n = 3')
    print('Output :')
    print(str(Solution().myPow(2.10000,3)))
    print('Exception :')
    print('9.26100')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('x = 2.00000, n = -2')
    print('Output :')
    print(str(Solution().myPow(2.00000,-2)))
    print('Exception :')
    print('0.25000')
    print()
    
    pass
# @lc main=end