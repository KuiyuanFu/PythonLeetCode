# @lc app=leetcode id=440 lang=python3
#
# [440] K-th Smallest in Lexicographical Order
#
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/
#
# algorithms
# Hard (30.06%)
# Likes:    463
# Dislikes: 67
# Total Accepted:    15.9K
# Total Submissions: 52.    9K
# Testcase Example:  '13\n2'
#
# Given two integers n and k, return the k^th lexicographically smallest
# integer in the range [1, n].
#
#
# Example 1:
#
#
# Input: n = 13, k = 2
# Output: 10
# Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6,
# 7, 8, 9], so the second smallest number is 10.
#
#
# Example 2:
#
#
# Input: n = 1, k = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= k <= n <= 10^9
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定n，找1-n按照字典序排列的第k小值。
# 从高位向低位依次判断。本质上是找接下来的两个相邻数字中间的间隔是否大于k，如果大于，则跳过这个数字。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def findGap(l, r):
            g = 0
            while l <= n:
                g += min(n + 1, r) - l
                l *= 10
                r *= 10
            return g

        l = 1
        while k > 1:
            g = findGap(l, l + 1)
            if g < k:
                k -= g
                l += 1
            else:
                l *= 10
                k -= 1
        return l


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 13, k = 2')
    print('Exception :')
    print('10')
    print('Output :')
    print(str(Solution().findKthNumber(13, 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1, k = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findKthNumber(1, 1)))
    print()

    pass
# @lc main=end