# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (40.91%)
# Likes:    3688
# Dislikes: 5262
# Total Accepted:    857.9K
# Total Submissions: 2.1M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
#
# The number of elements initialized in nums1 and nums2 are m and n
# respectively. You may assume that nums1 has a size equal to m + n such that
# it has enough space to hold additional elements from nums2.
#
#
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
#
#
# Constraints:
#
#
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -10^9 <= nums1[i], nums2[i] <= 10^9
#
#
#

# @lc tags=array;two-pointers

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个有序数组，将第二个合并到第一个中。
# 由于是数组，所以需要从后向前遍历，防止覆盖元素。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            pass
        elif m == 0:
            for i, n in enumerate(nums2):
                nums1[i] = n
        else:
            p = n + m - 1
            f = m - 1
            s = n - 1

            while True:
                if nums1[f] > nums2[s]:
                    nums1[p] = nums1[f]
                    f -= 1
                    if f == -1:
                        for i in range(s + 1):
                            nums1[i] = nums2[i]
                        break
                else:
                    nums1[p] = nums2[s]
                    s -= 1
                    if s == -1:
                        break
                p -= 1

        return nums1
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3')
    print('Output :')
    print(str(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)))
    print('Exception :')
    print('[1,2,2,3,5,6]')
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [1], m = 1, nums2 = [], n = 0')
    print('Output :')
    print(str(Solution().merge([1], 1, [], 0)))
    print('Exception :')
    print('[1]')
    print()

    pass
# @lc main=end