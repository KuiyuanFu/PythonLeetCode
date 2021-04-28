# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (37.46%)
# Likes:    5278
# Dislikes: 203
# Total Accepted:    680.6K
# Total Submissions: 1.8M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# Follow up: Could you write an algorithm with O(log n) runtime complexity?
#
#
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
#
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
# 求关键字在有序数组中的第一个出现的位置及最后出现的位置。
# 二分搜索，首先找到一个出现位置，之后以其为中心，分别在左右两个区域找第一次和最后一次出现位置时，利用求中位数时的加一计算，使中位数贴近已出现位置。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # 是否存在
        l, r = 0, len(nums) - 1
        while l <= r:
            midKey = (l + r) // 2
            if nums[midKey] == target:
                break
            elif nums[midKey] < target:
                l = midKey + 1
            else:
                r = midKey - 1
        if l > r:
            return [-1, -1]

        ret = []
        # 第一个位置
        l, r = 0, midKey
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                r = mid
            else:
                l = mid + 1
            pass
        ret.append(r)
        # 最后一个位置
        l, r = midKey, len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] == target:
                l = mid
            else:
                r = mid - 1
            pass
        ret.append(l)

        return ret


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [5,7,7,8,8,10], target = 8')
    print('Output :')
    print(str(Solution().searchRange([5, 7, 7, 8, 8, 10], 8)))
    print('Exception :')
    print('[3,4]')
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [5,7,7,8,8,10], target = 6')
    print('Output :')
    print(str(Solution().searchRange([5, 7, 7, 8, 8, 10], 6)))
    print('Exception :')
    print('[-1,-1]')
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [], target = 0')
    print('Output :')
    print(str(Solution().searchRange([], 0)))
    print('Exception :')
    print('[-1,-1]')
    print()

    pass
# @lc main=end