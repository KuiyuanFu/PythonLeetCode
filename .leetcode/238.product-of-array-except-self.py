# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (61.47%)
# Likes:    7842
# Dislikes: 574
# Total Accepted:    804.9K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,4]'
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
#
#
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#
#
# Follow up: Can you solve the problem in O(1) extra space complexity? (The
# output array does not count as extra space for space complexity analysis.)
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 对于数组中每个元素，求其他元素的乘积。
# 先考虑0的个数，两个就结果全为0，一个就只有结果一个不为零，没有就全不为0.
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = nums.count(0)
        if n >= 2:
            return [0] * len(nums)
        elif n == 1:
            r = [0] * len(nums)
            index = nums.index(0)
            r[index] = 1
            for i in list(range(0, index)) + list(range(index + 1, len(nums))):
                r[index] *= nums[i]
            return r
        else:
            from functools import reduce
            pro = reduce(lambda x, y: x * y, nums)
            return [pro // n for n in nums]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,4]')
    print('Exception :')
    print('[24,12,8,6]')
    print('Output :')
    print(str(Solution().productExceptSelf([1, 2, 3, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [-1,1,0,-3,3]')
    print('Exception :')
    print('[0,0,9,0,0]')
    print('Output :')
    print(str(Solution().productExceptSelf([-1, 1, 0, -3, 3])))
    print()

    pass
# @lc main=end