# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#
# https://leetcode.com/problems/sum-of-subarray-minimums/description/
#
# algorithms
# Medium (33.81%)
# Likes:    3412
# Dislikes: 228
# Total Accepted:    75.1K
# Total Submissions: 222K
# Testcase Example:  '[3,1,2,4]'
#
# Given an array of integers arr, find the sum of min(b), where b ranges over
# every (contiguous) subarray of arr. Since the answer may be large, return the
# answer modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: arr = [3,1,2,4]
# Output: 17
# Explanation:
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4],
# [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
#
#
# Example 2:
#
#
# Input: arr = [11,81,94,43,3]
# Output: 444
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 3 * 10^4
# 1 <= arr[i] <= 3 * 10^4
#
#
#

# @lc tags=binary-search

# @lc imports=start
from turtle import right
from imports import *

# @lc imports=end

# @lc idea=start
#
# 获得所有连续子序列的最小值等的和。
# dp，记录最小值对应的序列长度，及和。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def sumSubarrayMins(self, arr: List[int]) -> int:

        dp = []
        res = 0
        for n in arr:
            l = 1
            while len(dp) > 0 and dp[-1][0] >= n:
                l += dp[-1][1]
                dp.pop()
            s = 0
            if len(dp) > 0:
                s += dp[-1][2]
            s += n * l
            dp.append((n, l, s))
            res += s
        return res % (10**9 + 7)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [3,1,2,4]')
    print('Exception :')
    print('17')
    print('Output :')
    print(str(Solution().sumSubarrayMins([3, 1, 2, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [11,81,94,43,3]')
    print('Exception :')
    print('444')
    print('Output :')
    print(str(Solution().sumSubarrayMins([11, 81, 94, 43, 3])))
    print()
    print(str(Solution().sumSubarrayMins([71, 55, 82, 55])))
    pass
# @lc main=end