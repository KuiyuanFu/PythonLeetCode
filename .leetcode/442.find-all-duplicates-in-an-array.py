# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (70.07%)
# Likes:    4131
# Dislikes: 197
# Total Accepted:    299K
# Total Submissions: 426.1K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an integer array nums of length n where all the integers of nums are in
# the range [1, n] and each integer appears once or twice, return an array of
# all the integers that appears twice.
#
# You must write an algorithm that runs in O(n) time and uses only constant
# extra space.
#
#
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:
# Input: nums = [1,1,2]
# Output: [1]
# Example 3:
# Input: nums = [1]
# Output: []
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n
# Each element in nums appears once or twice.
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求数组中出现两次的元素。
# 翻转元素值，作为标记。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [4,3,2,7,8,2,3,1]')
    print('Exception :')
    print('[2,3]')
    print('Output :')
    print(str(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,1,2]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().findDuplicates([1, 1, 2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().findDuplicates([1])))
    print()

    pass
# @lc main=end