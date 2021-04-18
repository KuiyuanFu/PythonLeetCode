# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (35.11%)
# Likes:    2421
# Dislikes: 980
# Total Accepted:    362K
# Total Submissions: 1M
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
#
# Note: You must not use any built-in BigInteger library or convert the inputs
# to integer directly.
#
#
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Constraints:
#
#
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
#
#
#
#
#

# @lc tags=math;string

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 计算两个正整数的乘积，以字符串的形式计算。
# 直接乘呗。反转，从低到高依次乘。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = [0] * (len(num1)+len(num2)+1)
        for i, c1 in enumerate(reversed(num1)):
            for j, c2 in enumerate(reversed(num2)):
                n = (ord(c1) - 48) * (ord(c2) - 48)
                result[i+j+1] += (result[i+j] + n) // 10
                result[i+j] = (result[i+j] + n) % 10
        r = ''.join([str(n) for n in reversed(result)]).lstrip('0')
        return r if len(r) > 0 else '0'


        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num1 = "2", num2 = "3"')
    print('Output :')
    print(str(Solution().multiply("2","3")))
    print('Exception :')
    print('"6"')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('num1 = "123", num2 = "456"')
    print('Output :')
    print(str(Solution().multiply("123","456")))
    print('Exception :')
    print('"56088"')
    print()
    
    pass
# @lc main=end