# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#
# https://leetcode.com/problems/the-skyline-problem/description/
#
# algorithms
# Hard (36.96%)
# Likes:    2982
# Dislikes: 166
# Total Accepted:    174.8K
# Total Submissions: 471.7K
# Testcase Example:  '[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]'
#
# A city's skyline is the outer contour of the silhouette formed by all the
# buildings in that city when viewed from a distance. Given the locations and
# heights of all the buildings, return the skyline formed by these buildings
# collectively.
#
# The geometric information of each building is given in the array buildings
# where buildings[i] = [lefti, righti, heighti]:
#
#
# lefti is the x coordinate of the left edge of the i^th building.
# righti is the x coordinate of the right edge of the i^th building.
# heighti is the height of the i^th building.
#
#
# You may assume all buildings are perfect rectangles grounded on an absolutely
# flat surface at height 0.
#
# The skyline should be represented as a list of "key points" sorted by their
# x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left
# endpoint of some horizontal segment in the skyline except the last point in
# the list, which always has a y-coordinate 0 and is used to mark the skyline's
# termination where the rightmost building ends. Any ground between the
# leftmost and rightmost buildings should be part of the skyline's contour.
#
# Note: There must be no consecutive horizontal lines of equal height in the
# output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is
# not acceptable; the three lines of height 5 should be merged into one in the
# final output as such: [...,[2 3],[4 5],[12 7],...]
#
#
# Example 1:
#
#
# Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# Explanation:
# Figure A shows the buildings of the input.
# Figure B shows the skyline formed by those buildings. The red points in
# figure B represent the key points in the output list.
#
#
# Example 2:
#
#
# Input: buildings = [[0,2,3],[2,5,3]]
# Output: [[0,3],[5,0]]
#
#
#
# Constraints:
#
#
# 1 <= buildings.length <= 10^4
# 0 <= lefti < righti <= 2^31 - 1
# 1 <= heighti <= 2^31 - 1
# buildings is sorted by lefti in non-decreasing order.
#
#
#

# @lc tags=divide-and-conquer;heap;binary-indexed-tree;segment-tree;line-sweep

# @lc imports=start
from heapq import heappop, heappush
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求天际线，给定建筑的左右边际和高度，得到所有高度改变的位置及高度。
# 从左到右，一次判断最高建筑。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start

import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        import heapq
        # building: left right height
        buildings.sort()
        self.buildings = buildings
        # heap: height right
        self.h = []
        # left height
        self.results = []

        self.addAllBuidlings()

        return self.results

    def addAllBuidlings(self, ):

        for building in self.buildings:
            self.addBuilding(building)
        while self.h:
            position = self.h[0][1]
            height = self.getNextLevel(position)
            self.addResult([position, height])

    def addBuilding(self, building):

        while self.h and self.h[0][1] <= building[0]:
            position = self.h[0][1]
            height = self.getNextLevel(position)
            self.addResult([position, height])
        if not self.h or building[2] > -self.h[0][0]:
            self.addResult([building[0], building[2]])
        heappush(self.h, [-building[2], building[1]])
        pass

    def getNextLevel(self, position):

        while self.h:
            if self.h[0][1] <= position:
                heappop(self.h)
            else:
                return -self.h[0][0]
        return 0

    def addResult(self, result):
        while self.results:
            resultLast = self.results[-1]
            if resultLast[1] == result[1]:
                return
            if resultLast[0] == result[0]:
                self.results.pop()
            else:
                break
        self.results.append(result)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]')
    print('Exception :')
    print('[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]')
    print('Output :')
    print(
        str(Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12],
                                   [15, 20, 10], [19, 24, 8]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('buildings = [[0,2,3],[2,5,3]]')
    print('Exception :')
    print('[[0,3],[5,0]]')
    print('Output :')
    print(str(Solution().getSkyline([[0, 2, 3], [2, 5, 3]])))
    print()

    pass
# @lc main=end