# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (39.13%)
# Likes:    1436
# Dislikes: 1447
# Total Accepted:    344.8K
# Total Submissions: 878K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and abs(i
# - j) <= k.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
#
#
#

# @lc tags=array;hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个整数序列，给定一个长度k，判断是否在k长的子序列中存在重复元素。
# 直接滑动窗口，集合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return False
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            if i - k >= 0:
                s.remove(nums[i - k])
            s.add(nums[i])
        return False


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,1], k = 3')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,0,1,1], k = 1')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,2,3,1,2,3], k = 2')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)))
    print()

    pass
# @lc main=end