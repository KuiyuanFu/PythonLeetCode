# @lc app=leetcode id=446 lang=python3
#
# [446] Arithmetic Slices II - Subsequence
#
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/
#
# algorithms
# Hard (34.45%)
# Likes:    809
# Dislikes: 74
# Total Accepted:    27.4K
# Total Submissions: 79.5K
# Testcase Example:  '[2,4,6,8,10]'
#
# Given an integer array nums, return the number of all the arithmetic
# subsequences of nums.
#
# A sequence of numbers is called arithmetic if it consists of at least three
# elements and if the difference between any two consecutive elements is the
# same.
#
#
# For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are
# arithmetic sequences.
# For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
#
#
# A subsequence of an array is a sequence that can be formed by removing some
# elements (possibly none) of the array.
#
#
# For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
#
#
# The test cases are generated so that the answer fits in 32-bit integer.
#
#
# Example 1:
#
#
# Input: nums = [2,4,6,8,10]
# Output: 7
# Explanation: All arithmetic subsequence slices are:
# [2,4,6]
# [4,6,8]
# [6,8,10]
# [2,4,6,8]
# [4,6,8,10]
# [2,4,6,8,10]
# [2,6,10]
#
#
# Example 2:
#
#
# Input: nums = [7,7,7,7,7]
# Output: 16
# Explanation: Any subsequence of this array is arithmetic.
#
#
#
# Constraints:
#
#
# 1  <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求可能的算数切片个数。
# 对于每个节点，维护一个此节点为最后一个节点的切片个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        buffer = [defaultdict(int) for _ in range(len(nums))]
        for i in range(1, len(nums)):
            ni = nums[i]
            for j in range(i):
                nj = nums[j]
                t = buffer[j][ni - nj]
                res += t
                buffer[i][ni - nj] += t + 1
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,4,6,8,10]')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().numberOfArithmeticSlices([2, 4, 6, 8, 10])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [7,7,7,7,7]')
    print('Exception :')
    print('16')
    print('Output :')
    print(str(Solution().numberOfArithmeticSlices([7, 7, 7, 7, 7])))
    print()

    pass
# @lc main=end