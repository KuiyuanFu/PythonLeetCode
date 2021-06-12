# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (32.81%)
# Likes:    3315
# Dislikes: 819
# Total Accepted:    498.8K
# Total Submissions: 1.5M
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
#
#
# Example 1:
#
#
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#
# Example 2:
#
#
# Input: n = 0
# Output: 0
#
#
# Example 3:
#
#
# Input: n = 1
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= n <= 5 * 10^6
#
#
#

# @lc tags=hash-table;math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 计算小于一个非负数的素数。
# 使用散筛法。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        buffer = [True] * n
        buffer[0] = buffer[1] = False
        count = 0
        for i in range(n):
            if buffer[i]:
                count += 1
                for j in range(2, (n - 1) // i + 1):
                    buffer[i * j] = False
        return count


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 10')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().countPrimes(10)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().countPrimes(0)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().countPrimes(1)))
    print()

    pass
# @lc main=end