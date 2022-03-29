# @lc app=leetcode id=864 lang=python3
#
# [864] Shortest Path to Get All Keys
#
# https://leetcode.com/problems/shortest-path-to-get-all-keys/description/
#
# algorithms
# Hard (44.29%)
# Likes:    752
# Dislikes: 25
# Total Accepted:    22.6K
# Total Submissions: 50.9K
# Testcase Example:  '["@.a.#","###.#","b.A.B"]'
#
# You are given an m x n grid grid where:
#
#
# '.' is an empty cell.
# '#' is a wall.
# '@' is the starting point.
# Lowercase letters represent keys.
# Uppercase letters represent locks.
#
#
# You start at the starting point and one move consists of walking one space in
# one of the four cardinal directions. You cannot walk outside the grid, or
# walk into a wall.
#
# If you walk over a key, you can pick it up and you cannot walk over a lock
# unless you have its corresponding key.
#
# For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter
# of the first k letters of the English alphabet in the grid. This means that
# there is exactly one key for each lock, and one lock for each key; and also
# that the letters used to represent the keys and locks were chosen in the same
# order as the English alphabet.
#
# Return the lowest number of moves to acquire all keys. If it is impossible,
# return -1.
#
#
# Example 1:
#
#
# Input: grid = ["@.a.#","###.#","b.A.B"]
# Output: 8
# Explanation: Note that the goal is to obtain all the keys not to open all the
# locks.
#
#
# Example 2:
#
#
# Input: grid = ["@..aA","..B#.","....b"]
# Output: 6
#
#
# Example 3:
#
#
# Input: grid = ["@Aa"]
# Output: -1
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 30
# grid[i][j] is either an English letter, '.', '#', or '@'.
# The number of keys in the grid is in the range [1, 6].
# Each key in the grid is unique.
# Each key in the grid has a matching lock.
#
#
#

# @lc tags=array

# @lc imports=start
from ast import Str
from operator import truediv
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最短移动次数，找到所有钥匙。
# 直接暴力。
# 剪枝
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:

        maxMoveNumber = 30 * 30 * 6
        row, col = len(grid), len(grid[0])
        for i in range(row):
            grid[i] = list(grid[i])

        keys = {}
        locks = {}

        def searchKeys():
            k = 0
            for i, j in product(range(row), range(col)):
                if grid[i][j].islower():
                    keys[grid[i][j]] = (i, j)
                    k += 1
                if grid[i][j].isupper():
                    locks[grid[i][j].lower()] = (i, j)
                if grid[i][j] == '@':
                    startingPoint = (i, j)
                    grid[i][j] = '.'
            return startingPoint, k

        startingPoint, k = searchKeys()

        def generateVisitedGrid():
            return [[False for _ in range(col)] for _ in range(row)]

        offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def generateNIJ(i, j):
            res = []
            for oi, oj in offset:
                ni, nj = i + oi, j + oj
                if 0 <= ni < row and 0 <= nj < col:
                    res.append((ni, nj))
            return res

        def search(st: Tuple[int, int]):
            visited = generateVisitedGrid()
            visited[st[0]][st[1]] = True
            ls = []
            dp = [(st[0], st[1])]
            sn = 0
            while dp:
                dpn = []
                for i, j in dp:

                    if grid[i][j].islower():
                        ls.append((grid[i][j], sn))
                    for ni, nj in generateNIJ(i, j):

                        if not visited[ni][nj] and (grid[ni][nj] == '.'
                                                    or grid[ni][nj].islower()):
                            visited[ni][nj] = True
                            dpn.append((ni, nj))
                dp = dpn
                sn += 1
            return ls

        buffer = {}

        def recur(visited: List[str], st: Tuple[int, int]):
            bufferKey = ''.join(visited) + str(st)
            if bufferKey in buffer:
                return buffer[bufferKey]
            if len(visited) == k:
                return 0
            ls = search(st)
            res = maxMoveNumber
            for key, l in ls:
                keyI, keyJ = keys[key]
                lockI, lockJ = locks[key]
                grid[keyI][keyJ] = '.'
                grid[lockI][lockJ] = '.'
                visitedCopy = visited.copy()
                visitedCopy.append(key)
                visitedCopy.sort()
                res = min(res, l + recur(visitedCopy, (keyI, keyJ)))

                grid[keyI][keyJ] = key
                grid[lockI][lockJ] = key.upper()
            buffer[bufferKey] = res
            return res

        res = recur([], startingPoint)
        return res if res < maxMoveNumber else -1

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().shortestPathAllKeys([
            "#.............c.#.#...#.#.#.C.", ".##...#....#..#..##...........",
            "....##..........#...#..#....#.", ".a......#..#.#...#...#......##",
            "........#......##.............", "..#......E.#..##.......#......",
            ".#........B.#.#....#.........#", "A....#.##.....#..#............",
            "..#F#.#....#..###..##..#..##..", "...#.##.#..........#..#.......",
            "#....#....#..#......#...#....#", "#..#.#...........#........#.#.",
            "#.#.....##....#..#..#....##.#.", ".#..D..##...##.....###......#.",
            "...#.....###...#....#.#...#.#.", "#......#.......##..###........",
            ".............##..#.......#....", ".#####...##.....#...#....#.#..",
            "..#....@..#.#.#.....#..##.....", "#..##.#..#..#..f.#.#..........",
            ".#.......#....#.......#.#..#..", "..........#.........d#.......#",
            "......#....................#..", "#..#...#...#...#....#...#e.#..",
            ".............#.....#..b.....##", ".#......#...........##..#.....",
            ".....#................###.....", "....#....#..#..#..#......#..#.",
            "......##.....#.##.#.#...#....#", ".....##.#.......#.#....#.#.##."
        ])))
    print(
        str(Solution().shortestPathAllKeys([
            ".#......###..#.", ".###C..#...b...", "..#..#.........",
            ".........#.....", ".....@#.#......", "#.##...#..##...",
            "..d#...a...#...", "..###..........", "........#....#.",
            "..#.#..#...c#.#", "D#..........#.#", "............#A.",
            "..#..##...#....", "#...#..#..B....", ".....##.....#.."
        ])))
    print(
        str(Solution().shortestPathAllKeys([
            "..#....##.", "....d.#.D#", "#...#.c...", "..##.#..a.",
            "...#....##", "#....b....", ".#..#.....", "..........",
            ".#..##..A.", ".B..C.#..@"
        ])))

    print('Example 2:')
    print('Input : ')
    print('grid = ["@..aA","..B#.","....b"]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().shortestPathAllKeys(["@..aA", "..B#.", "....b"])))
    print()
    print('Example 1:')
    print('Input : ')
    print('grid = ["@.a.#","###.#","b.A.B"]')
    print('Exception :')
    print('8')
    print('Output :')
    print(str(Solution().shortestPathAllKeys(["@.a.#", "###.#", "b.A.B"])))
    print()
    print('Example 3:')
    print('Input : ')
    print('grid = ["@Aa"]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().shortestPathAllKeys(["@Aa"])))
    print()

    pass
# @lc main=end