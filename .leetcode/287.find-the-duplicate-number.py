# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (58.18%)
# Likes:    8140
# Dislikes: 851
# Total Accepted:    554.7K
# Total Submissions: 954K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array of integers nums containing n + 1 integers where each integer
# is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and uses only
# constant extra space.
#
#
# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:
# Input: nums = [1,1]
# Output: 1
# Example 4:
# Input: nums = [1,1,2]
# Output: 1
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer
# which appears two or more times.
#
#
#
# Follow up:
#
#
# How can we prove that at least one duplicate number must exist in nums?
# Can you solve the problem in linear runtime complexity?
#
#
#

# @lc tags=array;two-pointers;binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，n+1个数字，分布在1-n中，只有一个数字是重复的，找到这个。
# 快慢指针。
#
# @lc idea=end

# @lc group=array;two-pointers

# @lc rank=7


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,4,2,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findDuplicate([1, 3, 4, 2, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [3,1,3,4,2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findDuplicate([3, 1, 3, 4, 2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findDuplicate([1, 1])))
    print()

    print('Example 4:')
    print('Input : ')
    print('nums = [1,1,2]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findDuplicate([1, 1, 2])))
    print()

    pass
# @lc main=end