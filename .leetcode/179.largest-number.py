# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (31.07%)
# Likes:    3165
# Dislikes: 326
# Total Accepted:    253.5K
# Total Submissions: 814K
# Testcase Example:  '[10,2]'
#
# Given a list of non-negative integers nums, arrange them such that they form
# the largest number.
#
# Note: The result may be very large, so you need to return a string instead of
# an integer.
#
#
# Example 1:
#
#
# Input: nums = [10,2]
# Output: "210"
#
#
# Example 2:
#
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#
#
# Example 3:
#
#
# Input: nums = [1]
# Output: "1"
#
#
# Example 4:
#
#
# Input: nums = [10]
# Output: "10"
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10^9
#
#
#

# @lc tags=sort

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key

        def cmp(l, r):

            lt, rt = l + r, r + l
            if lt < rt:
                return -1
            elif lt > rt:
                return 1
            else:
                return 0

        strs = [(str(n)) for n in nums]
        buf = reversed(sorted(strs, key=cmp_to_key(cmp)))
        result = ''.join(buf)
        if result[0] == '0':
            result = '0'
        return result


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [10,2]')
    print('Exception :')
    print('"210"')
    print('Output :')
    print(str(Solution().largestNumber([10, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [3,30,34,5,9]')
    print('Exception :')
    print('"9534330"')
    print('Output :')
    print(str(Solution().largestNumber([3, 30, 34, 5, 9])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('"1"')
    print('Output :')
    print(str(Solution().largestNumber([1])))
    print()

    print('Example 4:')
    print('Input : ')
    print('nums = [10]')
    print('Exception :')
    print('"10"')
    print('Output :')
    print(str(Solution().largestNumber([10])))
    print()

    pass
# @lc main=end