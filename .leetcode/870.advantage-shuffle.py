# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#
# https://leetcode.com/problems/advantage-shuffle/description/
#
# algorithms
# Medium (51.19%)
# Likes:    1211
# Dislikes: 77
# Total Accepted:    52.2K
# Total Submissions: 102K
# Testcase Example:  '[2,7,11,15]\n[1,10,4,11]'
#
# You are given two integer arrays nums1 and nums2 both of the same length. The
# advantage of nums1 with respect to nums2 is the number of indices i for which
# nums1[i] > nums2[i].
#
# Return any permutation of nums1 that maximizes its advantage with respect to
# nums2.
#
#
# Example 1:
# Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
# Output: [2,11,7,15]
# Example 2:
# Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
# Output: [24,32,8,12]
#
#
# Constraints:
#
#
# 1 <= nums1.length <= 10^5
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 10^9
#
#
#

# @lc tags=array

# @lc imports=start
import re
from imports import *

# @lc imports=end

# @lc idea=start
#
# 两个数组，优势为对应位置大于另一个的个数，重新排列，使优势最大。
# 排序，从大到小，使每一个值，对应最大的比起小的值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        length = len(nums1)
        res = [None] * length
        nums1Sorted = sorted(nums1, reverse=True)
        nums2SortedWithIndex = sorted([(n, i) for i, n in enumerate(nums2)],
                                      reverse=True)

        l, r = 0, length - 1
        for n, i in nums2SortedWithIndex:
            if nums1Sorted[l] > n:
                res[i] = nums1Sorted[l]
                l += 1
            else:
                res[i] = nums1Sorted[r]
                r -= 1

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [2,7,11,15], nums2 = [1,10,4,11]')
    print('Exception :')
    print('[2,11,7,15]')
    print('Output :')
    print(str(Solution().advantageCount([2, 7, 11, 15], [1, 10, 4, 11])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [12,24,8,32], nums2 = [13,25,32,11]')
    print('Exception :')
    print('[24,32,8,12]')
    print('Output :')
    print(str(Solution().advantageCount([12, 24, 8, 32], [13, 25, 32, 11])))
    print()

    pass
# @lc main=end