# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (47.40%)
# Likes:    2562
# Dislikes: 285
# Total Accepted:    187K
# Total Submissions: 393.9K
# Testcase Example:  '[1,2,3]\n4'
#
# Given an array of distinct integers nums and a target integer target, return
# the number of possible combinations that add up to target.
#
# The answer is guaranteed to fit in a 32-bit integer.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
#
#
# Example 2:
#
#
# Input: nums = [9], target = 3
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000
#
#
#
# Follow up: What if negative numbers are allowed in the given array? How does
# it change the problem? What limitation we need to add to the question to
# allow negative numbers?
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一系列不重复的数字，求达到目标的排列，每个数字可使用多次。
# 动态规划。
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=10


# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        combs = [0] * (target + 1)
        combs[0] = 1
        for i, j in product(range(1, target + 1), range(len(nums))):
            # print((i, j))
            if i - nums[j] >= 0:
                combs[i] += combs[i - nums[j]]
        return combs[-1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3], target = 4')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().combinationSum4([1, 2, 3], 4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [9], target = 3')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().combinationSum4([9], 3)))
    print()

    pass
# @lc main=end