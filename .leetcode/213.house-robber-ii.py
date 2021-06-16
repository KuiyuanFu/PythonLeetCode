# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (37.84%)
# Likes:    3011
# Dislikes: 66
# Total Accepted:    249.7K
# Total Submissions: 658.7K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have a security system connected, and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
#
#
# Example 1:
#
#
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2), because they are adjacent houses.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 3:
#
#
# Input: nums = [0]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 一个环形的街区，不能抢劫相邻的房间，最多抢多少钱。
# 对于第一个房间，有两种情况，一是抢这个，那么就不能抢最后一个；反之亦然。所以执行两次之前的方案即可。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def _rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        nums[2] = max(nums[1], nums[2] + nums[0])
        for i in range(3, len(nums)):
            nums[i] = max(nums[i - 1], nums[i] + max(nums[i - 2], nums[i - 3]))
        return nums[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        return max(self._rob(nums[:-1]), self._rob(nums[1:]))


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,3,2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().rob([2, 3, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,1]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().rob([1, 2, 3, 1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [0]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().rob([0])))
    print()

    pass
# @lc main=end