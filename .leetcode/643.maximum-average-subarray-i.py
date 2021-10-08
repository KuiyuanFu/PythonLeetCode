# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (42.62%)
# Likes:    1226
# Dislikes: 146
# Total Accepted:    116.1K
# Total Submissions: 271.6K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# You are given an integer array nums consisting of n elements, and an integer
# k.
#
# Find a contiguous subarray whose length is equal to k that has the maximum
# average value and return this value. Any answer with a calculation error less
# than 10^-5 will be accepted.
#
#
# Example 1:
#
#
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#
#
# Example 2:
#
#
# Input: nums = [5], k = 1
# Output: 5.00000
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= k <= n <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找指定长度的连续子数组的平均值最大。
# 滑动窗口。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k - 1])
        res = -10000
        for i in range(k - 1, len(nums)):
            s += nums[i]
            res = max(res, s / k)
            s -= nums[i - (k - 1)]
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,12,-5,-6,50,3], k = 4')
    print('Exception :')
    print('12.75000')
    print('Output :')
    print(str(Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [5], k = 1')
    print('Exception :')
    print('5.00000')
    print('Output :')
    print(str(Solution().findMaxAverage([5], 1)))
    print()

    pass
# @lc main=end