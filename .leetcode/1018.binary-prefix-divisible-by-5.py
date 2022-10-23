# @lc app=leetcode id=1018 lang=python3
#
# [1018] Binary Prefix Divisible By 5
#
# https://leetcode.com/problems/binary-prefix-divisible-by-5/description/
#
# algorithms
# Easy (47.41%)
# Likes:    576
# Dislikes: 153
# Total Accepted:    42.6K
# Total Submissions: 89.8K
# Testcase Example:  '[0,1,1]'
#
# You are given a binary array nums (0-indexed).
#
# We define xi as the number whose binary representation is the subarray
# nums[0..i] (from most-significant-bit to least-significant-bit).
#
#
# For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
#
#
# Return an array of booleans answer where answer[i] is true if xi is divisible
# by 5.
#
#
# Example 1:
#
#
# Input: nums = [0,1,1]
# Output: [true,false,false]
# Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and
# 3 in base-10.
# Only the first number is divisible by 5, so answer[0] is true.
#
#
# Example 2:
#
#
# Input: nums = [1,1,1]
# Output: [false,false,false]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
#
#
#

# @lc tags=math;sort

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二进制前缀，是否被5整除。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []

        p = 0
        for n in nums:
            p = (p * 2 + n) % 5
            res.append(p == 0)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [0,1,1]')
    print('Exception :')
    print('[true,false,false]')
    print('Output :')
    print(str(Solution().prefixesDivBy5([0, 1, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,1,1]')
    print('Exception :')
    print('[false,false,false]')
    print('Output :')
    print(str(Solution().prefixesDivBy5([1, 1, 1])))
    print()

    pass
# @lc main=end