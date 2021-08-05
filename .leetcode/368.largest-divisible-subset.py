# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (38.71%)
# Likes:    2090
# Dislikes: 95
# Total Accepted:    117.6K
# Total Submissions: 303.5K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct positive integers nums, return the largest subset
# answer such that every pair (answer[i], answer[j]) of elements in this subset
# satisfies:
#
#
# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
#
#
# If there are multiple solutions, return any of them.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.
#
#
# Example 2:
#
#
# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 10^9
# All the integers in nums are unique.
#
#
#

# @lc tags=math;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给整数数组，求最长的整除自己，满足相邻两个元素可以整除。
# 动态规划，n^2.
# 排序是关键。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        S = {-1: set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
        return list(max(S.values(), key=len))


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().largestDivisibleSubset([1, 2, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,4,8]')
    print('Exception :')
    print('[1,2,4,8]')
    print('Output :')
    print(str(Solution().largestDivisibleSubset([1, 2, 4, 8])))
    print()

    pass
# @lc main=end