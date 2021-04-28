# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (60.46%)
# Likes:    4648
# Dislikes: 331
# Total Accepted:    556.7K
# Total Submissions: 919.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#
#
# Example 2:
#
#
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
#
# Example 3:
#
#
# Input: matrix = [[1]]
# Output: [[1]]
#
#
# Example 4:
#
#
# Input: matrix = [[1,2],[3,4]]
# Output: [[3,1],[4,2]]
#
#
#
# Constraints:
#
#
# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
#
#
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个方阵，向右侧旋转。
# 把旋转看成两次反转。一次上下反转，一次左下右上反转。
# 这样就可以直接进行交换了。
#
# @lc idea=end

# @lc group=array

# @lc rank=10


# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.upToDown(matrix)
        self.leftDownToRightUp(matrix)
        return matrix

    def upToDown(self, matrix):
        for i in range(len(matrix) // 2):
            matrix[i], matrix[-1 - i] = matrix[-1 - i], matrix[i]

    def leftDownToRightUp(self, matrix):
        for i in range(0, len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[1,2,3],[4,5,6],[7,8,9]]')
    print('Output :')
    print(str(Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))
    print('Exception :')
    print('[[7,4,1],[8,5,2],[9,6,3]]')
    print()

    print('Example 2:')
    print('Input : ')
    print('matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]')
    print('Output :')
    print(
        str(Solution().rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7],
                               [15, 14, 12, 16]])))
    print('Exception :')
    print('[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]')
    print()

    print('Example 3:')
    print('Input : ')
    print('matrix = [[1]]')
    print('Output :')
    print(str(Solution().rotate([[1]])))
    print('Exception :')
    print('[[1]]')
    print()

    print('Example 4:')
    print('Input : ')
    print('matrix = [[1,2],[3,4]]')
    print('Output :')
    print(str(Solution().rotate([[1, 2], [3, 4]])))
    print('Exception :')
    print('[[3,1],[4,2]]')
    print()

    pass
# @lc main=end