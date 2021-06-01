# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (66.95%)
# Likes:    6362
# Dislikes: 205
# Total Accepted:    1.2M
# Total Submissions: 1.8M
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
#
#
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
# Input: nums = [1]
# Output: 1
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# Each element in the array appears twice except for one element which appears
# only once.
#
#
#

# @lc tags=hash-table;bit-manipulation

# @lc imports=start
from tkinter import N
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个数字数组，只有一个数字出现一次，其他出现两次，找到这个。
# 直接异或。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for n in nums:
            r ^= n
        return r
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,2,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().singleNumber([2, 2, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [4,1,2,1,2]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().singleNumber([4, 1, 2, 1, 2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().singleNumber([1])))
    print()

    pass
# @lc main=end