# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (42.22%)
# Likes:    1613
# Dislikes: 280
# Total Accepted:    250.7K
# Total Submissions: 593.7K
# Testcase Example:  '[1,3,5]'
#
# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,4,4,5,6,7] might
# become:
#
#
# [4,5,6,7,0,1,4] if it was rotated 4 times.
# [0,1,4,4,5,6,7] if it was rotated 7 times.
#
#
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums that may contain duplicates, return the
# minimum element of this array.
#
# You must decrease the overall operation steps as much as possible.
#
#
# Example 1:
# Input: nums = [1,3,5]
# Output: 1
# Example 2:
# Input: nums = [2,2,2,0,1]
# Output: 0
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# nums is sorted and rotated between 1 and n times.
#
#
#
# Follow up: This problem is similar to Find Minimum in Rotated Sorted Array,
# but nums may contain duplicates. Would this affect the runtime complexity?
# How and why?
#
#
#
#

# @lc tags=array;binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个数组，这个数组是有序数组经过n次旋转得到的，即向后循环移动n次。有重复元素。
# 求最小值。
# 直接二分法。需要考虑重复元素。
# 遇到重复元素，可以将边界缩小，由于重复，所以不会将最小值去掉。
#
# @lc idea=end

# @lc group=array;binary-search

# @lc rank=10

# @lc code=start


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            # reduce range
            else:
                right -= 1

        return nums[left]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,5]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findMin([1, 3, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,2,2,0,1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().findMin([2, 2, 2, 0, 1])))
    print()

    pass
# @lc main=end