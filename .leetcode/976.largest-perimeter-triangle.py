# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#
# https://leetcode.com/problems/largest-perimeter-triangle/description/
#
# algorithms
# Easy (52.60%)
# Likes:    1365
# Dislikes: 202
# Total Accepted:    107.3K
# Total Submissions: 204K
# Testcase Example:  '[2,1,2]'
#
# Given an integer array nums, return the largest perimeter of a triangle with
# a non-zero area, formed from three of these lengths. If it is impossible to
# form any triangle of a non-zero area, return 0.
#
#
# Example 1:
#
#
# Input: nums = [2,1,2]
# Output: 5
#
#
# Example 2:
#
#
# Input: nums = [1,2,1]
# Output: 0
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^6
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定三条边，求三角形周长
# 排序，遍历
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for idx in range(len(nums) - 2):
            i, j, k = nums[idx], nums[idx + 1], nums[idx + 2],
            if i < j + k:
                return i + j + k
        return 0

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,1,2]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().largestPerimeter([2, 1, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().largestPerimeter([1, 2, 1])))
    print()

    pass
# @lc main=end