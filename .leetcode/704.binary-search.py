# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# https://leetcode.com/problems/binary-search/description/
#
# algorithms
# Easy (55.08%)
# Likes:    2380
# Dislikes: 79
# Total Accepted:    424.9K
# Total Submissions: 774.2K
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
#
# Example 2:
#
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All the integers in nums are unique.
# nums is sorted in ascending order.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二分搜索。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            n = nums[m]
            if n == target:
                return m
            elif n < target:
                l = m + 1
            else:
                r = m - 1
        return -1

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-1,0,3,5,9,12], target = 9')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().search([-1, 0, 3, 5, 9, 12], 9)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [-1,0,3,5,9,12], target = 2')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().search([-1, 0, 3, 5, 9, 12], 2)))
    print()

    pass
# @lc main=end