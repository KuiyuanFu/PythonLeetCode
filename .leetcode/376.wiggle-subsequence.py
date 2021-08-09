# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#
# https://leetcode.com/problems/wiggle-subsequence/description/
#
# algorithms
# Medium (42.77%)
# Likes:    1964
# Dislikes: 82
# Total Accepted:    110.7K
# Total Submissions: 258.4K
# Testcase Example:  '[1,7,4,9,2,5]'
#
# A wiggle sequence is a sequence where the differences between successive
# numbers strictly alternate between positive and negative. The first
# difference (if one exists) may be either positive or negative. A sequence
# with one element and a sequence with two non-equal elements are trivially
# wiggle sequences.
#
#
# For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences
# (6, -3, 5, -7, 3) alternate between positive and negative.
# In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences.
# The first is not because its first two differences are positive, and the
# second is not because its last difference is zero.
#
#
# A subsequence is obtained by deleting some elements (possibly zero) from the
# original sequence, leaving the remaining elements in their original order.
#
# Given an integer array nums, return the length of the longest wiggle
# subsequence of nums.
#
#
# Example 1:
#
#
# Input: nums = [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence with differences (6,
# -3, 5, -7, 3).
#
#
# Example 2:
#
#
# Input: nums = [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length.
# One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,4,5,6,7,8,9]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#
#
#
# Follow up: Could you solve this in O(n) time?
#
#

# @lc tags=dynamic-programming;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一个列表转化为一低一高交替的序列，只能删除元素，求剩下的最长的序列长度。
# 直接动态规划
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        f = True
        for j in range(1, len(nums)):
            if nums[j] != nums[0]:
                f = nums[0] < nums[j]
                break

        v, l, = nums[0], 1
        for i in range(1, len(nums)):
            n = nums[i]
            if f:
                if n > v:
                    v, l, f = n, l + 1, not f
                else:
                    v = min(v, n)
            else:
                if n < v:
                    v, l, f = n, l + 1, not f
                else:
                    v = max(v, n)
        return l


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().wiggleMaxLength([1, 1, 7, 4, 9, 2, 5])))
    print('Example 1:')
    print('Input : ')
    print('nums = [1,7,4,9,2,5]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().wiggleMaxLength([1, 7, 4, 9, 2, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,17,5,10,13,15,10,5,16,8]')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16,
                                          8])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,2,3,4,5,6,7,8,9]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9])))
    print()

    pass
# @lc main=end