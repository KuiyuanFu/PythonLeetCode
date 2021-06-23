# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#
# https://leetcode.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (31.95%)
# Likes:    417
# Dislikes: 769
# Total Accepted:    54K
# Total Submissions: 168.8K
# Testcase Example:  '13'
#
# Given an integer n, count the total number of digit 1 appearing in all
# non-negative integers less than or equal to n.
#
#
# Example 1:
#
#
# Input: n = 13
# Output: 6
#
#
# Example 2:
#
#
# Input: n = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= n <= 2 * 10^9
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定整数n，求小于等于n的所有整数一共含有多少个1。
# 我们首先要计算每进一位，就会有多少个1。
# 0 - 0
# 9 - 1 ：1
# 99 - 20 ：1 10 11 12-19 21-91
# 999 -
#
#
# @lc idea=end

# @lc group=math

# @lc rank=10


# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:

        counts = [0, 1]
        numbers = [1, 10]
        while numbers[-1] <= n // 10:

            counts.append(counts[-1] * 10 + numbers[-1])
            numbers.append(numbers[-1] * 10)
        ret = 0
        for i in reversed(range(len(numbers))):
            num = numbers[i]
            count = counts[i]
            q = n // num
            ret += q * count
            n = n % num
            if q >= 2:
                ret += num
            elif q == 1:
                ret += n + 1
        return ret
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().countDigitOne(123)))
    print(str(Solution().countDigitOne(1234)))
    print(str(Solution().countDigitOne(12345)))
    print('Example 1:')
    print('Input : ')
    print('n = 13')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().countDigitOne(13)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().countDigitOne(0)))
    print()

    pass
# @lc main=end