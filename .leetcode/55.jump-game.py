# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (35.24%)
# Likes:    6069
# Dislikes: 418
# Total Accepted:    613.4K
# Total Submissions: 1.7M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# 0 <= nums[i] <= 10^5
# 
# 
#
# 
#

# @lc tags=array;greedy

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 跳跃游戏，看是否能跳到终点。
# 跳跃游戏 2 的简化版。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        now = 0
        while True:
            jumpLength = nums[now]
            if (jumpLength) == 0 :
                return False
            if now + jumpLength >= len(nums)-1:
                return True
            next = now
            maxLength = 0
            for i in range(now + 1, now + 1+jumpLength):
                if i + nums[i] > maxLength:
                    next = i
                    maxLength = i + nums[i]
            now = next

   
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,3,1,1,4]')
    print('Output :')
    print(str(Solution().canJump([2,3,1,1,4])))
    print('Exception :')
    print('true')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [3,2,1,0,4]')
    print('Output :')
    print(str(Solution().canJump([3,2,1,0,4])))
    print('Exception :')
    print('false')
    print()
    
    pass
# @lc main=end