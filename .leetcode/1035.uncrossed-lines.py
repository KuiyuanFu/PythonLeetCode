# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#
# https://leetcode.com/problems/uncrossed-lines/description/
#
# algorithms
# Medium (58.96%)
# Likes:    1962
# Dislikes: 28
# Total Accepted:    76.7K
# Total Submissions: 130K
# Testcase Example:  '[1,4,2]\n[1,2,4]'
#
# You are given two integer arrays nums1 and nums2. We write the integers of
# nums1 and nums2 (in the order they are given) on two separate horizontal
# lines.
#
# We may draw connecting lines: a straight line connecting two numbers nums1[i]
# and nums2[j] such that:
#
#
# nums1[i] == nums2[j], and
# the line we draw does not intersect any other connecting (non-horizontal)
# line.
#
#
# Note that a connecting line cannot intersect even at the endpoints (i.e.,
# each number can only belong to one connecting line).
#
# Return the maximum number of connecting lines we can draw in this way.
#
#
# Example 1:
#
#
# Input: nums1 = [1,4,2], nums2 = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to
# nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
#
#
# Example 2:
#
#
# Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
# Output: 3
#
#
# Example 3:
#
#
# Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums1.length, nums2.length <= 500
# 1 <= nums1[i], nums2[j] <= 2000
#
#
#

# @lc tags=tree;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两列数字，不同列的相同数字可以连接，但连接线不能交叉，问最多的连接数。
# 直接dp
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        length1 = len(nums1)
        length2 = len(nums2)
        dp = [[0 for _ in range(length2 + 1)] for _ in range(length1 + 1)]

        for i in range(length1):
            ni = nums1[i]
            for j in range(length2):
                nj = nums2[j]
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1],
                                       dp[i][j] + (1 if ni == nj else 0))
        return dp[-1][-1]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,4,2], nums2 = [1,2,4]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().maxUncrossedLines([1, 4, 2], [1, 2, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().maxUncrossedLines([2, 5, 1, 2, 5],
                                         [10, 5, 2, 1, 5, 2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1])))
    print()

    pass
# @lc main=end