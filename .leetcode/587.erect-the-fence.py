# @lc app=leetcode id=587 lang=python3
#
# [587] Erect the Fence
#
# https://leetcode.com/problems/erect-the-fence/description/
#
# algorithms
# Hard (38.16%)
# Likes:    501
# Dislikes: 327
# Total Accepted:    22.8K
# Total Submissions: 52.9K
# Testcase Example:  '[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]'
#
# You are given an array trees where trees[i] = [xi, yi] represents the
# location of a tree in the garden.
#
# You are asked to fence the entire garden using the minimum length of rope as
# it is expensive. The garden is well fenced only if all the trees are
# enclosed.
#
# Return the coordinates of trees that are exactly located on the fence
# perimeter.
#
#
# Example 1:
#
#
# Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
#
#
# Example 2:
#
#
# Input: points = [[1,2],[2,2],[4,2]]
# Output: [[4,2],[2,2],[1,2]]
#
#
#
# Constraints:
#
#
# 1 <= points.length <= 3000
# points[i].length == 2
# 0 <= xi, yi <= 100
# All the given points are unique.
#
#
#

# @lc tags=geometry

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定树的坐标，设计篱笆围住所有的树，返回篱笆边界上的树。
# 先排序，从最左侧点开始，分为上下两部分，分别求上边界与下边界。使用斜率，计算是否是凸的。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 2:
            return trees

        def cmp(a, b, c):
            ax, ay = a
            bx, by = b
            cx, cy = c
            return (cy - ay) * (bx - ax) - (by - ay) * (cx - ax)

        trees.sort()
        upper = []
        lower = []
        for c in trees:
            c = tuple(c)

            while len(upper) >= 2 and cmp(upper[-2], upper[-1], c) > 0:
                upper.pop()
            while len(lower) >= 2 and cmp(lower[-2], lower[-1], c) < 0:
                lower.pop()
            upper.append(c)
            lower.append(c)
        return list(list(c) for c in set(upper + lower))


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]')
    print('Exception :')
    print('[[1,1],[2,0],[3,3],[2,4],[4,2]]')
    print('Output :')
    print(
        str(Solution().outerTrees([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3],
                                   [4, 2]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('points = [[1,2],[2,2],[4,2]]')
    print('Exception :')
    print('[[4,2],[2,2],[1,2]]')
    print('Output :')
    print(str(Solution().outerTrees([[4, 2], [2, 2], [1, 2]])))
    print()

    pass
# @lc main=end