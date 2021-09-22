# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (44.29%)
# Likes:    3308
# Dislikes: 156
# Total Accepted:    202K
# Total Submissions: 455.1K
# Testcase Example:  '[0,1]'
#
# Given a binary array nums, return the maximum length of a contiguous subarray
# with an equal number of 0 and 1.
#
#
# Example 1:
#
#
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number
# of 0 and 1.
#
#
# Example 2:
#
#
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定1，0两元素的数组，求连续子数组满足1，0个数相等的最长长度。
# 记录个数差距位置的最左侧位置。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = 0
        dic = {0: -1}
        res = 0
        for i, n in enumerate(nums):
            diff += 1 if n == 1 else -1
            if diff in dic:
                res = max(res, i - dic[diff])
            else:
                dic[diff] = i
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    # print('Example 1:')
    # print('Input : ')
    # print('nums = [0,1]')
    # print('Exception :')
    # print('2')
    # print('Output :')
    # print(str(Solution().findMaxLength([0, 1])))
    # print()

    # print('Example 2:')
    # print('Input : ')
    # print('nums = [0,1,0]')
    # print('Exception :')
    # print('2')
    # print('Output :')
    # print(str(Solution().findMaxLength([0, 1, 0])))
    print()
    print(str(Solution().findMaxLength([0, 0, 1, 0, 0, 0, 1, 1])))
    pass
# @lc main=end