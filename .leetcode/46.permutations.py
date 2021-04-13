#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (67.05%)
# Likes:    5779
# Dislikes: 134
# Total Accepted:    793.9K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3]'
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.
# 
# 
#
# 
#
# @lc idea=start
#
# 给定数组，返回所有排列，没有重复数字。
# 递归，插入。就是在子任务的结果上，每一个排列的任意位置，插入当前的数字。
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) ==1 :
            return [nums]
        n = nums.pop()
        results = []
        for l in self.permute(nums):
            for i in range(len(l)+1):
                lT =l.copy()
                lT.insert(i,n)
                results.append(lT)
        return results

        
# @lc code=end
if __name__ == '__main__':
    print(Solution().permute([1]))
    print(Solution().permute([1,2]))
    print(Solution().permute([1,2,3]))

