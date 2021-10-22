# @lc app=leetcode id=699 lang=python3
#
# [699] Falling Squares
#
# https://leetcode.com/problems/falling-squares/description/
#
# algorithms
# Hard (43.51%)
# Likes:    393
# Dislikes: 68
# Total Accepted:    17.9K
# Total Submissions: 41.1K
# Testcase Example:  '[[1,2],[2,3],[6,1]]'
#
# There are several squares being dropped onto the X-axis of a 2D plane.
#
# You are given a 2D integer array positions where positions[i] = [lefti,
# sideLengthi] represents the i^th square with a side length of sideLengthi
# that is dropped with its left edge aligned with X-coordinate lefti.
#
# Each square is dropped one at a time from a height above any landed squares.
# It then falls downward (negative Y direction) until it either lands on the
# top side of another square or on the X-axis. A square brushing the left/right
# side of another square does not count as landing on it. Once it lands, it
# freezes in place and cannot be moved.
#
# After each square is dropped, you must record the height of the current
# tallest stack of squares.
#
# Return an integer array ans where ans[i] represents the height described
# above after dropping the i^th square.
#
#
# Example 1:
#
#
# Input: positions = [[1,2],[2,3],[6,1]]
# Output: [2,5,5]
# Explanation:
# After the first drop, the tallest stack is square 1 with a height of 2.
# After the second drop, the tallest stack is squares 1 and 2 with a height of
# 5.
# After the third drop, the tallest stack is still squares 1 and 2 with a
# height of 5.
# Thus, we return an answer of [2, 5, 5].
#
#
# Example 2:
#
#
# Input: positions = [[100,100],[200,100]]
# Output: [100,100]
# Explanation:
# After the first drop, the tallest stack is square 1 with a height of 100.
# After the second drop, the tallest stack is either square 1 or square 2, both
# with heights of 100.
# Thus, we return an answer of [100, 100].
# Note that square 2 only brushes the right side of square 1, which does not
# count as landing on it.
#
#
#
# Constraints:
#
#
# 1 <= positions.length <= 1000
# 1 <= lefti <= 10^8
# 1 <= sideLengthi <= 10^6
#
#
#

# @lc tags=segment-tree;ordered-map

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 方块依次下落，记录最大高度。
# 线段树。二分搜索。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        res = []
        m = 0
        dp = [[0, 0]]

        for l, h in positions:
            r = l + h
            idxL = bisect_left(dp, [l + 1, -1]) - 1
            idxR = bisect_right(dp, [r, -1])
            h += 0 if idxL == idxR else \
                 max(dp[i][1] for i in range(idxL, idxR))
            m = max(m, h)
            res.append(m)
            dp = dp[:idxL + 1] + [[l, h], [r, dp[idxR - 1][1]]] + dp[idxR:]
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('positions = [[1,2],[2,3],[6,1]]')
    print('Exception :')
    print('[2,5,5]')
    print('Output :')
    print(str(Solution().fallingSquares([[1, 2], [2, 3], [6, 1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('positions = [[100,100],[200,100]]')
    print('Exception :')
    print('[100,100]')
    print('Output :')
    print(str(Solution().fallingSquares([[100, 100], [200, 100]])))
    print()
    print('Example 2:')
    print('Input : ')
    print(
        'positions =[[2,82],[57,22],[16,66],[46,15],[5,11],[9,83],[1,32],[87,91],[64,61],[87,53]]'
    )
    print('Exception :')
    print('[82,104,170,185,185,268,300,359,420,473]')
    print('Output :')
    print(
        str(Solution().fallingSquares([[2, 82], [57, 22], [16, 66], [46, 15],
                                       [5, 11], [9, 83], [1, 32], [87, 91],
                                       [64, 61], [87, 53]])))
    print()
    pass
# @lc main=end