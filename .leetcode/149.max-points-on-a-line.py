# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (18.06%)
# Likes:    217
# Dislikes: 53
# Total Accepted:    185K
# Total Submissions: 1M
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given an array of points where points[i] = [xi, yi] represents a point on the
# X-Y plane, return the maximum number of points that lie on the same straight
# line.
#
#
# Example 1:
#
#
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
#
#
# Example 2:
#
#
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= points.length <= 300
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# All the points are unique.
#
#
#

# @lc tags=hash-table;math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一系列点，求共线的点的最多个数。
# 朴素的思想是，保存每一条线的表达式，之后一次判断是否在线上，这样是 O n^3，很慢。
# 比较好的思想是，不保存所有的线，每一次指定一个点，为核心点，之后计算其他点到其的斜率，这样就相当于指定了定点，线的参数可以简化为斜率，这个斜率使用斜率的比值形式存储。这样也没有了平行线的问题。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
from collections import defaultdict


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)

        result = 2
        for i in range(len(points)):
            count = defaultdict(int)
            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                g = gcd(dy, dx)
                count[str(dx // g) + ':' + str(dy // g)] += 1
            if len(count) > 0:
                m = max(list(count.values()))
                result = max(result, m + 1)
        return result
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('points = [[1,1],[2,2],[3,3]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().maxPoints([[1, 1], [2, 2], [3, 3]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(
        str(Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3],
                                  [1, 4]])))
    print()

    pass
# @lc main=end