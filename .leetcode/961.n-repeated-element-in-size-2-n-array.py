# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/
#
# algorithms
# Easy (75.70%)
# Likes:    995
# Dislikes: 306
# Total Accepted:    187K
# Total Submissions: 247K
# Testcase Example:  '[1,2,3,3]'
#
# You are given an integer array nums with the following properties:
#
#
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
#
#
# Return the element that is repeated n times.
#
#
# Example 1:
# Input: nums = [1,2,3,3]
# Output: 3
# Example 2:
# Input: nums = [2,1,2,5,3,2]
# Output: 2
# Example 3:
# Input: nums = [5,1,5,2,5,3,5,4]
# Output: 5
#
#
# Constraints:
#
#
# 2 <= n <= 5000
# nums.length == 2 * n
# 0 <= nums[i] <= 10^4
# nums contains n + 1 unique elements and one of them is repeated exactly n
# times.
#
#
#

# @lc tags=two-pointers;string

# @lc imports=start
import re
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，长2n，有一个元素重复n次，其他唯一。求这个元素。
# 重复元素必定出现在一个连续三元组中。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums) - 2):
            if nums[i] == nums[i + 1] or nums[i] == nums[i + 2]:
                return nums[i]
        if nums[-1] == nums[-2] or nums[-2] == nums[0]:
            return nums[-2]
        if nums[-1] == nums[1 % len(nums)] or nums[-1] == nums[0]:
            return nums[-1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,3]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().repeatedNTimes([1, 2, 3, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,1,2,5,3,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().repeatedNTimes([2, 1, 2, 5, 3, 2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [5,1,5,2,5,3,5,4]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4])))
    print()

    pass
# @lc main=end