# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (46.60%)
# Likes:    3593
# Dislikes: 310
# Total Accepted:    607.9K
# Total Submissions: 1.3M
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,2,4,5,6,7] might
# become:
#
#
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
#
#
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums of unique elements, return the minimum
# element of this array.
#
# You must write an algorithm that runs in O(log n) time.
#
#
# Example 1:
#
#
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
#
#
# Example 2:
#
#
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4
# times.
#
#
# Example 3:
#
#
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4
# times.
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.
#
#
#

# @lc tags=array;binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个数组，这个数组是有序数组经过n次旋转得到的，即向后循环移动n次。无重复元素。
# 求最小值。
# 直接二分法。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def recur(self, l, r):

        if r - l <= 1:
            return min(self.nums[l], self.nums[r])
        if self.nums[l] < self.nums[r]:
            return self.nums[l]
        m = (r + l) // 2
        if self.nums[l] > self.nums[m]:
            return self.recur(l, m)
        else:
            return self.recur(m, r)

    def findMin(self, nums: List[int]) -> int:
        self.nums = nums
        return self.recur(0, len(nums) - 1)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,4,5,1,2]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findMin([3, 4, 5, 1, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [4,5,6,7,0,1,2]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().findMin([4, 5, 6, 7, 0, 1, 2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [11,13,15,17]')
    print('Exception :')
    print('11')
    print('Output :')
    print(str(Solution().findMin([11, 13, 15, 17])))
    print()

    pass
# @lc main=end