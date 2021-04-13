#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (47.87%)
# Likes:    11528
# Dislikes: 556
# Total Accepted:    1.4M
# Total Submissions: 2.9M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: nums = [5,4,-1,7,8]
# Output: 23
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -10^5 <= nums[i] <= 10^5
# 
# 
# 
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#
# 
#
# @lc idea=start
#
# 求数字数组的子序列的最大和。至少包括一个元素。
# 分治法，线段树，递归。
# 每一次计算局部的  左侧最优解 局部和 右侧最优解 局部最优解，通过分治法的两个子问题的解来合成更大的解。
# 很优美，但是效率不如动态规划。
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        self.nums =nums
        return self.maxSubArrayRecur(0,len(nums)-1)[3]
        pass
    def maxSubArrayRecur(self,l ,r ):
        if l ==r :
            return (self.nums[l],self.nums[l],self.nums[l],self.nums[l])

        mid = (l+r) //2 
        ll,lm,lr,lResult = self.maxSubArrayRecur(l,mid)
        rl,rm,rr,rResult = self.maxSubArrayRecur(mid +1 ,r)
        
        l = (lm + rl) if lm + rl > ll else ll
        r = (rm + lr) if rm + lr > rr else rr
        m = lm +rm
        result = max([lResult,rResult,lr+rl])
        # 左侧最优解 局部和 右侧最优解 局部最优解
        return (l,m,r,result)
        
# @lc code=end
if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(Solution().maxSubArray([1]))
    print(Solution().maxSubArray([5,4,-1,7,8]))

