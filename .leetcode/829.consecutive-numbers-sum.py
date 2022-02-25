# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#
# https://leetcode.com/problems/consecutive-numbers-sum/description/
#
# algorithms
# Hard (40.82%)
# Likes:    963
# Dislikes: 1158
# Total Accepted:    65.3K
# Total Submissions: 160K
# Testcase Example:  '5'
#
# Given an integer n, return the number of ways you can write n as the sum of
# consecutive positive integers.
#
#
# Example 1:
#
#
# Input: n = 5
# Output: 2
# Explanation: 5 = 2 + 3
#
#
# Example 2:
#
#
# Input: n = 9
# Output: 3
# Explanation: 9 = 4 + 5 = 2 + 3 + 4
#
#
# Example 3:
#
#
# Input: n = 15
# Output: 4
# Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
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

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定整数n，求有多少种连续正整数的序列的和等于其。
# 直接按长度计算。计算这么长l的序列的最小值base，之后判断时候(n - base) % l == 0，如果是，就合理。如果base > n，那就没有合理的了。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:

        res = 0

        for l in range(1, n + 1):
            base = (1 + l) * l // 2
            if base > n:
                break

            if (n - base) % l == 0:
                res += 1

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().consecutiveNumbersSum(5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 9')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().consecutiveNumbersSum(9)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 15')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().consecutiveNumbersSum(15)))
    print()

    print(str(Solution().consecutiveNumbersSum(10**9)))
    print()

    pass
# @lc main=end