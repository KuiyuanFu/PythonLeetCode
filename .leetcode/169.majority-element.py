# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (60.49%)
# Likes:    5325
# Dislikes: 265
# Total Accepted:    863.1K
# Total Submissions: 1.4M
# Testcase Example:  '[3,2,3]'
#
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You
# may assume that the majority element always exists in the array.
#
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
#

# @lc tags=array;divide-and-conquer;bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定n个元素序列，求出现次数大于 n/2 的主元素。
# 主要利用次数，记录当前字符出现次数，遇到不是的，次数减一，到零更换元素。由于主元素大于一半，所以最后剩下的就是主元素。
#
# @lc idea=end

# @lc group=array

# @lc rank=10


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == major:
                count += 1
            else:
                count -= 1
                if count == 0:
                    major = nums[i]
                    count = 1
        return major
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,2,3]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().majorityElement([3, 2, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,2,1,1,1,2,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])))
    print()

    pass
# @lc main=end