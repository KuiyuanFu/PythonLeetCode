# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (44.64%)
# Likes:    3346
# Dislikes: 368
# Total Accepted:    419.6K
# Total Submissions: 939.8K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given an m x n matrix. If an element is 0, set its entire row and column to
# 0. Do it in-place.
#
# Follow up:
#
#
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
#
# Example 2:
#
#
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个二维矩阵，如果其中一个元素为0，那么就将所在行与列赋值为0。要求使用常数额外空间。
# 由于常数额外空间，所以为每行每列设置一个标志位的想法破灭了。
# 这道题的难点是如果区分元素本来就是0，还是因为其所在的行列中有0时，被修改为0的。
# 首先借用第一行与第一列，其中第一行中的元素为0，说明此列全可以设置为0。列同理。但由于0 ，0 位置上的元素用来表示列的标志为了，用额外的一个标志位表示第一行是否为0。
#
# @lc idea=end

# @lc group=in-place

# @lc rank=10


# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        flag = matrix[0][0] == 0

        # 设置标志位
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                flag = True
            for i in range(1, len(matrix)):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # 先处理行，因为第一列保存行的信息，如果先处理列，可能会将这一列全置为0.
        for i in reversed(range(1, len(matrix))):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[0])):
                    matrix[i][j] = 0
        # 再处理列
        for j in reversed(range(len(matrix[0]))):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0
        # 最后处理第一行
        if flag:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        return matrix


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[1,1,1],[1,0,1],[1,1,1]]')
    print('Output :')
    print(str(Solution().setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])))
    print('Exception :')
    print('[[1,0,1],[0,0,0],[1,0,1]]')
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]')
    print('Output :')
    print(str(Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1,
                                                                 5]])))
    print('Exception :')
    print('[[0,0,0,0],[0,4,5,0],[0,3,1,0]]')
    print()

    pass
# @lc main=end