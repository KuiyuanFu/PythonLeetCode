# @lc app=leetcode id=497 lang=python3
#
# [497] Random Point in Non-overlapping Rectangles
#
# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/description/
#
# algorithms
# Medium (39.08%)
# Likes:    355
# Dislikes: 562
# Total Accepted:    32.1K
# Total Submissions: 82.2K
# Testcase Example:  '["Solution","pick","pick","pick","pick","pick"]\n' +
# '[[[[-2,-2,1,1],[2,2,4,6]]],[],[],[],[],[]]'
#
# You are given an array of non-overlapping axis-aligned rectangles rects where
# rects[i] = [ai, bi, xi, yi] indicates that (ai, bi) is the bottom-left corner
# point of the i^th rectangle and (xi, yi) is the top-right corner point of the
# i^th rectangle. Design an algorithm to pick a random integer point inside the
# space covered by one of the given rectangles. A point on the perimeter of a
# rectangle is included in the space covered by the rectangle.
#
# Any integer point inside the space covered by one of the given rectangles
# should be equally likely to be returned.
#
# Note that an integer point is a point that has integer coordinates.
#
# Implement the Solution class:
#
#
# Solution(int[][] rects) Initializes the object with the given rectangles
# rects.
# int[] pick() Returns a random integer point [u, v] inside the space covered
# by one of the given rectangles.
#
#
#
# Example 1:
#
#
# Input
# ["Solution", "pick", "pick", "pick", "pick", "pick"]
# [[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
# Output
# [null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]
#
# Explanation
# Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
# solution.pick(); // return [1, -2]
# solution.pick(); // return [1, -1]
# solution.pick(); // return [-1, -2]
# solution.pick(); // return [-2, -2]
# solution.pick(); // return [0, 0]
#
#
#
# Constraints:
#
#
# 1 <= rects.length <= 100
# rects[i].length == 4
# -10^9 <= ai < xi <= 10^9
# -10^9 <= bi < yi <= 10^9
# xi - ai <= 2000
# yi - bi <= 2000
# All the rectangles do not overlap.
# At most 10^4 calls will be made to pick.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from warnings import resetwarnings
from imports import *

# @lc imports=end

# @lc idea=start
#
# 在不重叠的给定矩形区域内随机选择一个整数点。
# 根据每个矩形区域的大小，即整数点个数，来确定权重，根据随机值与总权重确定矩形位置。之后再根据剩余值，确定在这个矩形内的位置，加上偏移量即可。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def __init__(self, rects: List[List[int]]):
        self.total = 0
        self.rects = rects
        self.orders = []
        for r in rects:
            self.orders.append(self.total)
            left, bottom, right, top = r
            self.total += (top - bottom + 1) * (right - left + 1)

    def pick(self) -> List[int]:

        r = random.randint(0, self.total - 1)
        idx = bisect_right(self.orders, r) - 1
        r -= self.orders[idx]
        left, bottom, right, top = self.rects[idx]
        l = right - left + 1
        xr = left + r % l
        yr = bottom + r // l
        return [xr, yr]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('')
    print('Exception :')
    print('')
    print('Output :')
    print(str(Solution().__init__(error)))
    print()

    pass
# @lc main=end