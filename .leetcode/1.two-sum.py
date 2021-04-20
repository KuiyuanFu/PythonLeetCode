# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (46.69%)
# Likes:    20189
# Dislikes: 712
# Total Accepted:    4.1M
# Total Submissions: 8.7M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
# Example 2:
#
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
# Example 3:
#
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^3
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
#
#


# @lc tags=array;hash-table

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定一个数组，求和为 target 的两个元素的索引。
# 使用一个 dic 存储元素与其索引的键值对。这样每读取一个元素时，判断 dic 中是否已经有与其和为 target 的元素，若有就可以在字典中直接读取另一个元素的索引，之后直接输出。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, n in enumerate(nums):
            if target - n in s.keys():
                return [s[target - n], i]
            else:
                s[n] = i
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,7,11,15], target = 9')
    print('Output :')
    print(str(Solution().twoSum([2,7,11,15],9)))
    print('Exception :')
    print('[0,1]Because nums[0] + nums[1] == 9, we return [0, 1].')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [3,2,4], target = 6')
    print('Output :')
    print(str(Solution().twoSum([3,2,4],6)))
    print('Exception :')
    print('[1,2]')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [3,3], target = 6')
    print('Output :')
    print(str(Solution().twoSum([3,3],6)))
    print('Exception :')
    print('[0,1]')
    print()
    
    pass
# @lc main=end