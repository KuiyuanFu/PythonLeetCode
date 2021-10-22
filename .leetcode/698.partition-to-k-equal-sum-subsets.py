# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (45.25%)
# Likes:    3960
# Dislikes: 231
# Total Accepted:    165.5K
# Total Submissions: 361.6K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an integer array nums and an integer k, return true if it is possible
# to divide this array into k non-empty subsets whose sums are all equal.
#
#
# Example 1:
#
#
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4], k = 3
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 16
# 1 <= nums[i] <= 10^4
# The frequency of each element is in the range [1, 4].
#
#
#

# @lc tags=dynamic-programming;recursion

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断是否可以将数组分成k个和相等的子集。
# 排序，递归。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        s = sum(nums)
        if s // k * k != s:
            return False
        target = s // k

        nums.sort(reverse=True)
        length = len(nums)
        dp = [True] * length

        def recur(t, idx):
            if t == 0:
                return True
            if t < 0:
                return False
            if idx == length:
                return False

            if dp[idx]:
                dp[idx] = False

                if recur(t - nums[idx], idx + 1):
                    return True
                dp[idx] = True

            return recur(t, idx + 1)

        for _ in range(k):
            if not recur(target, 0):
                return False
        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [4,3,2,3,5,2,1], k = 4')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4], k = 3')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canPartitionKSubsets([1, 2, 3, 4], 3)))
    print()

    pass
# @lc main=end