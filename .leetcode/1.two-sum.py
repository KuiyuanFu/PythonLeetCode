#
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

# @lc idea=start
#
# 目的是求和为 target 的两个数字的索引。使用一个d ic 存储数字与其索引的键值对。这样每读取一个数字时，判断 dic中是否已经有与其和为 target 的数字，若有就可以在字典中直接读取另一个数字的索引，之后直接输出。
#
# @lc idea=end

from typing import *

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
