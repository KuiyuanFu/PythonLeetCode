# @lc app=leetcode id=995 lang=python3
#
# [995] Minimum Number of K Consecutive Bit Flips
#
# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/description/
#
# algorithms
# Hard (51.10%)
# Likes:    937
# Dislikes: 52
# Total Accepted:    28.2K
# Total Submissions: 55.2K
# Testcase Example:  '[0,1,0]\n1'
#
# You are given a binary array nums and an integer k.
#
# A k-bit flip is choosing a subarray of length k from nums and simultaneously
# changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
#
# Return the minimum number of k-bit flips required so that there is no 0 in
# the array. If it is not possible, return -1.
#
# A subarray is a contiguous part of an array.
#
#
# Example 1:
#
#
# Input: nums = [0,1,0], k = 1
# Output: 2
# Explanation: Flip nums[0], then flip nums[2].
#
#
# Example 2:
#
#
# Input: nums = [1,1,0], k = 2
# Output: -1
# Explanation: No matter how we flip subarrays of size 2, we cannot make the
# array become [1,1,1].
#
#
# Example 3:
#
#
# Input: nums = [0,0,0,1,0,1,1,0], k = 3
# Output: 3
# Explanation:
# Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
# Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
# Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= k <= nums.length
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，元素为0或1，与一个k，每次选择k长的连续子数组，反转。使最后只有1，没有0。如果可以返回最少次数，否则返回-1。
# 直接遍历一次，记录当前反转次数，使0变成1，如果不可能就失败了。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0
        idx = 0
        length = 0
        lengtgNums = len(nums)
        q = []
        for i, n in enumerate(nums):
            while idx < length and q[idx] <= i:
                idx += 1
            l = length - idx
            if (n + l) % 2 == 1:
                continue
            q.append(i + k)
            length += 1
            res += 1
        while idx < length and q[idx] <= lengtgNums:
            idx += 1
        if idx == length:
            return res
        else:
            return -1

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [0,1,0], k = 1')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minKBitFlips([0, 1, 0], 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,1,0], k = 2')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().minKBitFlips([1, 1, 0], 2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [0,0,0,1,0,1,1,0], k = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3)))
    print()

    pass
# @lc main=end