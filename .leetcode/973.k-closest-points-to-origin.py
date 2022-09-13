# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
# https://leetcode.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (65.91%)
# Likes:    6474
# Dislikes: 235
# Total Accepted:    867.7K
# Total Submissions: 1.3M
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# Given an array of points where points[i] = [xi, yi] represents a point on the
# X-Y plane and an integer k, return the k closest points to the origin (0,
# 0).
#
# The distance between two points on the X-Y plane is the Euclidean distance
# (i.e., √(x1 - x2)^2 + (y1 - y2)^2).
#
# You may return the answer in any order. The answer is guaranteed to be unique
# (except for the order that it is in).
#
#
# Example 1:
#
#
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just
# [[-2,2]].
#
#
# Example 2:
#
#
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
#
#
#
# Constraints:
#
#
# 1 <= k <= points.length <= 10^4
# -10^4 < xi, yi < 10^4
#
#
#

# @lc tags=string;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求距离远点最近的n个点
# 堆，nlargest
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        return list(nlargest(k, points, key=lambda p: -(p[0]**2 + p[1]**2)))

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('points = [[1,3],[-2,2]], k = 1')
    print('Exception :')
    print('[[-2,2]]')
    print('Output :')
    print(str(Solution().kClosest([[1, 3], [-2, 2]], 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('points = [[3,3],[5,-1],[-2,4]], k = 2')
    print('Exception :')
    print('[[3,3],[-2,4]]')
    print('Output :')
    print(str(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2)))
    print()

    pass
# @lc main=end