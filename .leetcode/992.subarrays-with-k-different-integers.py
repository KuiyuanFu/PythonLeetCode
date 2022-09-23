# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#
# https://leetcode.com/problems/subarrays-with-k-different-integers/description/
#
# algorithms
# Hard (54.11%)
# Likes:    3569
# Dislikes: 53
# Total Accepted:    79.4K
# Total Submissions: 146.7K
# Testcase Example:  '[1,2,1,2,3]\n2'
#
# Given an integer array nums and an integer k, return the number of good
# subarrays of nums.
#
# A good array is an array where the number of different integers in that array
# is exactly k.
#
#
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
#
#
# A subarray is a contiguous part of an array.
#
#
# Example 1:
#
#
# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2],
# [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
#
#
# Example 2:
#
#
# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3],
# [2,1,3], [1,3,4].
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i], k <= nums.length
#
#
#

# @lc tags=greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，和一个整数k，求子数组个数，子数组满足不同元素为k个。
# 窗口，统计个数
#
# @lc idea=end

# @lc group=

# @lc rank=3


# @lc code=start
class Solution:

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        res = 0
        counter = {}
        length = 1
        diff = 0
        l = 0
        for n in nums:

            if n not in counter:
                diff += 1
                counter[n] = 0
                # remove a kind of elements
                if diff == k + 1:
                    while counter[nums[l]] != 1:
                        counter[nums[l]] -= 1
                        l += 1
                    counter.pop(nums[l])
                    diff -= 1
                    length = 1
                    l += 1

            # increase length
            counter[n] += 1
            if diff == k:
                while counter[nums[l]] > 1:
                    counter[nums[l]] -= 1
                    length += 1
                    l += 1
            if diff == k:
                res += length
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,1,2,3], k = 2')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,1,3,4], k = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().subarraysWithKDistinct([1, 2, 1, 3, 4], 3)))
    print()

    pass
# @lc main=end