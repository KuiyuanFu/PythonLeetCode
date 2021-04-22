# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (33.71%)
# Likes:    2075
# Dislikes: 578
# Total Accepted:    301.7K
# Total Submissions: 894.8K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# There is an integer array nums sorted in non-decreasing order (not
# necessarily with distinct values).
#
# Before being passed to your function, nums is rotated at an unknown pivot
# index k (0 <= k < nums.length) such that the resulting array is [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
# example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become
# [4,5,6,6,7,0,1,2,4,4].
#
# Given the array nums after the rotation and an integer target, return true if
# target is in nums, or false if it is not in nums.
#
#
# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums is guaranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
#
#
#
# Follow up: This problem is the same as Search in Rotated Sorted Array, where
# nums may contain duplicates. Would this affect the runtime complexity? How
# and why?
#

# @lc tags=array;binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 一个非减有序数组，有重复元素，在一个位置旋转，求是否一个值在这个数组中。
# 主要思想是判断是找到旋转点，再二分搜索，由于有重复元素，时间复杂度会将为 n。
#
# @lc idea=end

# @lc group=binary-search

# @lc rank=10


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        self.nums = nums
        self.target = target
        rotation = self.findRotation(0, len(nums) - 1)

        # 二分搜索
        l, r = rotation, rotation - 1 + len(nums)
        while l <= r:
            m = (l + r) // 2
            if nums[m - len(nums)] == target:
                return True
            elif nums[m - len(nums)] < target:
                l = m + 1
            else:
                r = m - 1

        return False

    def findRotation(self, l, r):
        # 长度为1 或没有旋转
        if l == r or self.nums[l] < self.nums[r]:
            return l
        # 直接是旋转位置了
        m = (l + r) // 2
        if self.nums[m] > self.nums[m + 1]:
            return m + 1

        # 在左侧
        if self.nums[m] < self.nums[r]:
            return self.findRotation(l, m)
        # 在右侧
        elif self.nums[m] > self.nums[l]:
            return self.findRotation(m + 1, r)
        else:
            # 先看是否在右侧
            rResult = self.findRotation(m + 1, r)
            if rResult != m + 1:
                return rResult
            else:
                # 不是的话就只能在左侧了。
                return self.findRotation(l, m)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().search([0,1,1,1,2,2], 0)))
    print(str(Solution().search([1, 3, 5], 5)))
    print(
        str(Solution().search(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2)))

    print('Example 1:')
    print('Input : ')
    print('nums = [2,5,6,0,0,1,2], target = 0')
    print('Output :')
    print(str(Solution().search([2, 5, 6, 0, 0, 1, 2], 0)))
    print('Exception :')
    print('true')
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,5,6,0,0,1,2], target = 3')
    print('Output :')
    print(str(Solution().search([2, 5, 6, 0, 0, 1, 2], 3)))
    print('Exception :')
    print('false')
    print()

    pass
# @lc main=end