# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (58.02%)
# Likes:    3236
# Dislikes: 90
# Total Accepted:    213.3K
# Total Submissions: 367.6K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
# Find this single element that appears only once.
#
# Follow up: Your solution should run in O(log n) time and O(1) space.
#
#
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 除了一个元素是不重复的，其余都是两个。已排序，求单个元素。
# 二分法。判断从偶数索引开始的两个值是否相等。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2

            f = True
            if m % 2 == 0:
                f = nums[m] == nums[m + 1]
            else:
                f = nums[m] == nums[m - 1]
            if f:
                l += 1
            else:
                r = m

        return nums[l]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1,2,3,3,4,4,8,8]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [3,3,7,7,10,11,11]')
    print('Exception :')
    print('10')
    print('Output :')
    print(str(Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])))
    print()

    pass
# @lc main=end