# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#
# https://leetcode.com/problems/count-of-range-sum/description/
#
# algorithms
# Hard (36.23%)
# Likes:    1192
# Dislikes: 130
# Total Accepted:    52.7K
# Total Submissions: 145.3K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# Given an integer array nums and two integers lower and upper, return the
# number of range sums that lie in [lower, upper] inclusive.
#
# Range sum S(i, j) is defined as the sum of the elements in nums between
# indices i and j inclusive, where i <= j.
#
#
# Example 1:
#
#
# Input: nums = [-2,5,-1], lower = -2, upper = 2
# Output: 3
# Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their
# respective sums are: -2, -1, 2.
#
#
# Example 2:
#
#
# Input: nums = [0], lower = 0, upper = 0
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# -10^5 <= lower <= upper <= 10^5
# The answer is guaranteed to fit in a 32-bit integer.
#
#
#

# @lc tags=binary-search;divide-and-conquer;sort;binary-indexed-tree;segment-tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求区间和在一定范围的个数。
# 线段树，二分搜索。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        from bisect import bisect

        def recursion(l: int, r: int):
            if l == r:
                return [nums[l]], [nums[l]], nums[l],\
                     (1 if lower <= nums[l] <= upper else 0)
            m = (l + r) // 2
            lladj, lradj, lsum, lcount = recursion(l, m)
            rladj, rradj, rsum, rcount = recursion(m + 1, r)
            ladj = lladj + [lsum + rla for rla in rladj]
            ladj.sort()
            radj = rradj + [rsum + lra for lra in lradj]
            radj.sort()

            csum = lsum + rsum
            count = lcount + rcount

            for key in lradj:
                l = bisect(rladj, lower - key - 1)
                r = bisect(rladj, upper - key)
                count += r - l
            return ladj, radj, csum, count

        return recursion(0, len(nums) - 1)[-1]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().countRangeSum([0, 0], 0, 0)))
    print(str(Solution().countRangeSum([-3, 1, 2, -2, 2, -1], -3, -1)))
    print(str(Solution().countRangeSum([0, -1, -2, -3, 0, 2], 3, 5)))
    print('Example 1:')
    print('Input : ')
    print('nums = [-2,5,-1], lower = -2, upper = 2')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().countRangeSum([-2, 5, -1], -2, 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0], lower = 0, upper = 0')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().countRangeSum([0], 0, 0)))
    print()

    pass
# @lc main=end