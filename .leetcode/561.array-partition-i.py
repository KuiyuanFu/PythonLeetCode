# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition I
#
# https://leetcode.com/problems/array-partition-i/description/
#
# algorithms
# Easy (74.43%)
# Likes:    455
# Dislikes: 85
# Total Accepted:    289.6K
# Total Submissions: 388.4K
# Testcase Example:  '[1,4,3,2]'
#
# Given an integer array nums of 2n integers, group these integers into n pairs
# (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i
# is maximized. Return the maximized sum.
#
#
# Example 1:
#
#
# Input: nums = [1,4,3,2]
# Output: 4
# Explanation: All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.
#
# Example 2:
#
#
# Input: nums = [6,2,6,5,1,2]
# Output: 9
# Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) +
# min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^4
# nums.length == 2 * n
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将给定的2n个整数，分成n组，求每组最小值的和的最大值。
# 排序，取奇数位。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([n if i % 2 == 0 else 0 for i, n in enumerate(nums)])

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,4,3,2]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().arrayPairSum([1, 4, 3, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [6,2,6,5,1,2]')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().arrayPairSum([6, 2, 6, 5, 1, 2])))
    print()

    pass
# @lc main=end