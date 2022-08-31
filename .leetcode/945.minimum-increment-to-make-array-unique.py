# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/
#
# algorithms
# Medium (49.49%)
# Likes:    1201
# Dislikes: 46
# Total Accepted:    57.6K
# Total Submissions: 116.3K
# Testcase Example:  '[1,2,2]'
#
# You are given an integer array nums. In one move, you can pick an index i
# where 0 <= i < nums.length and increment nums[i] by 1.
#
# Return the minimum number of moves to make every value in nums unique.
#
# The test cases are generated so that the answer fits in a 32-bit integer.
#
#
# Example 1:
#
#
# Input: nums = [1,2,2]
# Output: 1
# Explanation: After 1 move, the array could be [1, 2, 3].
#
#
# Example 2:
#
#
# Input: nums = [3,2,1,2,1,7]
# Output: 6
# Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to
# have all unique values.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
#
#
#

# @lc tags=breadth-first-search

# @lc imports=start
from threading import currentThread
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，使所有数字唯一，求最少的增加个数。
# 排序，依次安放在可以的位置上。
# 如果当前位置元素小于或等于上一个元素，那么这个元素调整为上一个元素加一。
#
# @lc idea=end

# @lc group=array

# @lc rank=10


# @lc code=start
class Solution:

    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                res += (nums[i - 1] + 1) - nums[i]
                nums[i] = (nums[i - 1] + 1)
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    # print('Example 1:')
    # print('Input : ')
    # print('nums = [1,2,2]')
    # print('Exception :')
    # print('1')
    # print('Output :')
    # print(str(Solution().minIncrementForUnique([1, 2, 2])))
    # print()

    print('Example 2:')
    print('Input : ')
    print('nums = [3,2,1,2,1,7]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7])))
    print()

    pass
# @lc main=end