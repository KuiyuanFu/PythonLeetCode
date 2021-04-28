# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (31.68%)
# Likes:    3942
# Dislikes: 176
# Total Accepted:    329.1K
# Total Submissions: 1M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers nums, you are initially positioned at
# the first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# You can assume that you can always reach the last index.
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
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
# 给定数组，数组的数字就是当前的跳跃能力，目标是跳到数组的结尾。求最小的跳跃次数。
# 贪心算法，每次跳跃看跳到当前跳跃范围内的格子中，再以这个格子跳跃能力跳一次，综合最远的跳跃距离，来确定下一次跳到哪个格子。
#
# @lc idea=end

# @lc group=greedy

# @lc rank=10


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        times = 0
        now = 0
        while True:
            jumpLength = nums[now]
            # 直接到终点了
            if now + jumpLength >= len(nums) - 1:
                times += 1
                break

            # 找到再跳跃一次距离最远的接力点
            next = now
            maxLength = 0
            for i in range(now + 1, now + 1 + jumpLength):
                if i + nums[i] > maxLength:
                    next = i
                    maxLength = i + nums[i]

            times += 1
            now = next

        return times

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,3,1,1,4]')
    print('Output :')
    print(str(Solution().jump([2, 3, 1, 1, 4])))
    print('Exception :')
    print('2')
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,3,0,1,4]')
    print('Output :')
    print(str(Solution().jump([2, 3, 0, 1, 4])))
    print('Exception :')
    print('2')
    print()

    pass
# @lc main=end