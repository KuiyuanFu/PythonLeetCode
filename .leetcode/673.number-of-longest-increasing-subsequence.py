# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (39.22%)
# Likes:    2765
# Dislikes: 137
# Total Accepted:    90.7K
# Total Submissions: 229.3K
# Testcase Example:  '[1,3,5,4,7]'
#
# Given an integer array nums, return the number of longest increasing
# subsequences.
#
# Notice that the sequence has to be strictly increasing.
#
#
# Example 1:
#
#
# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1,
# 3, 5, 7].
#
#
# Example 2:
#
#
# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1,
# and there are 5 subsequences' length is 1, so output 5.
#
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2000
# -10^6 <= nums[i] <= 10^6
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求最长严格递增的子序列的个数。
# 保存每个不同数值，以其结尾的最长子序列长度及数量。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = []
        for n in nums:
            idx = None
            ln = 0
            cn = 1
            for i in range(len(dp)):
                ni, l, c = dp[i]
                if ni == n:
                    idx = i
                elif ni < n:
                    if l > ln:
                        ln = l
                        cn = c
                    elif l == ln:
                        cn += c
            ln += 1
            if idx is not None:
                ni, l, c = dp[idx]

                if l < ln:
                    dp[idx][1] = ln
                    dp[idx][2] = cn

                elif l == ln:
                    dp[idx][2] += cn
            else:
                dp.append([n, ln, cn])
        ml = 0
        res = 0
        for i in range(len(dp)):
            ni, l, c = dp[i]
            if l == ml:
                res += c
            elif l > ml:
                ml, res = l, c
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,5,4,7]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findNumberOfLIS([1, 3, 5, 4, 7])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,2,2,2,2]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findNumberOfLIS([2, 2, 2, 2, 2])))
    print()

    pass
# @lc main=end