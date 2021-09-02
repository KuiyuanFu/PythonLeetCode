# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs/description/
#
# algorithms
# Medium (52.84%)
# Likes:    495
# Dislikes: 786
# Total Accepted:    75.9K
# Total Submissions: 143.6K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# You are given n points in the plane that are all distinct, where points[i] =
# [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance
# between i and j equals the distance between i and k (the order of the tuple
# matters).
#
# Return the number of boomerangs.
#
#
# Example 1:
#
#
# Input: points = [[0,0],[1,0],[2,0]]
# Output: 2
# Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and
# [[1,0],[2,0],[0,0]].
#
#
# Example 2:
#
#
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 2
#
#
# Example 3:
#
#
# Input: points = [[1,1]]
# Output: 0
#
#
#
# Constraints:
#
#
# n == points.length
# 1 <= n <= 500
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# All the points are unique.
#
#
#

# @lc tags=hash-table

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求距离同一个点距离相同的对数。
# 对于每个节点，通过到其他节点的距离个数，之后相同距离大于2个，即可组成一对。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        buffer = [defaultdict(int) for _ in range(len(points))]
        for i in range(1, len(points)):
            ix, iy = points[i]
            for j in range(i):
                jx, jy = points[j]
                l = sqrt((ix - jx)**2 + (iy - jy)**2)
                buffer[i][l] += 1
                buffer[j][l] += 1
        res = 0
        for d in buffer:
            for n in d.values():
                if n >= 2:
                    res += n * (n - 1)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('points = [[0,0],[1,0],[2,0]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numberOfBoomerangs([[0, 0], [1, 0], [2, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('points = [[1,1],[2,2],[3,3]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numberOfBoomerangs([[1, 1], [2, 2], [3, 3]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('points = [[1,1]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().numberOfBoomerangs([[1, 1]])))
    print()

    pass
# @lc main=end