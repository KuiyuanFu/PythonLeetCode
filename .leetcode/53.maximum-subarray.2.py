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

# @lc tags=array;divide-and-conquer;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求数字数组的子序列的最大和。至少包括一个元素。
# 动态规划。dp保存包括当前的最优解，max 是全局最优解。
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=10


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            dp = n if dp < 0 else (n + dp)
            result = max(dp, result)
        return result

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-2,1,-3,4,-1,2,1,-5,4]')
    print('Output :')
    print(str(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])))
    print('Exception :')
    print('6')
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1]')
    print('Output :')
    print(str(Solution().maxSubArray([1])))
    print('Exception :')
    print('1')
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [5,4,-1,7,8]')
    print('Output :')
    print(str(Solution().maxSubArray([5, 4, -1, 7, 8])))
    print('Exception :')
    print('23')
    print()

    pass
# @lc main=end