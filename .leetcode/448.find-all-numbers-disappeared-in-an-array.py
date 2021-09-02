# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (56.91%)
# Likes:    4743
# Dislikes: 327
# Total Accepted:    423.9K
# Total Submissions: 743.4K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in
# nums.
#
#
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
# Input: nums = [1,1]
# Output: [2]
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n
#
#
#
# Follow up: Could you do it without extra space and in O(n) runtime? You may
# assume the returned list does not count as extra space.
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 在n长的数组中，元素值满足1-n，找1-n中没有出现的值。
# 直接负数标记。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [4,3,2,7,8,2,3,1]')
    print('Exception :')
    print('[5,6]')
    print('Output :')
    print(str(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,1]')
    print('Exception :')
    print('[2]')
    print('Output :')
    print(str(Solution().findDisappearedNumbers([1, 1])))
    print()

    pass
# @lc main=end