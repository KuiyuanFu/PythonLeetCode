# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (57.92%)
# Likes:    4440
# Dislikes: 205
# Total Accepted:    309.3K
# Total Submissions: 533K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given an n x n matrix where each of the rows and columns are sorted in
# ascending order, return the k^th smallest element in the matrix.
#
# Note that it is the k^th smallest element in the sorted order, not the k^th
# distinct element.
#
#
# Example 1:
#
#
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and
# the 8^th smallest number is 13
#
#
# Example 2:
#
#
# Input: matrix = [[-5]], k = 1
# Output: -5
#
#
#
# Constraints:
#
#
# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 300
# -10^9 <= matrix[i][j] <= 10^9
# All the rows and columns of matrix are guaranteed to be sorted in
# non-decreasing order.
# 1 <= k <= n^2
#
#
#

# @lc tags=binary-search;heap

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 在有序的二维数组中，找第k小的值。
# 对于每一个元素，其左上方的都小于其，而右下方的都大于其。左下和右上的不确定。
# 二分法。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        mi, ma, n = matrix[0][0], matrix[-1][-1], len(matrix)
        while mi < ma:
            m = (ma + mi + 1) // 2
            t = 0
            for i in range(n):
                t += bisect_left(matrix[i], m)
            if t < k:
                mi = m
            else:
                ma = m - 1

        return mi

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8')
    print('Exception :')
    print('13')
    print('Output :')
    print(
        str(Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]],
                                   8)))
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [[-5]], k = 1')
    print('Exception :')
    print('-5')
    print('Output :')
    print(str(Solution().kthSmallest([[-5]], 1)))
    print()

    pass
# @lc main=end