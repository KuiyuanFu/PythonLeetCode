# @lc app=leetcode id=891 lang=python3
#
# [891] Sum of Subsequence Widths
#
# https://leetcode.com/problems/sum-of-subsequence-widths/description/
#
# algorithms
# Hard (35.34%)
# Likes:    490
# Dislikes: 139
# Total Accepted:    15.1K
# Total Submissions: 42.7K
# Testcase Example:  '[2,1,3]'
#
# The width of a sequence is the difference between the maximum and minimum
# elements in the sequence.
#
# Given an array of integers nums, return the sum of the widths of all the
# non-empty subsequences of nums. Since the answer may be very large, return it
# modulo 10^9 + 7.
#
# A subsequence is a sequence that can be derived from an array by deleting
# some or no elements without changing the order of the remaining elements. For
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
#
#
# Example 1:
#
#
# Input: nums = [2,1,3]
# Output: 6
# Explanation: The subsequences are [1], [2], [3], [2,1], [2,3], [1,3],
# [2,1,3].
# The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
# The sum of these widths is 6.
#
#
# Example 2:
#
#
# Input: nums = [2]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
#
#
#

# @lc tags=greedy

# @lc imports=start
from tkinter.messagebox import NO
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求所有子序列的宽度和。子序列为顺序不变的序列。宽度为最大值与最小值的差。
# 与原始排列顺序无关。可以先排序。之后根据索引值，就知道有多少个序列以其为最小值，及最大值。
#
# @lc idea=end

# @lc group=

# @lc rank=10


# @lc code=start
class Solution:

    def sumSubseqWidths(self, nums: List[int]) -> int:
        return sum(((1 << i) - (1 << len(nums) - i - 1)) * a
                   for i, a in enumerate(sorted(nums))) % (10**9 + 7)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,1,3]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().sumSubseqWidths([2, 1, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().sumSubseqWidths([2])))
    print()

    pass
# @lc main=end