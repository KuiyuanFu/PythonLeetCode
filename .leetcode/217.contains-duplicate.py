# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (57.33%)
# Likes:    1845
# Dislikes: 853
# Total Accepted:    840.2K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,1]'
#
# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
#
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#

# @lc tags=array;hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断数组中是否有重复元素。
# 直接集合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().containsDuplicate([1, 2, 3, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().containsDuplicate([1, 2, 3, 4])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,1,1,3,3,4,3,2,4,2]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])))
    print()

    pass
# @lc main=end