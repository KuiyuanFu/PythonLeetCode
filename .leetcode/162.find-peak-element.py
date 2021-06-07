# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (44.22%)
# Likes:    2985
# Dislikes: 2726
# Total Accepted:    503.9K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is strictly greater than its neighbors.
#
# Given an integer array nums, find a peak element, and return its index. If
# the array contains multiple peaks, return the index to any of the peaks.
#
# You may imagine that nums[-1] = nums[n] = -∞.
#
# You must write an algorithm that runs in O(log n) time.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
#
# Example 2:
#
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2, or index number 5 where the peak element is 6.
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.
#
#
#

# @lc tags=array;binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 寻找山峰元素，即比相邻元素大的元素。
# 要求O lgn。
# 这就需要二分法，关键是如何确定山峰的位置。
# 找到中间点后，若边界点大于其，一定有山峰。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m
        return l

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findPeakElement([1, 2, 3, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,1,3,5,6,4]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4])))
    print()

    pass
# @lc main=end