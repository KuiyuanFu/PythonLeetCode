# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Medium (43.44%)
# Likes:    7292
# Dislikes: 199
# Total Accepted:    735K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 2:
#
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 抢劫，给定一个街区的连续房子，不能抢相邻的两个房子，求最大的收益。
# 直接动态规划。对于每一个房子，其最大累计收益，若是抢劫上一个房子，那么就不会抢劫此房子；如果抢劫此房子，那么就需要判断是抢劫前第二个还是第三个；不需要判断前第四个，因为如果抢第四个，那么就还可以抢第二个，所以一定不会是第四个。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        nums[2] = max(nums[1], nums[2] + nums[0])
        for i in range(3, len(nums)):
            nums[i] = max(nums[i - 1], nums[i] + max(nums[i - 2], nums[i - 3]))
        return nums[-1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().rob([2, 1, 1, 2])))
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,1]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().rob([1, 2, 3, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,7,9,3,1]')
    print('Exception :')
    print('12')
    print('Output :')
    print(str(Solution().rob([2, 7, 9, 3, 1])))
    print()

    pass
# @lc main=end