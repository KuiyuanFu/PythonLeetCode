# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (58.82%)
# Likes:    5901
# Dislikes: 177
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#
# Follow up: Could you minimize the total number of operations done?
#

# @lc tags=array;two-pointers

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，将0移动到末尾，稳定原地。
# 直接遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r, n in enumerate(nums):
            if n != 0:
                nums[l] = n
                l += 1
        while l < len(nums):
            nums[l] = 0
            l += 1
        return nums
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [0,1,0,3,12]')
    print('Exception :')
    print('[1,3,12,0,0]')
    print('Output :')
    print(str(Solution().moveZeroes([0, 1, 0, 3, 12])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().moveZeroes([0])))
    print()

    pass
# @lc main=end