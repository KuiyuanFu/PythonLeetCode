# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (74.81%)
# Likes:    2656
# Dislikes: 111
# Total Accepted:    437.4K
# Total Submissions: 584.7K
# Testcase Example:  '[3,1,2,4]'
#
# Given an integer array nums, move all the even integers at the beginning of
# the array followed by all the odd integers.
#
# Return any array that satisfies this condition.
#
#
# Example 1:
#
#
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be
# accepted.
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000
#
#
#

# @lc tags=array;dynamic-programming

# @lc imports=start
from asyncio import shield
from imports import *

# @lc imports=end

# @lc idea=start
#
# 奇偶排序。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        l, r = 0, len(nums) - 1
        while l < r:
            while l < r:
                if nums[l] % 2 == 0:
                    l += 1
                else:
                    break
            while l < r:
                if nums[r] % 2 == 1:
                    r -= 1
                else:
                    break
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,1,2,4]')
    print('Exception :')
    print('[2,4,3,1]')
    print('Output :')
    print(str(Solution().sortArrayByParity([3, 1, 2, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().sortArrayByParity([0])))
    print()

    pass
# @lc main=end