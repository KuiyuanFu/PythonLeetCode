# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#
# https://leetcode.com/problems/self-dividing-numbers/description/
#
# algorithms
# Easy (76.33%)
# Likes:    1001
# Dislikes: 337
# Total Accepted:    164.8K
# Total Submissions: 215.4K
# Testcase Example:  '1\n22'
#
# A self-dividing number is a number that is divisible by every digit it
# contains.
#
#
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 ==
# 0, and 128 % 8 == 0.
#
#
# A self-dividing number is not allowed to contain the digit zero.
#
# Given two integers left and right, return a list of all the self-dividing
# numbers in the range [left, right].
#
#
# Example 1:
# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
# Example 2:
# Input: left = 47, right = 85
# Output: [48,55,66,77]
#
#
# Constraints:
#
#
# 1 <= left <= right <= 10^4
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找自身整除的数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.buffer = []
        for i in range(1, 10001):
            n = i
            while n:
                m = n % 10
                if m == 0 or i % m != 0:
                    break
                n = n // 10
            if n == 0:
                self.buffer.append(i)

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            s = str(i)
            f = True
            if '0' in s:
                continue
            for c in s:
                if i % int(c) != 0:
                    f = False
                    break
            if f:
                res.append(i)
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('left = 1, right = 22')
    print('Exception :')
    print('[1,2,3,4,5,6,7,8,9,11,12,15,22]')
    print('Output :')
    print(str(Solution().selfDividingNumbers(1, 22)))
    print()

    print('Example 2:')
    print('Input : ')
    print('left = 47, right = 85')
    print('Exception :')
    print('[48,55,66,77]')
    print('Output :')
    print(str(Solution().selfDividingNumbers(47, 85)))
    print()

    pass
# @lc main=end