# @lc app=leetcode id=749 lang=python3
#
# [749] Contain Virus
#
# https://leetcode.com/problems/contain-virus/description/
#
# algorithms
# Hard (49.14%)
# Likes:    190
# Dislikes: 349
# Total Accepted:    7.5K
# Total Submissions: 15.2K
# Testcase Example:  '[[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]'
#
# A virus is spreading rapidly, and your task is to quarantine the infected
# area by installing walls.
#
# The world is modeled as an m x n binary grid isInfected, where
# isInfected[i][j] == 0 represents uninfected cells, and isInfected[i][j] == 1
# represents cells contaminated with the virus. A wall (and only one wall) can
# be installed between any two 4-directionally adjacent cells, on the shared
# boundary.
#
# Every night, the virus spreads to all neighboring cells in all four
# directions unless blocked by a wall. Resources are limited. Each day, you can
# install walls around only one region (i.e., the affected area (continuous
# block of infected cells) that threatens the most uninfected cells the
# following night). There will never be a tie.
#
# Return the number of walls used to quarantine all the infected regions. If
# the world will become fully infected, return the number of walls used.
#
#
# Example 1:
#
#
# Input: isInfected =
# [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
# Output: 10
# Explanation: There are 2 contaminated regions.
# On the first day, add 5 walls to quarantine the viral region on the left. The
# board after the virus spreads is:
#
# On the second day, add 5 walls to quarantine the viral region on the right.
# The virus is fully contained.
#
#
#
# Example 2:
#
#
# Input: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
# Output: 4
# Explanation: Even though there is only one cell saved, there are 4 walls
# built.
# Notice that walls are only built on the shared boundary of two different
# cells.
#
#
# Example 3:
#
#
# Input: isInfected =
# [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
# Output: 13
# Explanation: The region on the left only builds two new walls.
#
#
#
# Constraints:
#
#
# m == isInfected.length
# n == isInfected[i].length
# 1 <= m, n <= 50
# isInfected[i][j] is either 0 or 1.
# There is always a contiguous viral region throughout the described process
# that will infect strictly more uncontaminated squares in the next round.
#
#
#

# @lc tags=hash-table

# @lc imports=start
from typing_extensions import get_args
from imports import *

# @lc imports=end

# @lc idea=start
#
# 用墙阻止感染。每次围上传播最多的区块。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Area:
    def __init__(self,
                 wallCount=0,
                 contaminatedArea=None,
                 uninfectedArea=None) -> None:
        self.wallCount = wallCount
        self.contaminatedArea = contaminatedArea if contaminatedArea is not None else []
        self.uninfectedArea = uninfectedArea if uninfectedArea is not None else set(
        )
        pass


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:

        rows, cols = len(isInfected), len(isInfected[0])

        dires = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def generateAllArea() -> List[Area]:

            visited = set()
            areas = []
            for i, j in product(range(rows), range(cols)):
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                state = isInfected[i][j]
                # new contaminated area
                if state == 1:

                    wallCount = 0
                    contaminatedArea = [(i, j)]
                    uninfectedArea = set()

                    idx = 0
                    while idx < len(contaminatedArea):
                        i, j = contaminatedArea[idx]
                        for oi, oj in dires:
                            ni, nj = i + oi, j + oj
                            if 0 <= ni < rows and 0 <= nj < cols:
                                ns = isInfected[ni][nj]
                                if ns == 0:
                                    uninfectedArea.add((ni, nj))
                                    wallCount += 1
                                if ns == 1 and (ni, nj) not in visited:
                                    visited.add((ni, nj))
                                    contaminatedArea.append((ni, nj))
                        idx += 1
                    area = Area(wallCount=wallCount,
                                contaminatedArea=contaminatedArea,
                                uninfectedArea=uninfectedArea)
                    areas.append(area)
            return areas

        def countWall():
            res = 0
            areas = generateAllArea()
            while len(areas) > 0:
                area = max(areas, key=lambda area: len(area.uninfectedArea))
                res += area.wallCount

                for i, j in area.contaminatedArea:
                    isInfected[i][j] = -1

                areas.remove(area)

                for area in areas:
                    for i, j in area.uninfectedArea:
                        isInfected[i][j] = 1

                areas = generateAllArea()
            return res

        return countWall()


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'isInfected =[[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]'
    )
    print('Exception :')
    print('10')
    print('Output :')
    print(
        str(Solution().containVirus([[0, 1, 0, 0, 0, 0, 0, 1],
                                     [0, 1, 0, 0, 0, 0, 0, 1],
                                     [0, 0, 0, 0, 0, 0, 0, 1],
                                     [0, 0, 0, 0, 0, 0, 0, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('isInfected = [[1,1,1],[1,0,1],[1,1,1]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().containVirus([[1, 1, 1], [1, 0, 1], [1, 1, 1]])))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'isInfected =[[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]'
    )
    print('Exception :')
    print('13')
    print('Output :')
    print(
        str(Solution().containVirus([[1, 1, 1, 0, 0, 0, 0, 0, 0],
                                     [1, 0, 1, 0, 1, 1, 1, 1, 1],
                                     [1, 1, 1, 0, 0, 0, 0, 0, 0]])))
    print()

    pass
# @lc main=end