# @lc app=leetcode id=537 lang=python3
#
# [537] Complex Number Multiplication
#
# https://leetcode.com/problems/complex-number-multiplication/description/
#
# algorithms
# Medium (70.85%)
# Likes:    436
# Dislikes: 1054
# Total Accepted:    76.7K
# Total Submissions: 108.3K
# Testcase Example:  '"1+1i"\n"1+1i"'
#
# A complex number can be represented as a string on the form "real+imaginaryi"
# where:
#
#
# real is the real part and is an integer in the range [-100, 100].
# imaginary is the imaginary part and is an integer in the range [-100,
# 100].
# i^2 == -1.
#
#
# Given two complex numbers num1 and num2 as strings, return a string of the
# complex number that represents their multiplications.
#
#
# Example 1:
#
#
# Input: num1 = "1+1i", num2 = "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it
# to the form of 0+2i.
#
#
# Example 2:
#
#
# Input: num1 = "1+-1i", num2 = "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert
# it to the form of 0+-2i.
#
#
#
# Constraints:
#
#
# num1 and num2 are valid complex numbers.
#
#
#

# @lc tags=math;string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 负数乘法。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def splitComplex(s: str):
            s = s.rstrip('i')
            ss = s.split('+')
            r = int(ss[0])
            i = int(ss[1])
            return r, i

        r1, i1 = splitComplex(num1)
        r2, i2 = splitComplex(num2)
        r = r1 * r2 - i1 * i2
        i = r1 * i2 + r2 * i1
        return str(r) + '+' + str(i) + 'i'
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num1 = "1+1i", num2 = "1+1i"')
    print('Exception :')
    print('"0+2i"')
    print('Output :')
    print(str(Solution().complexNumberMultiply("1+1i", "1+1i")))
    print()

    print('Example 2:')
    print('Input : ')
    print('num1 = "1+-1i", num2 = "1+-1i"')
    print('Exception :')
    print('"0+-2i"')
    print('Output :')
    print(str(Solution().complexNumberMultiply("1+-1i", "1+-1i")))
    print()

    pass
# @lc main=end