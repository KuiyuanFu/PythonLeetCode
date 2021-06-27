# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (43.18%)
# Likes:    2754
# Dislikes: 167
# Total Accepted:    211.8K
# Total Submissions: 489K
# Testcase Example:  '10'
#
# An ugly number is a positive integer whose prime factors are limited to 2, 3,
# and 5.
#
# Given an integer n, return the n^th ugly number.
#
#
# Example 1:
#
#
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10
# ugly numbers.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are
# limited to 2, 3, and 5.
#
#
#
# Constraints:
#
#
# 1 <= n <= 1690
#
#
#

# @lc tags=math;dynamic-programming;heap

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求丑数，满足整数，只能被2、3、5整除。得到第n个丑数。
# 使用一个集合记录出现过的数字，之后根据已有的丑数生成新的丑数，判断是否出现过，使用优先队列，得到最小的丑数。
#
#
# @lc idea=end

# @lc group=math;dynamic-programming;heap

# @lc rank=7


# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        from heapq import heapify, heappop, heappush

        heap = [1]
        recorder = set(heap)
        muls = [2, 3, 5]
        for _ in range(n):
            ret = heappop(heap)
            for m in muls:
                n = ret * m
                if n not in recorder:
                    recorder.add(n)
                    heappush(heap, n)
        return ret

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 10')
    print('Exception :')
    print('12')
    print('Output :')
    print(str(Solution().nthUglyNumber(10)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().nthUglyNumber(1)))
    print()

    pass
# @lc main=end