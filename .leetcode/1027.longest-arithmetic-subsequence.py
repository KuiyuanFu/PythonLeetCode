# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Subsequence
#
# https://leetcode.com/problems/longest-arithmetic-subsequence/description/
#
# algorithms
# Medium (47.06%)
# Likes:    2572
# Dislikes: 116
# Total Accepted:    95.8K
# Total Submissions: 203.6K
# Testcase Example:  '[3,6,9,12]'
#
# Given an array nums of integers, return the length of the longest arithmetic
# subsequence in nums.
#
# Recall that a subsequence of an array nums is a list nums[i1], nums[i2], ...,
# nums[ik] with 0 <= i1 < i2 < ... < ik <= nums.length - 1, and that a sequence
# seq is arithmetic if seq[i+1] - seq[i] are all the same value (for 0 <= i <
# seq.length - 1).
#
#
# Example 1:
#
#
# Input: nums = [3,6,9,12]
# Output: 4
# Explanation:
# The whole array is an arithmetic sequence with steps of length = 3.
#
#
# Example 2:
#
#
# Input: nums = [9,4,7,2,10]
# Output: 3
# Explanation:
# The longest arithmetic subsequence is [4,7,10].
#
#
# Example 3:
#
#
# Input: nums = [20,1,15,3,10,5,8]
# Output: 4
# Explanation:
# The longest arithmetic subsequence is [20,15,10,5].
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 1000
# 0 <= nums[i] <= 500
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找最长的子序列，满足相邻元素差值相同。
# dp
# 保留到当前索引所有步长的子序列的最长长度。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def longestArithSeqLength(self, nums: List[int]) -> int:

        length = len(nums)
        dp = [defaultdict(int) for _ in range(length)]

        for j in range(1, length):
            dpj = dp[j]
            for i in range(j):
                d = nums[j] - nums[i]
                dpj[d] = max(dpj[d], dp[i][d] + 1)

        res = max(max(dp[i].values()) for i in range(length)) + 1
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,6,9,12]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().longestArithSeqLength([3, 6, 9, 12])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [9,4,7,2,10]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().longestArithSeqLength([9, 4, 7, 2, 10])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [20,1,15,3,10,5,8]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().longestArithSeqLength([20, 1, 15, 3, 10, 5, 8])))
    print()

    pass
# @lc main=end