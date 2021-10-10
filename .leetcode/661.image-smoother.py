# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#
# https://leetcode.com/problems/image-smoother/description/
#
# algorithms
# Easy (52.89%)
# Likes:    335
# Dislikes: 1429
# Total Accepted:    58.7K
# Total Submissions: 110.5K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# An image smoother is a filter of the size 3 x 3 that can be applied to each
# cell of an image by rounding down the average of the cell and the eight
# surrounding cells (i.e., the average of the nine cells in the blue smoother).
# If one or more of the surrounding cells of a cell is not present, we do not
# consider it in the average (i.e., the average of the four cells in the red
# smoother).
#
# Given an m x n integer matrix img representing the grayscale of an image,
# return the image after applying the smoother on each cell of it.
#
#
# Example 1:
#
#
# Input: img = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[0,0,0],[0,0,0],[0,0,0]]
# Explanation:
# For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
#
#
# Example 2:
#
#
# Input: img = [[100,200,100],[200,50,200],[100,200,100]]
# Output: [[137,141,137],[141,138,141],[137,141,137]]
# Explanation:
# For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) =
# floor(137.5) = 137
# For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6)
# = floor(141.666667) = 141
# For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) =
# floor(138.888889) = 138
#
#
#
# Constraints:
#
#
# m == img.length
# n == img[i].length
# 1 <= m, n <= 200
# 0 <= img[i][j] <= 255
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求平均值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        dirs = [[0, 0], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1],
                [-1, 0], [-1, 1]]
        for i in range(rows):
            for j in range(cols):
                s = 0
                n = 0
                for oi, oj in dirs:
                    ni, nj = i + oi, j + oj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        n += 1
                        s += img[ni][nj]
                res[i][j] = s // n
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('img = [[1,1,1],[1,0,1],[1,1,1]]')
    print('Exception :')
    print('[[0,0,0],[0,0,0],[0,0,0]]')
    print('Output :')
    print(str(Solution().imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('img = [[100,200,100],[200,50,200],[100,200,100]]')
    print('Exception :')
    print('[[137,141,137],[141,138,141],[137,141,137]]')
    print('Output :')
    print(
        str(Solution().imageSmoother([[100, 200, 100], [200, 50, 200],
                                      [100, 200, 100]])))
    print()

    pass
# @lc main=end