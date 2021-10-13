# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
#
# algorithms
# Easy (47.06%)
# Likes:    1431
# Dislikes: 154
# Total Accepted:    168.8K
# Total Submissions: 356.7K
# Testcase Example:  '[1,3,5,4,7]'
#
# Given an unsorted array of integers nums, return the length of the longest
# continuous increasing subsequence (i.e. subarray). The subsequence must be
# strictly increasing.
#
# A continuous increasing subsequence is defined by two indices l and r (l < r)
# such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for
# each l <= i < r, nums[i] < nums[i + 1].
#
#
# Example 1:
#
#
# Input: nums = [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5] with
# length 3.
# Even though [1,3,5,7] is an increasing subsequence, it is not continuous as
# elements 5 and 7 are separated by element
# 4.
#
#
# Example 2:
#
#
# Input: nums = [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2] with length
# 1. Note that it must be strictly
# increasing.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求严格单调递增子数组的最长长度。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        pre = nums[0]
        l = 0
        res = 0
        for n in nums:
            if pre < n:
                l += 1

            else:
                l = 1
            res = max(res, l)
            pre = n
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,5,4,7]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findLengthOfLCIS([1, 3, 5, 4, 7])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,2,2,2,2]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findLengthOfLCIS([2, 2, 2, 2, 2])))
    print()

    pass
# @lc main=end