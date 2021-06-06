# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (33.01%)
# Likes:    7039
# Dislikes: 231
# Total Accepted:    489.6K
# Total Submissions: 1.5M
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find a contiguous non-empty subarray within the
# array that has the largest product, and return the product.
#
# It is guaranteed that the answer will fit in a 32-bit integer.
#
# A subarray is a contiguous subsequence of the array.
#
#
# Example 1:
#
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#
#

# @lc tags=array;dynamic-programming

# @lc imports=start
import re
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定整型数组，求子序列积最大值。
# 使用三个变量，记录变量，一个结果最大值，一个当前最大值，一个当前最小值。
# 遇到正数，最大值最小值都扩大；负数，最大值最小值互换；0，就为0。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r = maximum = minimum = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            maximum, minimum = maximum * n, minimum * n
            if n < 0:
                maximum, minimum = minimum, maximum
            maximum = max(maximum, n)
            minimum = min(minimum, n)
            r = max(r, maximum)
        return r
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().maxProduct([0, 2])))
    print(str(Solution().maxProduct([0, 2])))
    print(str(Solution().maxProduct([0, 2, -2, 0, 2, -2, 0, 2, -2])))
    print('Example 1:')
    print('Input : ')
    print('nums = [2,3,-2,4]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().maxProduct([2, 3, -2, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [-2,0,-1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maxProduct([-2, 0, -1])))
    print()

    pass
# @lc main=end