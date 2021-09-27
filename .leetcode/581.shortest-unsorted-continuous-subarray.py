# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Medium (33.36%)
# Likes:    4384
# Dislikes: 193
# Total Accepted:    193.6K
# Total Submissions: 579K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array nums, you need to find one continuous subarray that if
# you only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order.
#
# Return the shortest such subarray and output its length.
#
#
# Example 1:
#
#
# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4]
# Output: 0
#
#
# Example 3:
#
#
# Input: nums = [1]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5
#
#
#
# Follow up: Can you solve it in O(n) time complexity?
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求最短的连续子数组，使仅需要排序这一段，就可以使整个数组升序。
# 两次遍历，从左向右，保留最大值，如果大于之前的最大值，就合法。从右向左，保留最小值，小于最小值，合法。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        maxN = nums[0] - 1
        l = 0
        for n in nums:
            if n >= maxN:
                maxN = n
                l += 1
            else:
                l = 0
        minN = nums[-1] + 1
        r = 0
        for n in reversed(nums):
            if n <= minN:
                minN = n
                r += 1
            else:
                r = 0
        return len(nums) - min(l + r, len(nums))


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,6,4,8,10,9,15]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().findUnsortedSubarray([1, 2, 3, 4])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().findUnsortedSubarray([1])))
    print()

    pass
# @lc main=end