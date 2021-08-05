# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (39.76%)
# Likes:    1643
# Dislikes: 100
# Total Accepted:    71.5K
# Total Submissions: 179.9K
# Testcase Example:  '[[1,0,1],[0,-2,3]]\n2'
#
# Given an m x n matrix matrix and an integer k, return the max sum of a
# rectangle in the matrix such that its sum is no larger than k.
#
# It is guaranteed that there will be a rectangle with a sum no larger than
# k.
#
#
# Example 1:
#
#
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2,
# and 2 is the max number no larger than k (k = 2).
#
#
# Example 2:
#
#
# Input: matrix = [[2,2,-1]], k = 3
# Output: 3
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -100 <= matrix[i][j] <= 100
# -10^5 <= k <= 10^5
#
#
#
# Follow up: What if the number of rows is much larger than the number of
# columns?
#
#

# @lc tags=binary-search;dynamic-programming;queue

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求二维矩阵中矩形区域的和，不大于k的最大值。
# 直接暴力遍历。
# 超时了。
# 将行组合，得到所有的行区间，之后将这个区间上的行元素，压缩到一行上，之后在一行上执行最值。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def maxSumSubmatrix(self, M, k):
        from bisect import bisect_left, insort

        def countRangeSum(nums, U):
            SList, ans = [0], -float("inf")
            for s in accumulate(nums):
                idx = bisect_left(SList, s - U)
                if idx < len(SList): ans = max(ans, s - SList[idx])
                insort(SList, s)
            return ans

        m, n, ans = len(M), len(M[0]), -float("inf")

        # 列累加
        for i, j in product(range(1, m), range(n)):
            M[i][j] += M[i - 1][j]

        # 增加一行边界
        M = [[0] * n] + M

        for r1, r2 in combinations(range(m + 1), 2):
            row = [j - i for i, j in zip(M[r1], M[r2])]
            ans = max(ans, countRangeSum(row, k))

        return ans


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[1,0,1],[0,-2,3]], k = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [[2,2,-1]], k = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().maxSumSubmatrix([[2, 2, -1]], 3)))
    print()

    pass
# @lc main=end