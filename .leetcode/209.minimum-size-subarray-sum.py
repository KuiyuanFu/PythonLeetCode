# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (40.18%)
# Likes:    3923
# Dislikes: 145
# Total Accepted:    368.7K
# Total Submissions: 914.5K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray [numsl, numsl+1, ...,
# numsr-1, numsr] of which the sum is greater than or equal to target. If there
# is no such subarray, return 0 instead.
#
#
# Example 1:
#
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem
# constraint.
#
#
# Example 2:
#
#
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
#
# Example 3:
#
#
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution of which the time complexity is O(n log(n)).
#

# @lc tags=array;two-pointers;binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定整数序列，求连续的最短子序列，满足和大于目标值。
# 直接双指针即可。
# 也可以使用线段树，复杂度会高一点，O nlgn。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums) + 1
        l, r = 0, 0

        now = 0
        while r < len(nums):
            now += nums[r]
            if now >= target:
                while l < r and now - nums[l] >= target:
                    now -= nums[l]
                    l += 1
                n = min(n, r - l + 1)
            r += 1
        if n == len(nums) + 1:
            n = 0
        return n
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().minSubArrayLen(697439, [
            5334, 6299, 4199, 9663, 8945, 3566, 9509, 3124, 6026, 6250, 7475,
            5420, 9201, 9501, 38, 5897, 4411, 6638, 9845, 161, 9563, 8854,
            3731, 5564, 5331, 4294, 3275, 1972, 1521, 2377, 3701, 6462, 6778,
            187, 9778, 758, 550, 7510, 6225, 8691, 3666, 4622, 9722, 8011,
            7247, 575, 5431, 4777, 4032, 8682, 5888, 8047, 3562, 9462, 6501,
            7855, 505, 4675, 6973, 493, 1374, 3227, 1244, 7364, 2298, 3244,
            8627, 5102, 6375, 8653, 1820, 3857, 7195, 7830, 4461, 7821, 5037,
            2918, 4279, 2791, 1500, 9858, 6915, 5156, 970, 1471, 5296, 1688,
            578, 7266, 4182, 1430, 4985, 5730, 7941, 3880, 607, 8776, 1348,
            2974, 1094, 6733, 5177, 4975, 5421, 8190, 8255, 9112, 8651, 2797,
            335, 8677, 3754, 893, 1818, 8479, 5875, 1695, 8295, 7993, 7037,
            8546, 7906, 4102, 7279, 1407, 2462, 4425, 2148, 2925, 3903, 5447,
            5893, 3534, 3663, 8307, 8679, 8474, 1202, 3474, 2961, 1149, 7451,
            4279, 7875, 5692, 6186, 8109, 7763, 7798, 2250, 2969, 7974, 9781,
            7741, 4914, 5446, 1861, 8914, 2544, 5683, 8952, 6745, 4870, 1848,
            7887, 6448, 7873, 128, 3281, 794, 1965, 7036, 8094, 1211, 9450,
            6981, 4244, 2418, 8610, 8681, 2402, 2904, 7712, 3252, 5029, 3004,
            5526, 6965, 8866, 2764, 600, 631, 9075, 2631, 3411, 2737, 2328,
            652, 494, 6556, 9391, 4517, 8934, 8892, 4561, 9331, 1386, 4636,
            9627, 5435, 9272, 110, 413, 9706, 5470, 5008, 1706, 7045, 9648,
            7505, 6968, 7509, 3120, 7869, 6776, 6434, 7994, 5441, 288, 492,
            1617, 3274, 7019, 5575, 6664, 6056, 7069, 1996, 9581, 3103, 9266,
            2554, 7471, 4251, 4320, 4749, 649, 2617, 3018, 4332, 415, 2243,
            1924, 69, 5902, 3602, 2925, 6542, 345, 4657, 9034, 8977, 6799,
            8397, 1187, 3678, 4921, 6518, 851, 6941, 6920, 259, 4503, 2637,
            7438, 3893, 5042, 8552, 6661, 5043, 9555, 9095, 4123, 142, 1446,
            8047, 6234, 1199, 8848, 5656, 1910, 3430, 2843, 8043, 9156, 7838,
            2332, 9634, 2410, 2958, 3431, 4270, 1420, 4227, 7712, 6648, 1607,
            1575, 3741, 1493, 7770, 3018, 5398, 6215, 8601, 6244, 7551, 2587,
            2254, 3607, 1147, 5184, 9173, 8680, 8610, 1597, 1763, 7914, 3441,
            7006, 1318, 7044, 7267, 8206, 9684, 4814, 9748, 4497, 2239
        ])))

    print('Example 1:')
    print('Input : ')
    print('target = 7, nums = [2,3,1,2,4,3]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('target = 4, nums = [1,4,4]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minSubArrayLen(4, [1, 4, 4])))
    print()

    print('Example 3:')
    print('Input : ')
    print('target = 11, nums = [1,1,1,1,1,1,1,1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1])))
    print()

    pass
# @lc main=end