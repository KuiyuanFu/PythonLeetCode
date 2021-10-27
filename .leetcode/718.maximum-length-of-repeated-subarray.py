# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (51.07%)
# Likes:    3115
# Dislikes: 72
# Total Accepted:    142.9K
# Total Submissions: 279K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays nums1 and nums2, return the maximum length of a
# subarray that appears in both arrays.
#
#
# Example 1:
#
#
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
#
#
# Example 2:
#
#
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
#
#
#
# Constraints:
#
#
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100
#
#
#

# @lc tags=array;hash-table;binary-search;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最长相同子字符串。
# dp.
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        l1, l2 = len(nums1), len(nums2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(l1):
            for j in range(l2):
                t = 0
                if nums1[i] == nums2[j]:
                    t = dp[i][j] + 1
                else:
                    t = 0
                res = max(res, t)
                dp[i + 1][j + 1] = t
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findLength([0, 0, 0, 0, 0], [0, 0, 0, 0, 0])))
    print()

    pass
# @lc main=end