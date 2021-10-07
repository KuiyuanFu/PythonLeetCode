# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Medium (34.61%)
# Likes:    1069
# Dislikes: 433
# Total Accepted:    118.6K
# Total Submissions: 342.7K
# Testcase Example:  '5'
#
# Given a non-negative integer c, decide whether there're two integers a and b
# such that a^2 + b^2 = c.
#
#
# Example 1:
#
#
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
#
#
# Example 2:
#
#
# Input: c = 3
# Output: false
#
#
# Example 3:
#
#
# Input: c = 4
# Output: true
#
#
# Example 4:
#
#
# Input: c = 2
# Output: true
#
#
# Example 5:
#
#
# Input: c = 1
# Output: true
#
#
#
# Constraints:
#
#
# 0 <= c <= 2^31 - 1
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断一个数是否是两个平方的和。
# 暴力遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        idx = -1

        while True:
            idx += 1
            t = c - idx * idx
            tt = int(sqrt(t))
            if t == tt * tt:
                return True
            if idx >= tt:
                return False

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('c = 5')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().judgeSquareSum(5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('c = 3')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().judgeSquareSum(3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('c = 4')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().judgeSquareSum(4)))
    print()

    print('Example 4:')
    print('Input : ')
    print('c = 2')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().judgeSquareSum(2)))
    print()

    print('Example 5:')
    print('Input : ')
    print('c = 1')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().judgeSquareSum(1)))
    print()

    pass
# @lc main=end