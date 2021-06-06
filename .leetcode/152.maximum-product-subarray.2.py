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
# 前面是0，则保留本身的值。
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=8


# @lc code=start
class Solution:
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
            return max(A + B)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
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