# @lc app=leetcode id=850 lang=python3
#
# [850] Rectangle Area II
#
# https://leetcode.com/problems/rectangle-area-ii/description/
#
# algorithms
# Hard (53.26%)
# Likes:    766
# Dislikes: 50
# Total Accepted:    28.9K
# Total Submissions: 54.2K
# Testcase Example:  '[[0,0,2,2],[1,0,2,3],[1,0,3,1]]'
#
# You are given a 2D array of axis-aligned rectangles. Each rectangle[i] =
# [xi1, yi1, xi2, yi2] denotes the i^th rectangle where (xi1, yi1) are the
# coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of
# the top-right corner.
#
# Calculate the total area covered by all rectangles in the plane. Any area
# covered by two or more rectangles should only be counted once.
#
# Return the total area. Since the answer may be too large, return it modulo
# 10^9 + 7.
#
#
# Example 1:
#
#
# Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# Output: 6
# Explanation: A total area of 6 is covered by all three rectangales, as
# illustrated in the picture.
# From (1,1) to (2,2), the green and red rectangles overlap.
# From (1,0) to (2,3), all three rectangles overlap.
#
#
# Example 2:
#
#
# Input: rectangles = [[0,0,1000000000,1000000000]]
# Output: 49
# Explanation: The answer is 10^18 modulo (10^9 + 7), which is 49.
#
#
#
# Constraints:
#
#
# 1 <= rectangles.length <= 200
# rectanges[i].length == 4
# 0 <= xi1, yi1, xi2, yi2 <= 10^9
#
#
#

# @lc tags=linked-list

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 被矩形覆盖的区域。
# 按照高度遍历
# O n^2
#
# @lc idea=end

# @lc group=

# @lc rank=10


# @lc code=start
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:

        edges = []
        heights = set()

        for x1, y1, x2, y2 in rectangles:
            edges.append((x1, True, y1, y2))
            edges.append((x2, False, y1, y2))
            heights.add(y1)
            heights.add(y2)
        edges.sort()
        heights = sorted(heights)

        area = 0

        for i in range(1, len(heights)):
            hl, hu = heights[i - 1], heights[i]
            weith = 0
            times = 0
            edgeL = 0
            for x, f, y1, y2 in edges:
                if y1 <= hl and hu <= y2:
                    if f:
                        times += 1
                        if times == 1:
                            edgeL = x
                    else:
                        times -= 1
                        if times == 0:
                            edgeR = x
                            weith += edgeR - edgeL
            area += weith * (hu - hl)
        return area % (1000000007)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]')
    print('Exception :')
    print('6')
    print('Output :')
    print(
        str(Solution().rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3,
                                                                   1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('rectangles = [[0,0,1000000000,1000000000]]')
    print('Exception :')
    print('49')
    print('Output :')
    print(str(Solution().rectangleArea([[0, 0, 1000000000, 1000000000]])))
    print()

    pass
# @lc main=end