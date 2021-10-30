# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
# https://leetcode.com/problems/find-pivot-index/description/
#
# algorithms
# Easy (48.40%)
# Likes:    2365
# Dislikes: 341
# Total Accepted:    244.4K
# Total Submissions: 496.8K
# Testcase Example:  '[1,7,3,6,5,6]'
#
# Given an array of integers nums, calculate the pivot index of this array.
#
# The pivot index is the index where the sum of all the numbers strictly to the
# left of the index is equal to the sum of all the numbers strictly to the
# index's right.
#
# If the index is on the left edge of the array, then the left sum is 0 because
# there are no elements to the left. This also applies to the right edge of the
# array.
#
# Return the leftmost pivot index. If no such index exists, return -1.
#
#
# Example 1:
#
#
# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11
#
#
# Example 2:
#
#
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
#
# Example 3:
#
#
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -1000 <= nums[i] <= 1000
#
#
#
# Note: This question is the same as 1991:
# https://leetcode.com/problems/find-the-middle-index-in-array/
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找使左右两侧和相等的索引。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l, r = 0, sum(nums)

        for i, n in enumerate(nums):
            r -= n
            if l == r:
                return i
            l += n

        return -1
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,7,3,6,5,6]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().pivotIndex([1, 7, 3, 6, 5, 6])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().pivotIndex([1, 2, 3])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [2,1,-1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().pivotIndex([2, 1, -1])))
    print()

    pass
# @lc main=end