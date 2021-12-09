# @lc app=leetcode id=795 lang=python3
#
# [795] Number of Subarrays with Bounded Maximum
#
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/
#
# algorithms
# Medium (52.03%)
# Likes:    1417
# Dislikes: 82
# Total Accepted:    48.3K
# Total Submissions: 92.4K
# Testcase Example:  '[2,1,4,3]\n2\n3'
#
# Given an integer array nums and two integers left and right, return the
# number of contiguous non-empty subarrays such that the value of the maximum
# array element in that subarray is in the range [left, right].
#
# The test cases are generated so that the answer will fit in a 32-bit
# integer.
#
#
# Example 1:
#
#
# Input: nums = [2,1,4,3], left = 2, right = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2,
# 1], [3].
#
#
# Example 2:
#
#
# Input: nums = [2,9,2,5,6], left = 2, right = 8
# Output: 7
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 0 <= left <= right <= 10^9
#
#
#

# @lc tags=recursion

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最大值在给定区间的子序列的个数。
# dp。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int,
                              right: int) -> int:
        res = 0
        # the range left and right count. the lower count.
        il, ir, l = 0, 0, 0
        for n in nums:
            if n > right:
                il, ir, l = 0, 0, 0
            else:
                il, l = il + 1, l + 1
                if n >= left:
                    ir = 0
                    res += l
                else:
                    ir += 1
                    res += il - ir
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,1,4,3], left = 2, right = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().numSubarrayBoundedMax([2, 1, 4, 3], 2, 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,9,2,5,6], left = 2, right = 8')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().numSubarrayBoundedMax([2, 9, 2, 5, 6], 2, 8)))
    print()

    pass
# @lc main=end