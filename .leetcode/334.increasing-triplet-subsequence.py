# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (41.01%)
# Likes:    2747
# Dislikes: 173
# Total Accepted:    216.3K
# Total Submissions: 527.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given an integer array nums, return true if there exists a triple of indices
# (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
# indices exists, return false.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
#
#
# Example 2:
#
#
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
#
#
# Example 3:
#
#
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] ==
# 4 < nums[5] == 6.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^5
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#
# Follow up: Could you implement a solution that runs in O(n) time complexity
# and O(1) space complexity?
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个数组，判断是否有三个递增的索引其元素值也是递增的。
# 记录能达到要求的递增个数的元素最小值，如果接下来元素大于这个最小值，那么递增个数就可以加一。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        length = 3
        dp = [nums[0]]
        for i in range(len(nums)):
            n = nums[i]
            dp[0] = min(n, dp[0])
            for j in range(len(dp)):
                if dp[j] < n:
                    if j + 1 == len(dp):
                        dp.append(n)
                    else:
                        dp[j + 1] = min(dp[j + 1], n)
            if len(dp) == length:
                return True
        return False

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,4,5]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().increasingTriplet([1, 2, 3, 4, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [5,4,3,2,1]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().increasingTriplet([5, 4, 3, 2, 1])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [2,1,5,0,4,6]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().increasingTriplet([2, 1, 5, 0, 4, 6])))
    print()

    pass
# @lc main=end