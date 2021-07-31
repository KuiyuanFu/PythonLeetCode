# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (52.64%)
# Likes:    2549
# Dislikes: 542
# Total Accepted:    543.7K
# Total Submissions: 1M
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must appear as many times as it
# shows in both arrays and you may return the result in any order.
#
#
# Example 1:
#
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
#
#
# Example 2:
#
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
#
#
#
# Constraints:
#
#
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
#
#
#
# Follow up:
#
#
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
#
#
#

# @lc tags=hash-table;two-pointers;binary-search;sort

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个数组，求交集。
# 排序，之后指针。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        idx1, idx2 = 0, 0
        length1, length2 = len(nums1), len(nums2)
        while idx1 < length1 and idx2 < length2:
            if nums1[idx1] == nums2[idx2]:
                result.append(nums1[idx1])
                idx1 += 1
                idx2 += 1

            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        return result


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,2,2,1], nums2 = [2,2]')
    print('Exception :')
    print('[2,2]')
    print('Output :')
    print(str(Solution().intersect([1, 2, 2, 1], [2, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [4,9,5], nums2 = [9,4,9,8,4]')
    print('Exception :')
    print('[4,9]')
    print('Output :')
    print(str(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4])))
    print()

    pass
# @lc main=end