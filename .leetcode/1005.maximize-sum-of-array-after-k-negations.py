# @lc app=leetcode id=1005 lang=python3
#
# [1005] Maximize Sum Of Array After K Negations
#
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/
#
# algorithms
# Easy (51.16%)
# Likes:    1136
# Dislikes: 87
# Total Accepted:    62.6K
# Total Submissions: 122.4K
# Testcase Example:  '[4,2,3]\n1'
#
# Given an integer array nums and an integer k, modify the array in the
# following way:
#
#
# choose an index i and replace nums[i] with -nums[i].
#
#
# You should apply this process exactly k times. You may choose the same index
# i multiple times.
#
# Return the largest possible sum of the array after modifying it in this
# way.
#
#
# Example 1:
#
#
# Input: nums = [4,2,3], k = 1
# Output: 5
# Explanation: Choose index 1 and nums becomes [4,-2,3].
#
#
# Example 2:
#
#
# Input: nums = [3,-1,0,2], k = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
#
#
# Example 3:
#
#
# Input: nums = [2,-3,-1,5,-4], k = 2
# Output: 13
# Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -100 <= nums[i] <= 100
# 1 <= k <= 10^4
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组与k，反转k任意次任意元素，求最大的和
# 排序，将负的从绝对值最大的开始，依次反转。如果还剩余次数，那么找个绝对值最小的反转。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        nums.sort()
        m = inf

        for i, n in enumerate(nums):

            if n < 0:

                if k > 0:
                    k -= 1
                    n = -n
                    nums[i] = n
                    m = min(n, m)
            else:
                m = min(n, m)
                break
        res = sum(nums)
        if k % 2 == 1:
            res -= 2 * m
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [4,2,3], k = 1')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().largestSumAfterKNegations([4, 2, 3], 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [3,-1,0,2], k = 3')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().largestSumAfterKNegations([3, -1, 0, 2], 3)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [2,-3,-1,5,-4], k = 2')
    print('Exception :')
    print('13')
    print('Output :')
    print(str(Solution().largestSumAfterKNegations([2, -3, -1, 5, -4], 2)))
    print()

    pass
# @lc main=end