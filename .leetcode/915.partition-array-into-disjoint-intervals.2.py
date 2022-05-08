# @lc app=leetcode id=915 lang=python3
#
# [915] Partition Array into Disjoint Intervals
#
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/
#
# algorithms
# Medium (48.40%)
# Likes:    1174
# Dislikes: 59
# Total Accepted:    66.1K
# Total Submissions: 136.6K
# Testcase Example:  '[5,0,3,8,6]'
#
# Given an integer array nums, partition it into two (contiguous) subarrays
# left and right so that:
#
#
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
#
#
# Return the length of left after such a partitioning.
#
# Test cases are generated such that partitioning exists.
#
#
# Example 1:
#
#
# Input: nums = [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
#
#
# Example 2:
#
#
# Input: nums = [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^6
# There is at least one valid answer for the given input.
#
#
#

# @lc tags=math;random;rejection-sampling

# @lc imports=start
import enum
from socket import errorTab
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将数组分成两部分，右侧都大于左侧。
# 一次遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:

        m, rm, res = nums[0], nums[0], 1
        for i, n in enumerate(nums):
            if n < rm:
                rm = m
                res = i + 1
            elif n > m:
                m = n

        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [5,0,3,8,6]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().partitionDisjoint([5, 0, 3, 8, 6])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,1,1,0,6,12]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().partitionDisjoint([1, 1, 1, 0, 6, 12])))
    print()

    pass
# @lc main=end