# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#
# https://leetcode.com/problems/binary-gap/description/
#
# algorithms
# Easy (61.74%)
# Likes:    416
# Dislikes: 589
# Total Accepted:    57.5K
# Total Submissions: 93.1K
# Testcase Example:  '22'
#
# Given a positive integer n, find and return the longest distance between any
# two adjacent 1's in the binary representation of n. If there are no two
# adjacent 1's, return 0.
#
# Two 1's are adjacent if there are only 0's separating them (possibly no 0's).
# The distance between two 1's is the absolute difference between their bit
# positions. For example, the two 1's in "1001" have a distance of 3.
#
#
# Example 1:
#
#
# Input: n = 22
# Output: 2
# Explanation: 22 in binary is "10110".
# The first adjacent pair of 1's is "10110" with a distance of 2.
# The second adjacent pair of 1's is "10110" with a distance of 1.
# The answer is the largest of these two distances, which is 2.
# Note that "10110" is not a valid pair since there is a 1 separating the two
# 1's underlined.
#
#
# Example 2:
#
#
# Input: n = 8
# Output: 0
# Explanation: 8 in binary is "1000".
# There are not any adjacent pairs of 1's in the binary representation of 8, so
# we return 0.
#
#
# Example 3:
#
#
# Input: n = 5
# Output: 2
# Explanation: 5 in binary is "101".
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^9
#
#
#

# @lc tags=two-pointers;dynamic-programming

# @lc imports=start
import enum
from operator import indexOf
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二进制间隔，将整数表示为二进制后，相邻的两个1的最小间隔。
# 转二进制，遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        charList = bin(n)[2:]

        res = 0
        IdxPre = len(charList)
        for i, n in enumerate(charList):
            if n == '1':
                res = max(res, i - IdxPre)
                IdxPre = i
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 22')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().binaryGap(22)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 8')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().binaryGap(8)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().binaryGap(5)))
    print()

    pass
# @lc main=end