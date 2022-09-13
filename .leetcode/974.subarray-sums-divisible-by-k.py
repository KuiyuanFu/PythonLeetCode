# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#
# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (53.40%)
# Likes:    3513
# Dislikes: 144
# Total Accepted:    115.8K
# Total Submissions: 216.9K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# Given an integer array nums and an integer k, return the number of non-empty
# subarrays that have a sum divisible by k.
#
# A subarray is a contiguous part of an array.
#
#
# Example 1:
#
#
# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
#
#
# Example 2:
#
#
# Input: nums = [5], k = 9
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# 2 <= k <= 10^4
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，求子数组和可以整除k的个数。
# 记录模的值，以及0的偏移量，防止每次需要将整个数组移动。
#
# @lc idea=end

# @lc group=offset

# @lc rank=10


# @lc code=start
class Solution:

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        offset = 0
        res = 0
        buffer = [0] * k
        for n in nums:
            n = n % k
            buffer[offset] += 1
            offset = (offset + k - n) % k
            res += buffer[offset]
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [4,5,0,-2,-3,1], k = 5')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [5], k = 9')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().subarraysDivByK([5], 9)))
    print()

    pass
# @lc main=end