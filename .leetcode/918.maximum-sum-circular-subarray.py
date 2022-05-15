# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#
# https://leetcode.com/problems/maximum-sum-circular-subarray/description/
#
# algorithms
# Medium (37.10%)
# Likes:    3160
# Dislikes: 143
# Total Accepted:    117.2K
# Total Submissions: 315K
# Testcase Example:  '[1,-2,3,-2]'
#
# Given a circular integer array nums of length n, return the maximum possible
# sum of a non-empty subarray of nums.
#
# A circular array means the end of the array connects to the beginning of the
# array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the
# previous element of nums[i] is nums[(i - 1 + n) % n].
#
# A subarray may only include each element of the fixed buffer nums at most
# once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does
# not exist i <= k1, k2 <= j with k1 % n == k2 % n.
#
#
# Example 1:
#
#
# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.
#
#
# Example 2:
#
#
# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
#
#
# Example 3:
#
#
# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
#
#
#

# @lc tags=heap

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找循环数组中，和最大的子数组。
# 重复，之后记录和与位置。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        res = -3 * 10**4
        length = len(nums)
        nums = nums + nums
        ms = [(-1, 0)]
        s = 0
        for i, n in enumerate(nums):

            if i - ms[0][0] > length:
                ms.pop(0)
            s += n
            res = max(res, s - ms[0][1])
            while len(ms) > 0 and ms[-1][1] >= s:
                ms.pop()
            ms.append((i, s))
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,-2,3,-2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().maxSubarraySumCircular([1, -2, 3, -2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [5,-3,5]')
    print('Exception :')
    print('10')
    print('Output :')
    print(str(Solution().maxSubarraySumCircular([5, -3, 5])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [-3,-2,-3]')
    print('Exception :')
    print('-2')
    print('Output :')
    print(str(Solution().maxSubarraySumCircular([-3, -2, -3])))
    print()

    pass
# @lc main=end