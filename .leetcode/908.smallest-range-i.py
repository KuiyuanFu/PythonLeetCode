# @lc app=leetcode id=908 lang=python3
#
# [908] Smallest Range I
#
# https://leetcode.com/problems/smallest-range-i/description/
#
# algorithms
# Easy (67.23%)
# Likes:    427
# Dislikes: 1607
# Total Accepted:    59.8K
# Total Submissions: 89K
# Testcase Example:  '[1]\n0'
#
# You are given an integer array nums and an integer k.
#
# In one operation, you can choose any index i where 0 <= i < nums.length and
# change nums[i] to nums[i] + x where x is an integer from the range [-k, k].
# You can apply this operation at most once for each index i.
#
# The score of nums is the difference between the maximum and minimum elements
# in nums.
#
# Return the minimum score of nums after applying the mentioned operation at
# most once for each index in it.
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
# Output: 0
# Explanation: Change nums to be [4, 4, 4]. The score is max(nums) - min(nums)
# = 4 - 4 = 0.
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

# @lc tags=linked-list

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 计算间隔
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k )


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1], k = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().smallestRangeI([1], 0)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,10], k = 2')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().smallestRangeI([0, 10], 2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,3,6], k = 3')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().smallestRangeI([1, 3, 6], 3)))
    print()

    pass
# @lc main=end