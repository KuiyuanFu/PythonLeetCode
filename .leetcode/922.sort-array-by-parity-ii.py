# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#
# https://leetcode.com/problems/sort-array-by-parity-ii/description/
#
# algorithms
# Easy (70.63%)
# Likes:    1765
# Dislikes: 72
# Total Accepted:    185.4K
# Total Submissions: 262.4K
# Testcase Example:  '[4,2,5,7]'
#
# Given an array of integers nums, half of the integers in nums are odd, and
# the other half are even.
#
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever
# nums[i] is even, i is even.
#
# Return any answer array that satisfies this condition.
#
#
# Example 1:
#
#
# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
#
#
# Example 2:
#
#
# Input: nums = [2,3]
# Output: [2,3]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 2 * 10^4
# nums.length is even.
# Half of the integers in nums are even.
# 0 <= nums[i] <= 1000
#
#
#
# Follow Up: Could you solve it in-place?
#
#

# @lc tags=depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 奇偶分类。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        o, e = 1, 0

        while o < len(nums):
            while o < len(nums) and nums[o] % 2 == 1:
                o += 2
            while e < len(nums) and nums[e] % 2 == 0:
                e += 2
            if o < len(nums):
                nums[o], nums[e] = nums[e], nums[o]
            o += 2
            e += 2
        return nums

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [4,2,5,7]')
    print('Exception :')
    print('[4,5,2,7]')
    print('Output :')
    print(str(Solution().sortArrayByParityII([4, 2, 5, 7])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,3]')
    print('Exception :')
    print('[2,3]')
    print('Output :')
    print(str(Solution().sortArrayByParityII([2, 3])))
    print()

    pass
# @lc main=end