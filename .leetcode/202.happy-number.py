# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (51.56%)
# Likes:    3297
# Dislikes: 532
# Total Accepted:    640.3K
# Total Submissions: 1.2M
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
#
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
#
#
# Return true if n is a happy number, and false if not.
#
#
# Example 1:
#
#
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
# Example 2:
#
#
# Input: n = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc tags=hash-table;math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 快乐的数字，循环数字中的每一个数的平方和，直到等于1，就是快乐的，无限循环就是不快乐。
# 直接循环，集合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    mem = {}

    def isHappy(self, n: int) -> bool:
        buffer = set()
        while n != 1:
            buffer.add(n)
            next = 0
            while n != 0:
                next += (n % 10)**2
                n //= 10
            n = next
            if n in buffer:
                return False

        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 19')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isHappy(19)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isHappy(2)))
    print()

    pass
# @lc main=end