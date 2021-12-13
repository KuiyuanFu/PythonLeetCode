# @lc app=leetcode id=801 lang=python3
#
# [801] Minimum Swaps To Make Sequences Increasing
#
# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/description/
#
# algorithms
# Hard (38.98%)
# Likes:    1829
# Dislikes: 122
# Total Accepted:    49.5K
# Total Submissions: 126.4K
# Testcase Example:  '[1,3,5,4]\n[1,2,3,7]'
#
# You are given two integer arrays of the same length nums1 and nums2. In one
# operation, you are allowed to swap nums1[i] with nums2[i].
#
#
# For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the
# element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
#
#
# Return the minimum number of needed operations to make nums1 and nums2
# strictly increasing. The test cases are generated so that the given input
# always makes it possible.
#
# An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] <
# ... < arr[arr.length - 1].
#
#
# Example 1:
#
#
# Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
# Output: 1
# Explanation:
# Swap nums1[3] and nums2[3]. Then the sequences are:
# nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
# which are both strictly increasing.
#
#
# Example 2:
#
#
# Input: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
# Output: 1
#
#
#
# Constraints:
#
#
# 2 <= nums1.length <= 10^5
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 2 * 10^5
#
#
#

# @lc tags=depth-first-search;breadth-first-search;graph

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个数组，可以交换相同索引的元素。求最小的交换次数，使两数组成为严格单调递增数组。
# dp。就两个状态，一个交换，一个不交换。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        # not swap element, swap element
        nse, se = 0, 1
        l = len(nums1)
        for i in range(1, l):
            fns = nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]
            fs = nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]
            nse, se = min(nse if fns else l, se if fs else l)\
                , min( se if fns else l,nse if fs else l)+1
        return min(se, nse)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,3,5,4], nums2 = [1,2,3,7]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minSwap([1, 3, 5, 4], [1, 2, 3, 7])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minSwap([0, 3, 5, 8, 9], [2, 1, 4, 6, 9])))
    print()

    pass
# @lc main=end