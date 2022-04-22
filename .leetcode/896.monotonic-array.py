# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#
# https://leetcode.com/problems/monotonic-array/description/
#
# algorithms
# Easy (58.44%)
# Likes:    1488
# Dislikes: 55
# Total Accepted:    203.2K
# Total Submissions: 347.6K
# Testcase Example:  '[1,2,2,3]'
#
# An array is monotonic if it is either monotone increasing or monotone
# decreasing.
#
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
#
# Given an integer array nums, return true if the given array is monotonic, or
# false otherwise.
#
#
# Example 1:
#
#
# Input: nums = [1,2,2,3]
# Output: true
#
#
# Example 2:
#
#
# Input: nums = [6,5,4,4]
# Output: true
#
#
# Example 3:
#
#
# Input: nums = [1,3,2]
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5
#
#
#

# @lc tags=tree

# @lc imports=start
import re
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断是否单调。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def isMonotonic(self, nums: List[int]) -> bool:

        def inc():
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True

        def dec():
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    return False
            return True

        return inc() or dec()
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,2,3]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isMonotonic([1, 2, 2, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [6,5,4,4]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isMonotonic([6, 5, 4, 4])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,3,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isMonotonic([1, 3, 2])))
    print()

    pass
# @lc main=end