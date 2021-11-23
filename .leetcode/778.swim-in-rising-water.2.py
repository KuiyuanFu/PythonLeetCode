# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#
# https://leetcode.com/problems/swim-in-rising-water/description/
#
# algorithms
# Hard (57.81%)
# Likes:    1582
# Dislikes: 113
# Total Accepted:    61.1K
# Total Submissions: 105.2K
# Testcase Example:  '[[0,2],[1,3]]'
#
# You are given an n x n integer matrix grid where each value grid[i][j]
# represents the elevation at that point (i, j).
#
# The rain starts to fall. At time t, the depth of the water everywhere is t.
# You can swim from a square to another 4-directionally adjacent square if and
# only if the elevation of both squares individually are at most t. You can
# swim infinite distances in zero time. Of course, you must stay within the
# boundaries of the grid during your swim.
#
# Return the least time until you can reach the bottom right square (n - 1, n -
# 1) if you start at the top left square (0, 0).
#
#
# Example 1:
#
#
# Input: grid = [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a
# higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.
#
#
# Example 2:
#
#
# Input: grid =
# [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation: The final route is shown.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
#
#
#
# Constraints:
#
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] < n^2
# Each value grid[i][j] is unique.
#
#
#

# @lc tags=string;heap;greedy;sort

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 从左上移动到右下，下雨，t时刻，水深t，只能在t高度移动。
# 找能达到的最小值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        target = (n - 1, n - 1)
        if n == 0:
            return 0

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        res = max(grid[-1][-1], grid[0][0])
        s = [(0, 0)]
        visited = set(s)
        heap = []
        while True:
            while s:
                tu = s.pop()

                i, j = tu
                if tu == target:
                    return res
                for oi, oj in directions:
                    tu2 = i + oi, j + oj
                    ni, nj = tu2

                    if 0 <= ni < n and 0 <= nj < n:
                        if tu2 in visited:
                            continue
                        visited.add(tu2)
                        v = grid[ni][nj]
                        if v <= res:
                            s.append(tu2)
                        else:
                            heappush(heap, (v, tu2))
            if heap:
                res = heap[0][0]

            else:
                break
            while heap and heap[0][0] <= res:
                t = heappop(heap)[1]
                s.append(t)
        return -1
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'grid = [[10,27,37,77,87,49,70,85,90,40],[73,63,50,8,5,98,20,19,52,32],[99,46,45,86,96,91,42,38,97,0],[21,78,79,62,35,2,48,81,89,80],[13,22,53,12,34,75,36,18,88,23],[95,9,59,84,72,25,74,65,83,4],[43,47,58,30,3,31,57,69,28,92],[6,7,94,82,54,67,61,39,33,55],[60,15,41,68,24,56,1,76,14,64],[29,16,71,44,17,93,51,11,26,66]]'
    )
    print('Exception :')
    print('78')
    print('Output :')
    print(
        str(Solution().swimInWater([[10, 27, 37, 77, 87, 49, 70, 85, 90, 40],
                                    [73, 63, 50, 8, 5, 98, 20, 19, 52, 32],
                                    [99, 46, 45, 86, 96, 91, 42, 38, 97, 0],
                                    [21, 78, 79, 62, 35, 2, 48, 81, 89, 80],
                                    [13, 22, 53, 12, 34, 75, 36, 18, 88, 23],
                                    [95, 9, 59, 84, 72, 25, 74, 65, 83, 4],
                                    [43, 47, 58, 30, 3, 31, 57, 69, 28, 92],
                                    [6, 7, 94, 82, 54, 67, 61, 39, 33, 55],
                                    [60, 15, 41, 68, 24, 56, 1, 76, 14, 64],
                                    [29, 16, 71, 44, 17, 93, 51, 11, 26,
                                     66]])))
    print()

    print('Example 1:')
    print('Input : ')
    print('grid = [[0,2],[1,3]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().swimInWater([[0, 2], [1, 3]])))
    print()
    print('Example 1:')
    print('Input : ')
    print('grid = [[3,2],[0,1]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().swimInWater([[3, 2], [0, 1]])))
    print()
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'grid =[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]'
    )
    print('Exception :')
    print('16')
    print('Output :')
    print(
        str(Solution().swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5],
                                    [12, 13, 14, 15, 16], [11, 17, 18, 19, 20],
                                    [10, 9, 8, 7, 6]])))
    print()

    pass
# @lc main=end