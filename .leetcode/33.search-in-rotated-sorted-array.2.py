#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (36.08%)
# Likes:    7388
# Dislikes: 649
# Total Accepted:    964K
# Total Submissions: 2.7M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
#
# Prior to being passed to your function, nums is rotated at an unknown pivot
# index k (0 <= k < nums.length) such that the resulting array is [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
# example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become
# [4,5,6,7,0,1,2].
#
# Given the array nums after the rotation and an integer target, return the
# index of target if it is in nums, or -1 if it is not in nums.
#
#
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guaranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
#
#
#
# Follow up: Can you achieve this in O(log n) time complexity?
#
#
#
# @lc idea=start
#
# 求在旋转的无重复有序数组中，搜索一个关键字。
# 先使用二分法，找到旋转点，之后再使用二分法搜索。
#
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid 
        #  旋转点为最小值
        rot = r
        length = len(nums)
        l = rot 
        r = rot+length -1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid % length] == target:
                return mid % length
            elif nums[mid % length] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


# @lc code=end
if __name__ == '__main__':
    print(Solution().search([1, 3], 0))
    print(Solution().search([1, 3], 1))
    print(Solution().search([1, 3], 3))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
