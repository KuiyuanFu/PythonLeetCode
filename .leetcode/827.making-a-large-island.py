# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最多将一个海域改成陆地，求最大岛屿。
# 统计岛屿，之后转换。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        islands = {}
        n = len(grid)
        islandIdx = 2
        for i, j in product(range(n), range(n)):
            v = grid[i][j]
            if v == 1:
                grid[i][j] = islandIdx
                islandArea = 1
                ls = [(i, j)]
                while ls:
                    i, j = ls.pop()
                    for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j),
                                   (i, j - 1)]:
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            islandArea += 1
                            grid[ni][nj] = islandIdx
                            ls.append((ni, nj))
                islands[islandIdx] = islandArea
                islandIdx += 1
        maxArea = max(islands.values()) if len(islands) > 0 else 1
        for i, j in product(range(n), range(n)):
            v = grid[i][j]
            if v == 0:
                s = set()
                for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] >= 2:
                        s.add(grid[ni][nj])
                a = 1 + sum(islands[islandIdx]
                            for islandIdx in s) if len(s) > 0 else 0
                maxArea = max(maxArea, a)
        return maxArea
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [[1,0],[0,1]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().largestIsland([[1, 0], [0, 1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [[1,1],[1,0]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().largestIsland([[1, 1], [1, 0]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('grid = [[1,1],[1,1]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().largestIsland([[1, 1], [1, 1]])))
    print()

    pass
# @lc main=end