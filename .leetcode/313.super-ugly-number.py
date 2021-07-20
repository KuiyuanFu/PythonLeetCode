# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#
# https://leetcode.com/problems/super-ugly-number/description/
#
# algorithms
# Medium (47.05%)
# Likes:    995
# Dislikes: 178
# Total Accepted:    91.4K
# Total Submissions: 194.3K
# Testcase Example:  '12\n[2,7,13,19]'
#
# A super ugly number is a positive integer whose prime factors are in the
# array primes.
#
# Given an integer n and an array of integers primes, return the n^th super
# ugly number.
#
# The n^th super ugly number is guaranteed to fit in a 32-bit signed
# integer.
#
#
# Example 1:
#
#
# Input: n = 12, primes = [2,7,13,19]
# Output: 32
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
# super ugly numbers given primes = [2,7,13,19].
#
#
# Example 2:
#
#
# Input: n = 1, primes = [2,3,5]
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are
# in the array primes = [2,3,5].
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^6
# 1 <= primes.length <= 100
# 2 <= primes[i] <= 1000
# primes[i] is guaranteed to be a prime number.
# All the values of primes are unique and sorted in ascending order.
#
#
#

# @lc tags=math;heap

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求超级丑数，满足整数，只能被给定的素数整除。得到第n个丑数。
# 使用一个集合记录出现过的数字，之后根据已有的丑数生成新的丑数，判断是否出现过，使用优先队列，得到最小的丑数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        from heapq import heapify, heappop, heappush

        heap = [1]
        recorder = set(heap)
        for _ in range(n):
            ret = heappop(heap)
            for m in primes:
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
    print('n = 12, primes = [2,7,13,19]')
    print('Exception :')
    print('32')
    print('Output :')
    print(str(Solution().nthSuperUglyNumber(12, [2, 7, 13, 19])))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1, primes = [2,3,5]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().nthSuperUglyNumber(1, [2, 3, 5])))
    print()

    pass
# @lc main=end