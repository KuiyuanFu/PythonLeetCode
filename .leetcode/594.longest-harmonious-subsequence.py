# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#
# https://leetcode.com/problems/longest-harmonious-subsequence/description/
#
# algorithms
# Easy (51.84%)
# Likes:    1326
# Dislikes: 137
# Total Accepted:    104.3K
# Total Submissions: 200.9K
# Testcase Example:  '[1,3,2,2,5,2,3,7]'
#
# We define a harmonious array as an array where the difference between its
# maximum value and its minimum value is exactly 1.
#
# Given an integer array nums, return the length of its longest harmonious
# subsequence among all its possible subsequences.
#
# A subsequence of array is a sequence that can be derived from the array by
# deleting some or no elements without changing the order of the remaining
# elements.
#
#
# Example 1:
#
#
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4]
# Output: 2
#
#
# Example 3:
#
#
# Input: nums = [1,1,1,1]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最长绝对值差一的子序列。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for k in d.keys():
            if k + 1 in d:
                res = max(res, d[k] + d[k + 1])
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,2,2,5,2,3,7]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findLHS([1, 3, 2, 2, 5, 2, 3, 7])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findLHS([1, 2, 3, 4])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,1,1,1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().findLHS([1, 1, 1, 1])))
    print()

    pass
# @lc main=end