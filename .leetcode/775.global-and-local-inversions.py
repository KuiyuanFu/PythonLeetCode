# @lc app=leetcode id=775 lang=python3
#
# [775] Global and Local Inversions
#
# https://leetcode.com/problems/global-and-local-inversions/description/
#
# algorithms
# Medium (45.87%)
# Likes:    1031
# Dislikes: 286
# Total Accepted:    53.1K
# Total Submissions: 116.2K
# Testcase Example:  '[1,0,2]'
#
# You are given an integer array nums of length n which represents a
# permutation of all the integers in the range [0, n - 1].
#
# The number of global inversions is the number of the different pairs (i, j)
# where:
#
#
# 0 <= i < j < n
# nums[i] > nums[j]
#
#
# The number of local inversions is the number of indices i where:
#
#
# 0 <= i < n - 1
# nums[i] > nums[i + 1]
#
#
# Return true if the number of global inversions is equal to the number of
# local inversions.
#
#
# Example 1:
#
#
# Input: nums = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion and 1 local inversion.
#
#
# Example 2:
#
#
# Input: nums = [1,2,0]
# Output: false
# Explanation: There are 2 global inversions and 1 local inversion.
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^5
# 0 <= nums[i] < n
# All the integers of nums are unique.
# nums is a permutation of all the numbers in the range [0, n - 1].
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 全局与本地逆序。
# 全局逆序是任意逆序，本地逆序指的是相邻的逆序。
# 判断是否一样多。
# 每个值都应为其右侧第二个开始的所有值的最小值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        m = 100000
        length = len(nums)
        for i in reversed(range(length - 2)):
            m = min(m, nums[i + 2])
            if nums[i] > m:
                return False

        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,0,2]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isIdealPermutation([1, 0, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,0]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isIdealPermutation([1, 2, 0])))
    print()

    pass
# @lc main=end