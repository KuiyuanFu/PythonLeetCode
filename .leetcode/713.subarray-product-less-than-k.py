# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#
# https://leetcode.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (41.34%)
# Likes:    2990
# Dislikes: 106
# Total Accepted:    125.1K
# Total Submissions: 298.2K
# Testcase Example:  '[10,5,2,6]\n100'
#
# Given an array of integers nums and an integer k, return the number of
# contiguous subarrays where the product of all the elements in the subarray is
# strictly less than k.
#
#
# Example 1:
#
#
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly
# less than k.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3], k = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# 1 <= nums[i] <= 1000
# 0 <= k <= 10^6
#
#
#

# @lc tags=array;two-pointers

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求连续子数组元素乘积严格小于给定值的个数。
# 滑动窗口s
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        p = 1
        l = 0
        for r in range(len(nums)):
            p = p * nums[r]
            while p >= k and l <= r:
                p //= nums[l]
                l += 1
            res += r - l + 1
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [10,5,2,6], k = 100')
    print('Exception :')
    print('8')
    print('Output :')
    print(str(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3], k = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().numSubarrayProductLessThanK([1, 2, 3], 0)))
    print()

    pass
# @lc main=end