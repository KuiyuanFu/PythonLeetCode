# @lc app=leetcode id=1036 lang=python3
#
# [1036] Escape a Large Maze
#
# https://leetcode.com/problems/escape-a-large-maze/description/
#
# algorithms
# Hard (34.10%)
# Likes:    551
# Dislikes: 155
# Total Accepted:    17.7K
# Total Submissions: 51.9K
# Testcase Example:  '[[0,1],[1,0]]\n[0,0]\n[0,2]'
#
# There is a 1 million by 1 million grid on an XY-plane, and the coordinates of
# each grid square are (x, y).
#
# We start at the source = [sx, sy] square and want to reach the target = [tx,
# ty] square. There is also an array of blocked squares, where each blocked[i]
# = [xi, yi] represents a blocked square with coordinates (xi, yi).
#
# Each move, we can walk one square north, east, south, or west if the square
# is not in the array of blocked squares. We are also not allowed to walk
# outside of the grid.
#
# Return true if and only if it is possible to reach the target square from the
# source square through a sequence of valid moves.
#
#
# Example 1:
#
#
# Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
# Output: false
# Explanation: The target square is inaccessible starting from the source
# square because we cannot move.
# We cannot move north or east because those squares are blocked.
# We cannot move south or west because we cannot go outside of the grid.
#
#
# Example 2:
#
#
# Input: blocked = [], source = [0,0], target = [999999,999999]
# Output: true
# Explanation: Because there are no blocked cells, it is possible to reach the
# target square.
#
#
#
# Constraints:
#
#
# 0 <= blocked.length <= 200
# blocked[i].length == 2
# 0 <= xi, yi < 10^6
# source.length == target.length == 2
# 0 <= sx, sy, tx, ty < 10^6
# source != target
# It is guaranteed that source and target are not blocked.
#
#
#

# @lc tags=breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 一个一百万乘一百万的网格，给定禁止进入的位置，判断是否可以从起点到终点。
# 判断是否可以将起点或终点围住。禁止进入位置围成的最大区域面积是固定的，如果从起点和终点出发，有超过此面积的区域可以到达，说明没有被围住。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int],
                         target: List[int]) -> bool:
        maxAreaCount = len(blocked)**2 // 2
        blocked = set(tuple(t) for t in blocked)
        offsets = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        s, t = tuple(source), tuple(target)
        for s, t in [(s, t), (t, s)]:
            q = [s]
            v = set(q)
            for _ in range(maxAreaCount):
                if len(q) == 0:
                    return False
                now = q.pop()
                if now == t:
                    return True
                i, j = now
                for oi, oj in offsets:
                    ni, nj = i + oi, j + oj
                    if 0 <= ni < 10**6 and 0 <= nj < 10**6 and (
                            ni, nj) not in blocked and (ni, nj) not in v:
                        v.add((ni, nj))
                        q.append((ni, nj))
        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isEscapePossible([[0, 1], [1, 0]], [0, 0], [0, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('blocked = [], source = [0,0], target = [999999,999999]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isEscapePossible([], [0, 0], [999999, 999999])))
    print()

    pass
# @lc main=end