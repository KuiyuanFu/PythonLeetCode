# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (66.45%)
# Likes:    1681
# Dislikes: 1646
# Total Accepted:    517.7K
# Total Submissions: 778.3K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may return
# the result in any order.
#
#
# Example 1:
#
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#
#
# Example 2:
#
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
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
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
                while idx1 < length1 and nums1[idx1] == nums1[idx1 - 1]:
                    idx1 += 1
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
    print('[2]')
    print('Output :')
    print(str(Solution().intersection([1, 2, 2, 1], [2, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [4,9,5], nums2 = [9,4,9,8,4]')
    print('Exception :')
    print('[9,4]')
    print('Output :')
    print(str(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4])))
    print()

    pass
# @lc main=end