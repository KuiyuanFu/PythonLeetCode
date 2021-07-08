# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (49.04%)
# Likes:    1395
# Dislikes: 1425
# Total Accepted:    267.4K
# Total Submissions: 538.4K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n' +
# '[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, handle multiple queries of the following
# type:
#
#
# Calculate the sum of the elements of nums between indices left and right
# inclusive where left <= right.
#
#
# Implement the NumArray class:
#
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums
# between indices left and right inclusive (i.e. nums[left] + nums[left + 1] +
# ... + nums[right]).
#
#
#
# Example 1:
#
#
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]
#
# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
# 0 <= left <= right < nums.length
# At most 10^4 calls will be made to sumRange.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个整数数组，求指定范围内的和。
# 直接遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:

        return sum(self.nums[left:right + 1])


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    pass
# @lc main=end