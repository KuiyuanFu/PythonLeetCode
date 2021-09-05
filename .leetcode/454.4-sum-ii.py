# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
# https://leetcode.com/problems/4sum-ii/description/
#
# algorithms
# Medium (55.31%)
# Likes:    2355
# Dislikes: 87
# Total Accepted:    183.3K
# Total Submissions: 331.4K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
# return the number of tuples (i, j, k, l) such that:
#
#
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
#
#
#
# Example 1:
#
#
# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) +
# (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) +
# (-1) + 0 = 0
#
#
# Example 2:
#
#
# Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# Output: 1
#
#
#
# Constraints:
#
#
# n == nums1.length
# n == nums2.length
# n == nums3.length
# n == nums4.length
# 1 <= n <= 200
# -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
#
#
#

# @lc tags=hash-table;binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求四个数组中，各区一个元素和为0的个数。
# 统计前两个数组组合的值的个数，之后在后两个中组合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int],
                     nums3: List[int], nums4: List[int]) -> int:

        d1 = Counter(n1 + n2 for n1 in nums1 for n2 in nums2)
        return sum(d1[-(n1 + n2)] for n1 in nums3 for n2 in nums4)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().fourSumCount([0], [0], [0], [0])))
    print()

    pass
# @lc main=end