# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#
# https://leetcode.com/problems/arithmetic-slices/description/
#
# algorithms
# Medium (60.33%)
# Likes:    2011
# Dislikes: 208
# Total Accepted:    141.1K
# Total Submissions: 233.4K
# Testcase Example:  '[1,2,3,4]'
#
# An integer array is called arithmetic if it consists of at least three
# elements and if the difference between any two consecutive elements is the
# same.
#
#
# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic
# sequences.
#
#
# Given an integer array nums, return the number of arithmetic subarrays of
# nums.
#
# A subarray is a contiguous subsequence of the array.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and
# [1,2,3,4] itself.
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000
#
#
#

# @lc tags=math;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
#  判断一个数字序列有多少个等差序列。
# 记录每个等差序列的长度，之后等差求和。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return 0
        res = 0
        nums.append(nums[-1] + nums[-1] - nums[-2] + 1)
        d = nums[1] - nums[0]
        np = nums[0] - d
        l = 0
        for n in nums:
            if n - np == d:
                l += 1
            else:
                if l >= 3:
                    l = l - 2
                    res += (1 + l) * l // 2
                d = n - np
                l = 2
            np = n
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().numberOfArithmeticSlices([-1, 0, 1])))
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,4]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().numberOfArithmeticSlices([1, 2, 3, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().numberOfArithmeticSlices([1])))
    print()

    pass
# @lc main=end