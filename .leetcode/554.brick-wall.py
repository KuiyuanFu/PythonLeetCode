# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#
# https://leetcode.com/problems/brick-wall/description/
#
# algorithms
# Medium (52.00%)
# Likes:    1600
# Dislikes: 82
# Total Accepted:    92.9K
# Total Submissions: 178.6K
# Testcase Example:  '[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]'
#
# There is a rectangular brick wall in front of you with n rows of bricks. The
# i^th row has some number of bricks each of the same height (i.e., one unit)
# but they can be of different widths. The total width of each row is the
# same.
#
# Draw a vertical line from the top to the bottom and cross the least bricks.
# If your line goes through the edge of a brick, then the brick is not
# considered as crossed. You cannot draw a line just along one of the two
# vertical edges of the wall, in which case the line will obviously cross no
# bricks.
#
# Given the 2D array wall that contains the information about the wall, return
# the minimum number of crossed bricks after drawing such a vertical line.
#
#
# Example 1:
#
#
# Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# Output: 2
#
#
# Example 2:
#
#
# Input: wall = [[1],[1],[1]]
# Output: 3
#
#
#
# Constraints:
#
#
# n == wall.length
# 1 <= n <= 10^4
# 1 <= wall[i].length <= 10^4
# 1 <= sum(wall[i].length) <= 2 * 10^4
# sum(wall[i]) is the same for each row i.
# 1 <= wall[i][j] <= 2^31 - 1
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 砖墙，每一层的砖的宽度不同，求从上到下的一条线穿过最少的砖。
# 对砖右侧排序。统计同一位置有多少个缝隙。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        length = sum(wall[0])
        h = []
        for w in wall:
            b = 0
            for r in w:
                b += r
                heappush(h, b)
        res = 0
        preR, n = -1, 0
        while h[0] != length:
            r = heappop(h)
            if r == preR:
                n += 1
            else:
                preR, n = r, 1
            if n > res:
                res = n

        return len(wall) - res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4],
                                    [3, 1, 2], [1, 3, 1, 1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('wall = [[1],[1],[1]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().leastBricks([[1], [1], [1]])))
    print()

    pass
# @lc main=end