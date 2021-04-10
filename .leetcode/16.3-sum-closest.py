#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (46.33%)
# Likes:    3080
# Dislikes: 169
# Total Accepted:    570.4K
# Total Submissions: 1.2M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
#
#
# Example 1:
#
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 =
# 2).
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
#
#
#

# @lc idea=start
# 使用回溯和备忘录方法，每一次经过一个索引，分成两部分，一个是使用这个值，另一个是不使用。使用次数为3时，就返回和，之后判断差值。
#
# @lc idea=end

from typing import *


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

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
        self.target = target
        self.memory = {}
        return self.recursion(0, 0, 0)
    # 现在的索引 已经使用的次数  和
    def recursion(self, index: int, times: int, n: int):

        if times == 3:
            return n
        if index == len(self.nums):
            return float('inf')
        if (index, times, n) in self. memory:
            return self.memory[(index, times, n)]
        # 不使用当前的值
        resultFirst = self.recursion(index+1, times, n)
        # 使用了当前的值
        resultSecond = self.recursion(index+1, times + 1, n + self.nums[index])

        result = resultFirst if abs(
            resultFirst - self.target) < abs(resultSecond - self.target) else resultSecond
        self.memory[(index, times, n)] = result
        return result

# @lc code=end


if __name__ == '__main__':
    print(Solution().threeSumClosest([0, 0, 0], 1))
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
