# @lc app=leetcode id=675 lang=python3
#
# [675] Cut Off Trees for Golf Event
#
# https://leetcode.com/problems/cut-off-trees-for-golf-event/description/
#
# algorithms
# Hard (35.51%)
# Likes:    779
# Dislikes: 459
# Total Accepted:    48.8K
# Total Submissions: 137.7K
# Testcase Example:  '[[1,2,3],[0,0,4],[7,6,5]]'
#
# You are asked to cut off all the trees in a forest for a golf event. The
# forest is represented as an m x n matrix. In this matrix:
#
#
# 0 means the cell cannot be walked through.
# 1 represents an empty cell that can be walked through.
# A number greater than 1 represents a tree in a cell that can be walked
# through, and this number is the tree's height.
#
#
# In one step, you can walk in any of the four directions: north, east, south,
# and west. If you are standing in a cell with a tree, you can choose whether
# to cut it off.
#
# You must cut off the trees in order from shortest to tallest. When you cut
# off a tree, the value at its cell becomes 1 (an empty cell).
#
# Starting from the point (0, 0), return the minimum steps you need to walk to
# cut off all the trees. If you cannot cut off all the trees, return -1.
#
# You are guaranteed that no two trees have the same height, and there is at
# least one tree needs to be cut off.
#
#
# Example 1:
#
#
# Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
# Output: 6
# Explanation: Following the path above allows you to cut off the trees from
# shortest to tallest in 6 steps.
#
#
# Example 2:
#
#
# Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
# Output: -1
# Explanation: The trees in the bottom row cannot be accessed as the middle row
# is blocked.
#
#
# Example 3:
#
#
# Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
# Output: 6
# Explanation: You can follow the same path as Example 1 to cut off all the
# trees.
# Note that you can cut off the first tree at (0, 0) before making any
# steps.
#
#
#
# Constraints:
#
#
# m == forest.length
# n == forest[i].length
# 1 <= m, n <= 50
# 0 <= forest[i][j] <= 10^9
#
#
#

# @lc tags=breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 按照数值大小遍历。
# 广度优先寻找通路距离。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        rows, cols = len(forest), len(forest[0])

        visited = [[0 for j in range(cols)] for i in range(rows)]
        directs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def distance(i, j, ti, tj, v):

            if i == ti and j == tj:
                return 0
            d = 0
            p = [(i, j)]
            visited[i][j] = v
            while p:
                d += 1
                pn = []
                for i, j in p:
                    for oi, oj in directs:
                        ni, nj = i + oi, j + oj
                        if 0 <= ni < rows and 0 <= nj < cols:
                            if ni == ti and nj == tj:
                                return d
                            if visited[ni][nj] < v and forest[ni][nj] >= 1:
                                visited[ni][nj] = v
                                pn.append((ni, nj))
                p = pn
            return None

        h = [(forest[i][j], i, j) for j in range(cols) for i in range(rows)]
        heapify(h)
        res = 0
        while h and h[0][0] <= 1:
            heappop(h)

        i, j = 0, 0
        while h:
            v, ni, nj = heappop(h)
            d = distance(i, j, ni, nj, v)
            if d is None:
                return -1
            res += d
            forest[ni][nj] = 1
            i, j = ni, nj

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('forest = [[1,2,3],[0,0,4],[7,6,5]]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().cutOffTree([[1, 2, 3], [0, 0, 4], [7, 6, 5]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('forest = [[1,2,3],[0,0,0],[7,6,5]]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().cutOffTree([[1, 2, 3], [0, 0, 0], [7, 6, 5]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('forest = [[2,3,4],[0,0,5],[8,7,6]]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().cutOffTree([[2, 3, 4], [0, 0, 5], [8, 7, 6]])))
    print()

    pass
# @lc main=end