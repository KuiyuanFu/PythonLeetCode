# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (45.03%)
# Likes:    7737
# Dislikes: 168
# Total Accepted:    575.4K
# Total Submissions: 1.3M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array by deleting
# some or no elements without changing the order of the remaining elements. For
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
#
#
# Example 1:
#
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
#
# Example 3:
#
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
#
#

# @lc tags=binary-search;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个数值序列，求最长的严格递增的子序列的最长长度。
# 使用动态规划的思想，对于每一元素来说，到此位置的最长长度是，之前所有比其小的元素的最长长度的最大值再加一，所以问题就变成了求比其小的元素的长度最大值问题。
# 已有元素根据元素的大小排序，新的元素会得到一个长度的值，如果之前的元素中，存在元素大于此元素且长度小于等于此长度，那就可以删去那个长度。
# 所以已有元素序列的结果，是一个元素值与长度值都严格递增的序列。实际上每个元素值的索引，就是其长度的序号。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for n in nums:
            l, r = 0, len(dp)
            while l < r:
                m = (l + r) // 2
                if dp[m] < n:
                    l = m + 1
                else:
                    r = m
            if r == len(dp):
                dp.append(n)
            else:
                dp[r] = min(dp[r], n)
        return len(dp)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [10,9,2,5,3,7,101,18]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,1,0,3,2,3]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [7,7,7,7,7,7,7]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7])))
    print()

    pass
# @lc main=end