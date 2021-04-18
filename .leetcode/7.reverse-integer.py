# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.95%)
# Likes:    4551
# Dislikes: 6976
# Total Accepted:    1.5M
# Total Submissions: 5.7M
# Testcase Example:  '123'
#
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-2^31, 2^31 - 1], then return 0.
# 
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
# 
# 
# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21
# Example 4:
# Input: x = 0
# Output: 0
# 
# 
# Constraints:
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
#
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 反转数字。首先将数字变成字符串，关键点是异号的除数和被除数的求模和整数除法与同好的不同，且不同编程语言的实现也不同。 Python 中如下：
# >>> 11 % 10
# 1
# >>> 11 % -10
# -9
# >>> -11  % 10
# 9
# >>> -11  % -10 
# -1
# 可见余数与除数同号。
# >>> 11 // 10
# 1
# >>> 11 // -10
# -2
# >>> -11 // 10
# -2
# >>> -11 // -10
# 1
# 可见异号时，由于余数的变化，商也与预期不同，所以最好是同号时进行运算，这样才与直观感觉相符。

# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        flag  = True if x >0 else False
        s = ''

        if flag:
            while x !=0:
                s += str(x %10)
                x = x //10
            s.lstrip('0')
            if len(s) == len('2147483647') and s > '2147483647':
                return 0 
            else :
                return (int(s) ) if (len(s) !=0 )  else 0
        else :
            while x !=0:
                s += str(  x % -10 * -1 )
                x = x //-10 *-1
            s.lstrip('0')
            if len(s) == len('2147483648') and s > '2147483648':
                return 0 
            else :
                return  (-1*int(s) ) if (len(s) !=0 )  else 0
        

        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('x = 123')
    print('Output :')
    print(str(Solution().reverse(123)))
    print('Exception :')
    print('321')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('x = -123')
    print('Output :')
    print(str(Solution().reverse(-123)))
    print('Exception :')
    print('-321')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('x = 120')
    print('Output :')
    print(str(Solution().reverse(120)))
    print('Exception :')
    print('21')
    print()
    
    print('Example 4:')
    print('Input : ')
    print('x = 0')
    print('Output :')
    print(str(Solution().reverse(0)))
    print('Exception :')
    print('0')
    print()
    
    pass
# @lc main=end