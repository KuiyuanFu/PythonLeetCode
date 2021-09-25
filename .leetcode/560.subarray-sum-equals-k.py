# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.66%)
# Likes:    9064
# Dislikes: 303
# Total Accepted:    566.3K
# Total Submissions: 1.3M
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers nums and an integer k, return the total number of
# continuous subarrays whose sum equals to k.
#
#
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
#
#
#

# @lc tags=array;hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求连续子数组和为目标值的个数。
# 计算每个位置之前的和，之后通过和的差，计算区间的和。
# 使用字典存储和的个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        d = defaultdict(int)
        d[0] = 1
        res = 0
        s = 0
        for n in nums:
            s += n
            res += d[s - k]
            d[s] += 1
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1,1], k = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().subarraySum([1, 1, 1], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3], k = 3')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().subarraySum([1, 2, 3], 3)))
    print()

    pass
# @lc main=end