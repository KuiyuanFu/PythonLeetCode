# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons/description/
#
# algorithms
# Hard (54.09%)
# Likes:    3898
# Dislikes: 115
# Total Accepted:    141.1K
# Total Submissions: 259.9K
# Testcase Example:  '[3,1,5,8]'
#
# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted
# with a number on it represented by an array nums. You are asked to burst all
# the balloons.
#
# If you burst the i^th balloon, you will get nums[i - 1] * nums[i] * nums[i +
# 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as
# if there is a balloon with a 1 painted on it.
#
# Return the maximum coins you can collect by bursting the balloons wisely.
#
#
# Example 1:
#
#
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#
# Example 2:
#
#
# Input: nums = [1,5]
# Output: 10
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 500
# 0 <= nums[i] <= 100
#
#
#

# @lc tags=divide-and-conquer;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个气球序列，每个气球有一个奖励值，戳破即可获得其与左右两个气球奖励值的乘积的值，求戳破所有气球后，最多可以获得的奖励值。
# 分析问题，得到结果是一个戳破的顺序，那么就会有第一个戳破的，和最后一个戳破的，最后一个戳破的气球，获得的奖励的值就是其本身的值。
# 那么就可以根据这个性质构建动态规划，或使用带备忘录的分治法。
# 动态规划。
#
# @lc idea=end

# @lc group=divide-and-conquer;dynamic-programming

# @lc rank=10


# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        length = len(nums)
        mem = [[0 for _ in range(length)] for _ in range(length)]

        for step in range(2, length):
            for l in range(0, length - step):
                r = l + step
                coins = 0
                t = nums[l] * nums[r]
                for m in range(l + 1, r):
                    coins = max(coins, mem[l][m] + t * nums[m] + mem[m][r])
                mem[l][r] = coins
        return mem[0][length - 1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().maxCoins([
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100
        ])))

    print('Example 1:')
    print('Input : ')
    print('nums = [3,1,5,8]')
    print('Exception :')
    print('167')
    print('Output :')
    print(str(Solution().maxCoins([3, 1, 5, 8])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,5]')
    print('Exception :')
    print('10')
    print('Output :')
    print(str(Solution().maxCoins([1, 5])))
    print()

    pass
# @lc main=end