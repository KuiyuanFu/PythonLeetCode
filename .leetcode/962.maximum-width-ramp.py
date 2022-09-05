# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#
# https://leetcode.com/problems/maximum-width-ramp/description/
#
# algorithms
# Medium (48.75%)
# Likes:    1284
# Dislikes: 38
# Total Accepted:    35.9K
# Total Submissions: 73.7K
# Testcase Example:  '[6,0,8,2,1,5]'
#
# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i]
# <= nums[j]. The width of such a ramp is j - i.
#
# Given an integer array nums, return the maximum width of a ramp in nums. If
# there is no ramp in nums, return 0.
#
#
# Example 1:
#
#
# Input: nums = [6,0,8,2,1,5]
# Output: 4
# Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] =
# 0 and nums[5] = 5.
#
#
# Example 2:
#
#
# Input: nums = [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] =
# 1 and nums[9] = 1.
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 5 * 10^4
# 0 <= nums[i] <= 5 * 10^4
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，如果后者大约等于前者可以形成一个斜面，宽度为索引差，求最大索引差。
# 栈，保留递减序列。因为如果此元素大于之前元素，那么之后的元素与之前元素形成的宽度，一定会大于与这个元素形成的宽度。
# 再从后向前遍历，如果此元素大于一个在栈中的元素，那么在此元素前的所有元素，与栈中元素形成的宽度一定会小于与这个元素形成的宽度。就可以弹出了。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0
        s = [(nums[0], 0)]
        for idx in range(1, len(nums)):
            n = nums[idx]
            if n < s[-1][0]:
                s.append((n, idx))
        for idx in range(len(nums) - 1, 0, -1):
            n = nums[idx]
            while len(s) > 0 and s[-1][0] <= n:
                idxLeft = s[-1][1]
                res = max(res, idx - idxLeft)
                s.pop()
            if len(s) == 0:
                break

        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [8,8,0,4,1,1,0,1,0,0]')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().maxWidthRamp([8, 8, 0, 4, 1, 1, 0, 1, 0, 0])))
    print()

    print('Example 1:')
    print('Input : ')
    print('nums = [6,0,8,2,1,5]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().maxWidthRamp([6, 0, 8, 2, 1, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [9,8,1,0,1,9,4,0,4,1]')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1])))
    print()

    pass
# @lc main=end