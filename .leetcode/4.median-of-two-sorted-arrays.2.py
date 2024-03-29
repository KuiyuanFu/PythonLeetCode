# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (31.35%)
# Likes:    9663
# Dislikes: 1486
# Total Accepted:    904.5K
# Total Submissions: 2.9M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
#
#
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
# Example 3:
#
#
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
#
#
# Example 4:
#
#
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
#
#
# Example 5:
#
#
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#
#
#
# Constraints:
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#
# Follow up: The overall run time complexity should be O(log (m+n)).
#

# @lc tags=array;binary-search;divide-and-conquer

# @lc imports=start
from cgitb import reset
from difflib import restore
from imports import *
# @lc imports=end

# @lc idea=start
#
# 求两个有序的数组的整体的中位数，同时要求时间复杂度是 lg n+m 级别，所以只能用二分搜索。
# 若是求一个有序数组的中位数，直接在左侧移除一定数量的元素，剩下的最小的就是中位数了，但现在有两个数组，那么就需要比较两个数组中的元素大小了来确定如何移除元素。
# 想法是，先计算左侧需要移除掉多少个元素，之后每次移除当前需要移除的个数的一半。每次移除一半是因为，确定了两个数组的比较位置后，此位置上的较小一方的所有左侧元素都可以确定为小于较大一方。但是较大一方左侧元素与较小一方的大小关系是无法确定的。所以如果每次移除的数量大于一半，那么就不能完全移除所有较小一方左侧的元素了。
# 确定此次需要移除的个数后，再通过每个数组的当前左边界确定比较位置，比较大小，移动左边界。
#
# @lc idea=end

# @lc group=binary-search

# @lc rank=10

# @lc code=start


class Solution:

    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        l1, l2 = len(nums1), len(nums2)
        f = (l1 + l2) % 2 == 1
        b1, b2 = -1, -1

        removeCount = (l1 + l2 - 1) // 2

        while removeCount > 0:
            half = (removeCount + 1) // 2

            i1 = b1 + half
            if i1 >= l1:
                i1 = l1 - 1
            i2 = b2 + half
            if i2 >= l2:
                i2 = l2 - 1

            if i2 == -1 or nums1[i1] < nums2[i2]:
                removeCount -= i1 - b1
                b1 = i1
            else:
                removeCount -= i2 - b2
                b2 = i2

            if b1 == l1 - 1:
                b2 += removeCount
                break
            if b2 == l2 - 1:
                b1 += removeCount
                break
        res = []
        b1 += 1
        if b1 < l1:
            res.append(nums1[b1])
        b1 += 1
        if b1 < l1:
            res.append(nums1[b1])
        b2 += 1
        if b2 < l2:
            res.append(nums2[b2])
        b2 += 1
        if b2 < l2:
            res.append(nums2[b2])

        res.sort()

        if f:
            return res[0]
        else:
            return (res[0] + res[1]) / 2


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,3], nums2 = [2]')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([1, 3], [2])))
    print('Exception :')
    print('2.00000')
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [1,2], nums2 = [3,4]')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([1, 2], [3, 4])))
    print('Exception :')
    print('2.50000')
    print()

    print('Example 3:')
    print('Input : ')
    print('nums1 = [0,0], nums2 = [0,0]')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([0, 0], [0, 0])))
    print('Exception :')
    print('0.00000')
    print()

    print('Example 4:')
    print('Input : ')
    print('nums1 = [], nums2 = [1]')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([], [1])))
    print('Exception :')
    print('1.00000')
    print()

    print('Example 4:')
    print('Input : ')
    print('nums1 = [], nums2 = [1, 2, 3, 4]')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([], [1, 2, 3, 4])))
    print('Exception :')
    print('2.50000')
    print()

    print('Example 5:')
    print('Input : ')
    print('nums1 = [2], nums2 = []')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([2], [])))
    print('Exception :')
    print('2.00000')
    print()

    pass
# @lc main=end
