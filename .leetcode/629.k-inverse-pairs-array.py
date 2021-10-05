# @lc app=leetcode id=629 lang=python3
#
# [629] K Inverse Pairs Array
#
# https://leetcode.com/problems/k-inverse-pairs-array/description/
#
# algorithms
# Hard (37.14%)
# Likes:    710
# Dislikes: 107
# Total Accepted:    23.8K
# Total Submissions: 63.9K
# Testcase Example:  '3\n0'
#
# For an integer array nums, an inverse pair is a pair of integers [i, j] where
# 0 <= i < j < nums.length and nums[i] > nums[j].
#
# Given two integers n and k, return the number of different arrays consist of
# numbers from 1 to n such that there are exactly k inverse pairs. Since the
# answer can be huge, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 3, k = 0
# Output: 1
# Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has
# exactly 0 inverse pairs.
#
#
# Example 2:
#
#
# Input: n = 3, k = 1
# Output: 2
# Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
#
#
#
# Constraints:
#
#
# 1 <= n <= 1000
# 0 <= k <= 1000
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求指定逆序个数的排序种类。
# dp。
# 对于n长的数组，第一位可以选任意一个数，就会产生选择数字减一的逆序，剩余的继续这么选择。
# 那么用一个数组保存，对于共n个数时，0-k个逆序对所对应的排序个数。
# 那么对于n+1个数时，由于可以选择1-n的任意一个数，产生0-(n-1)个逆序，所以，对于j个逆序对的情况，种类是n长中(j-(n-1)) - j对应种类的和，用滑动窗口避免重复运算。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        k += 1
        dp = [0 for _ in range(k)]
        dp[0] = 1
        dpn = [0 for _ in range(k)]
        for idx in range(1, n):
            s = 0
            for j in range(k):
                s += dp[j]
                dpn[j] = s % 1000000007
                if j - idx >= 0:
                    s -= dp[j - idx]
            dp, dpn = dpn, dp
        return dp[-1]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3, k = 0')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().kInversePairs(3, 0)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 3, k = 1')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().kInversePairs(3, 1)))
    print()
    print(str(Solution().kInversePairs(1000, 1000)))
    pass
# @lc main=end