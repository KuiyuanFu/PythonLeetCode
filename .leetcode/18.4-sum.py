# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (35.07%)
# Likes:    3162
# Dislikes: 406
# Total Accepted:    404.4K
# Total Submissions: 1.2M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 
# 
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 
# 
# You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# 
# 
#


# @lc tags=array;hash-table;two-pointers

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 求四个数的和为指定的值。
# 官方解法，复杂度是 n^(t -1 ) ，题目为求 t 个数的和为 target。
# 每一次降低一个数字个数，直到求两个数的和为止。
#
# @lc idea=end

# @lc group=two-pointers

# @lc rank=4

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            # 空 目标太小 目标太大  都不能成功
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                # 去重
                if i == 0 or nums[i - 1] != nums[i]:
                    # 递归求解，用之后数组中和为差值的结构，合并上此元素，组成最终结果。
                    for set in kSum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + set)
            return res
        # 双指针法求解
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0, len(nums) - 1
            while (lo < hi):
                sum = nums[lo] + nums[hi]
                if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res

        nums.sort()
        return kSum(nums, target, 4)
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,0,-1,0,-2,2], target = 0')
    print('Output :')
    print(str(Solution().fourSum([1,0,-1,0,-2,2],0)))
    print('Exception :')
    print('[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [2,2,2,2,2], target = 8')
    print('Output :')
    print(str(Solution().fourSum([2,2,2,2,2],8)))
    print('Exception :')
    print('[[2,2,2,2]]')
    print()
    
    pass
# @lc main=end