# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
#
# algorithms
# Easy (44.04%)
# Likes:    560
# Dislikes: 714
# Total Accepted:    135.2K
# Total Submissions: 304.7K
# Testcase Example:  '[3,6,1,0]'
#
# You are given an integer array nums where the largest integer is unique.
#
# Determine whether the largest element in the array is at least twice as much
# as every other number in the array. If it is, return the index of the largest
# element, or return -1 otherwise.
#
#
# Example 1:
#
#
# Input: nums = [3,6,1,0]
# Output: 1
# Explanation: 6 is the largest integer.
# For every other number in the array x, 6 is at least twice as big as x.
# The index of value 6 is 1, so we return 1.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4]
# Output: -1
# Explanation: 4 is less than twice the value of 3, so we return -1.
#
# Example 3:
#
#
# Input: nums = [1]
# Output: 0
# Explanation: 1 is trivially at least twice the value as any other number
# because there are no other numbers.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 50
# 0 <= nums[i] <= 100
# The largest element in nums is unique.
#
#
#

# @lc tags=array;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最大值是否是其余值最少两倍。
# 最大堆，优先队列。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        h = [(0, 0), (0, 0)]
        h.sort()
        for i, n in enumerate(nums):
            heappushpop(h, (n, i))
        if h[1][0] >= h[0][0] * 2:
            return h[1][1]
        else:
            return -1


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,6,1,0]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().dominantIndex([3, 6, 1, 0])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().dominantIndex([1, 2, 3, 4])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().dominantIndex([1])))
    print()

    pass
# @lc main=end