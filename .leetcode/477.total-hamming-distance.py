# @lc app=leetcode id=477 lang=python3
#
# [477] Total Hamming Distance
#
# https://leetcode.com/problems/total-hamming-distance/description/
#
# algorithms
# Medium (51.20%)
# Likes:    1295
# Dislikes: 70
# Total Accepted:    77.6K
# Total Submissions: 151.3K
# Testcase Example:  '[4,14,2]'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
#
# Given an integer array nums, return the sum of Hamming distances between all
# the pairs of the integers in nums.
#
#
# Example 1:
#
#
# Input: nums = [4,14,2]
# Output: 6
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is
# 0010 (just
# showing the four bits relevant in this case).
# The answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 +
# 2 + 2 = 6.
#
#
# Example 2:
#
#
# Input: nums = [4,14,4]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^9
# The answer for the given input will fit in a 32-bit integer.
#
#
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求给定数组中所有对的hamming距离之和。
# 统计每一位0,1个数，之后累计。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        masks = [(i, 1 << i) for i in range(30)]
        counts = [[0, 0] for _ in range(30)]
        for n in nums:
            for i, m in masks:
                t = 1 if n & m != 0 else 0
                counts[i][t] += 1
        return sum(z * o for z, o in counts)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [4,14,2]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().totalHammingDistance([4, 14, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [4,14,4]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().totalHammingDistance([4, 14, 4])))
    print()

    pass
# @lc main=end