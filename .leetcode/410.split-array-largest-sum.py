# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (47.56%)
# Likes:    3141
# Dislikes: 101
# Total Accepted:    135.2K
# Total Submissions: 282.7K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an array nums which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
#
# Write an algorithm to minimize the largest sum among these m subarrays.
#
#
# Example 1:
#
#
# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4,5], m = 2
# Output: 9
#
#
# Example 3:
#
#
# Input: nums = [1,4,4], m = 3
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 10^6
# 1 <= m <= min(50, nums.length)
#
#
#

# @lc tags=binary-search;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一个数组分成连续的k段，求每段和最大值的最小值。
# 朴素的想法是用分治备忘录，每次选一个位置，分成两端，分别赋予再分段的数量，取和的最大值，之后再选最小值。
# 比较好的思想是，二分搜索，选定一个最大值的值，之后再判断是否合法。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def valid(sm):
            s = 0
            c = 1
            for n in nums:
                s += n
                if s > sm:
                    s = n
                    c += 1
            return c <= k

        l, r = max(nums), sum(nums)
        while l < r:
            sm = (l + r) // 2
            if valid(sm):
                r = sm
            else:
                l = sm + 1
        return r
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [7,2,5,10,8], m = 2')
    print('Exception :')
    print('18')
    print('Output :')
    print(str(Solution().splitArray([7, 2, 5, 10, 8], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4,5], m = 2')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().splitArray([1, 2, 3, 4, 5], 2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,4,4], m = 3')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().splitArray([1, 4, 4], 3)))
    print()

    pass
# @lc main=end