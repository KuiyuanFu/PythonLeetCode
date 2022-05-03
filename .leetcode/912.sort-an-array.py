# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (61.47%)
# Likes:    2077
# Dislikes: 521
# Total Accepted:    262K
# Total Submissions: 426.5K
# Testcase Example:  '[5,2,3,1]'
#
# Given an array of integers nums, sort the array in ascending order.
#
#
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
#
#
#

# @lc tags=binary-search;random

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 排序数组。
# 根据取值范围，以空间换时间。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        times = [0] * 100001

        for n in nums:
            times[n + 50000] += 1

        res = []

        for i, t in enumerate(times):
            n = i - 50000
            for _ in range(t):
                res.append(n)
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [5,2,3,1]')
    print('Exception :')
    print('[1,2,3,5]')
    print('Output :')
    print(str(Solution().sortArray([5, 2, 3, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [5,1,1,2,0,0]')
    print('Exception :')
    print('[0,0,1,1,2,5]')
    print('Output :')
    print(str(Solution().sortArray([5, 1, 1, 2, 0, 0])))
    print()

    pass
# @lc main=end