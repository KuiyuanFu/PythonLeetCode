#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (28.25%)
# Likes:    10060
# Dislikes: 1037
# Total Accepted:    1.3M
# Total Submissions: 4.4M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
#
#
# Constraints:
#
#
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#
#
# @lc idea=start
#
# 返回所有三元组，满足和为0。由于要求不能重复，需要有重复校验。最简单就是三重循环，这样复杂度太高了。由于是三个数，所以时间复杂度不可能太低。
# 这样使用
#
# @lc idea=end

from typing import *

# @lc code=start


class Solution:


    def threeSum(self, nums: List[int]) -> List[List[int]]:

        dic = {}
        for n in nums:
            if not dic.__contains__(n):
                dic[n] = 0
            if dic[n] < 3:
                dic[n] += 1
        nums = []
        for i in list(dic.keys()):
            nums += [i]*dic[i]

        self.nums = nums
        sumToString = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                n = nums[i] + nums[j]
                if not sumToString.__contains__(n):
                    sumToString[n] = []
                sumToString[n].append([i, j])

        results = {}
        for i in range(len(nums)):
            n = - nums[i]
            if sumToString.__contains__(n):
                for l in sumToString[n]:
                    if i not in l:
                        t = l.copy()
                        t.append(i)
                        t.sort()
                        t = [self.nums[i] for i in t]

                        results[self.listToString(t)] = t
        return list(results.values())
    
    def listToString(self, l: List[int]) -> str:
        return '#'.join([str(i) for i in l])

# @lc code=end


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
