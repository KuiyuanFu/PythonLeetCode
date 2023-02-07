# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/
#
# algorithms
# Medium (59.54%)
# Likes:    2160
# Dislikes: 75
# Total Accepted:    59.9K
# Total Submissions: 100.6K
# Testcase Example:  '[0,6,5,2,2,5,1,9,4]\n1\n2'
#
# Given an integer array nums and two integers firstLen and secondLen, return
# the maximum sum of elements in two non-overlapping subarrays with lengths
# firstLen and secondLen.
#
# The array with length firstLen could occur before or after the array with
# length secondLen, but they have to be non-overlapping.
#
# A subarray is a contiguous part of an array.
#
#
# Example 1:
#
#
# Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with
# length 2.
#
#
# Example 2:
#
#
# Input: nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with
# length 2.
#
#
# Example 3:
#
#
# Input: nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [0,3,8]
# with length 3.
#
#
#
# Constraints:
#
#
# 1 <= firstLen, secondLen <= 1000
# 2 <= firstLen + secondLen <= 1000
# firstLen + secondLen <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求两段给定定长的子数组的最大和
# 先用一个滑动窗口，求到一个位置左侧和右侧定长的最大子数组，再用另一个滑动窗口，计算此窗口值加上左右两侧最大另一个子数组，再求最值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int,
                           secondLen: int) -> int:
        length = len(nums)
        ls = [0] * length
        s = sum(nums[:firstLen - 1])
        sm = 0
        for r in range(firstLen - 1, length):
            s += nums[r]
            sm = max(sm, s)
            ls[r] = sm
            s -= nums[r - (firstLen - 1)]
        ls = [0] + ls

        rs = [0] * length
        s = sum(nums[length - (firstLen - 1):])
        sm = 0
        for l in range(length - firstLen, -1, -1):
            s += nums[l]
            sm = max(sm, s)
            rs[l] = sm
            s -= nums[l + (firstLen - 1)]
        rs.append(0)

        res = 0
        s = sum(nums[:secondLen - 1])
        for r in range(secondLen - 1, length):
            s += nums[r]
            l = r - (secondLen - 1)
            res = max(res, s + max(ls[l], rs[r + 1]))
            s -= nums[l]

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2')
    print('Exception :')
    print('20')
    print('Output :')
    print(str(Solution().maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1,
                                            2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen = 2')
    print('Exception :')
    print('29')
    print('Output :')
    print(str(Solution().maxSumTwoNoOverlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3,
                                            2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen = 3')
    print('Exception :')
    print('31')
    print('Output :')
    print(
        str(Solution().maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4,
                                          3)))
    print()

    pass
# @lc main=end