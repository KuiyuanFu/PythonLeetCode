# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (45.69%)
# Likes:    2519
# Dislikes: 623
# Total Accepted:    137.9K
# Total Submissions: 301.6K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# There is an m x n rectangular island that borders both the Pacific Ocean and
# Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
# and the Atlantic Ocean touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells. You are given an m x n
# integer matrix heights where heights[r][c] represents the height above sea
# level of the cell at coordinate (r, c).
#
# The island receives a lot of rain, and the rain water can flow to neighboring
# cells directly north, south, east, and west if the neighboring cell's height
# is less than or equal to the current cell's height. Water can flow from any
# cell adjacent to an ocean into the ocean.
#
# Return a 2D list of grid coordinates result where result[i] = [ri, ci]
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and
# Atlantic oceans.
#
#
# Example 1:
#
#
# Input: heights =
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#
#
# Example 2:
#
#
# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]
#
#
#
# Constraints:
#
#
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 10^5
#
#
#

# @lc tags=depth-first-search;breadth-first-search

# @lc imports=start
from os import close
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二维棋盘，表示高度，雨水可以四个方向流向不高于其的位置，问哪些位置可以流向左上及右下。
# 直接从低到高遍历，相连的相同高度的值是相同的。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        f = defaultdict(int)
        re, ce = rows - 1, cols - 1
        for i in range(rows):
            f[i * cols + ce] |= 2
            f[i * cols] |= 1
        for j in range(cols):
            f[j] |= 1
            f[re * cols + j] |= 2

        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        s = [(heights[i][j], i, j) for i in range(rows) for j in range(cols)]
        heapify(s)
        res = []
        visited = set()
        while s:
            h, i, j = heappop(s)
            if (i, j) in visited:
                continue
            st = [[i, j]]
            nn = []
            nf = f[i * cols + j]
            visited.add((i, j))
            for i, j in st:
                nf |= f[i * cols + j]
                for si, sj in d:
                    ni, nj = i + si, j + sj
                    if 0 <= ni < rows and 0 <= nj < cols and \
                        (ni, nj) not in visited:
                        hh = heights[ni][nj]
                        if hh == h:
                            st.append([ni, nj])
                            visited.add((ni, nj))
                        if hh > h:
                            nn.append(ni * cols + nj)

            for k in nn:
                f[k] |= nf
            if nf == 3:
                res += st

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'heights =[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
    )
    print('Exception :')
    print('[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]')
    print('Output :')
    print(
        str(Solution().pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4],
                                        [2, 4, 5, 3, 1], [6, 7, 1, 4, 5],
                                        [5, 1, 1, 2, 4]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('heights = [[2,1],[1,2]]')
    print('Exception :')
    print('[[0,0],[0,1],[1,0],[1,1]]')
    print('Output :')
    print(str(Solution().pacificAtlantic([[2, 1], [1, 2]])))
    print()
    print(str(Solution().pacificAtlantic([[1, 1], [1, 1]])))
    pass
# @lc main=end