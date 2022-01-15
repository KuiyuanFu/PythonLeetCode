# @lc app=leetcode id=813 lang=python3
#
# [813] Largest Sum of Averages
#
# https://leetcode.com/problems/largest-sum-of-averages/description/
#
# algorithms
# Medium (52.08%)
# Likes:    1460
# Dislikes: 73
# Total Accepted:    37.6K
# Total Submissions: 72.1K
# Testcase Example:  '[9,1,2,3,9]\n3'
#
# You are given an integer array nums and an integer k. You can partition the
# array into at most k non-empty adjacent subarrays. The score of a partition
# is the sum of the averages of each subarray.
#
# Note that the partition must use every integer in nums, and that the score is
# not necessarily an integer.
#
# Return the maximum score you can achieve of all the possible partitions.
# Answers within 10^-6 of the actual answer will be accepted.
#
#
# Example 1:
#
#
# Input: nums = [9,1,2,3,9], k = 3
# Output: 20.00000
# Explanation:
# The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is
# 9 + (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4,5,6,7], k = 4
# Output: 20.50000
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将数组分成k组，求每组平均值的和的最大值。
# 动态规划。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # The max sum in 0-index, 1-k partition.
        dp = [[nums[0]] * k]

        for i in range(1, len(nums)):
            nl = [(nums[i] + dp[-1][0] * i) / (i + 1)] * k
            s = 0
            for j in range(i, 0, -1):
                s += nums[j]
                t = s / (i - j + 1)
                dpj = dp[j - 1]
                for ki in range(1, k):
                    nl[ki] = max(nl[ki], t + dpj[ki - 1])
            dp.append(nl)
        return dp[-1][-1]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [9,1,2,3,9], k = 3')
    print('Exception :')
    print('20.00000')
    print('Output :')
    print(str(Solution().largestSumOfAverages([9, 1, 2, 3, 9], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4,5,6,7], k = 4')
    print('Exception :')
    print('20.50000')
    print('Output :')
    print(str(Solution().largestSumOfAverages([1, 2, 3, 4, 5, 6, 7], 4)))
    print()

    pass
# @lc main=end