# @lc app=leetcode id=910 lang=python3
#
# [910] Smallest Range II
#
# https://leetcode.com/problems/smallest-range-ii/description/
#
# algorithms
# Medium (32.67%)
# Likes:    1087
# Dislikes: 355
# Total Accepted:    33.4K
# Total Submissions: 101.8K
# Testcase Example:  '[1]\n0'
#
# You are given an integer array nums and an integer k.
#
# For each index i where 0 <= i < nums.length, change nums[i] to be either
# nums[i] + k or nums[i] - k.
#
# The score of nums is the difference between the maximum and minimum elements
# in nums.
#
# Return the minimum score of nums after changing the values at each index.
#
#
# Example 1:
#
#
# Input: nums = [1], k = 0
# Output: 0
# Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.
#
#
# Example 2:
#
#
# Input: nums = [0,10], k = 2
# Output: 6
# Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8
# - 2 = 6.
#
#
# Example 3:
#
#
# Input: nums = [1,3,6], k = 3
# Output: 3
# Explanation: Change nums to be [4, 6, 3]. The score is max(nums) - min(nums)
# = 6 - 3 = 3.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^4
# 0 <= k <= 10^4
#
#
#

# @lc tags=math;binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 可以使每个值加k或减k。求最少差。
# 分情况讨论。排序测试。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]
        l, r = nums[0] + k, nums[-1] - k

        if res == 0:
            return 0
        elif res <= k:
            return res
        elif res >= 4 * k:
            return res - 2 * k
        else:
            for i in range(len(nums) - 1):
                res = min(res, max(r, nums[i] + k) - min(l, nums[i + 1] - k))

        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().smallestRangeII([
            8038, 9111, 5458, 8483, 5052, 9161, 8368, 2094, 8366, 9164, 53,
            7222, 9284, 5059, 4375, 2667, 2243, 5329, 3111, 5678, 5958, 815,
            6841, 1377, 2752, 8569, 1483, 9191, 4675, 6230, 1169, 9833, 5366,
            502, 1591, 5113, 2706, 8515, 3710, 7272, 1596, 5114, 3620, 2911,
            8378, 8012, 4586, 9610, 8361, 1646, 2025, 1323, 5176, 1832, 7321,
            1900, 1926, 5518, 8801, 679, 3368, 2086, 7486, 575, 9221, 2993,
            421, 1202, 1845, 9767, 4533, 1505, 820, 967, 2811, 5603, 574, 6920,
            5493, 9490, 9303, 4648, 281, 2947, 4117, 2848, 7395, 930, 1023,
            1439, 8045, 5161, 2315, 5705, 7596, 5854, 1835, 6591, 2553, 8628
        ], 4643)))
    print(str(Solution().smallestRangeII([7, 8, 8, 5, 2], 4)))
    print(str(Solution().smallestRangeII([3, 1, 10], 4)))
    print('Example 1:')
    print('Input : ')
    print('nums = [1], k = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().smallestRangeII([1], 0)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,10], k = 2')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().smallestRangeII([0, 10], 2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,3,6], k = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().smallestRangeII([1, 3, 6], 3)))
    print()

    pass
# @lc main=end