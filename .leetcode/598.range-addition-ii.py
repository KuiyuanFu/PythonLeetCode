# @lc app=leetcode id=598 lang=python3
#
# [598] Range Addition II
#
# https://leetcode.com/problems/range-addition-ii/description/
#
# algorithms
# Easy (54.15%)
# Likes:    557
# Dislikes: 746
# Total Accepted:    71.3K
# Total Submissions: 131.7K
# Testcase Example:  '3\n3\n[[2,2],[3,3]]'
#
# You are given an m x n matrix M initialized with all 0's and an array of
# operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented
# by one for all 0 <= x < ai and 0 <= y < bi.
#
# Count and return the number of maximum integers in the matrix after
# performing all the operations.
#
#
# Example 1:
#
#
# Input: m = 3, n = 3, ops = [[2,2],[3,3]]
# Output: 4
# Explanation: The maximum integer in M is 2, and there are four of it in M. So
# return 4.
#
#
# Example 2:
#
#
# Input: m = 3, n = 3, ops =
# [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
# Output: 4
#
#
# Example 3:
#
#
# Input: m = 3, n = 3, ops = []
# Output: 9
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 4 * 10^4
# 0 <= ops.length <= 10^4
# ops[i].length == 2
# 1 <= ai <= m
# 1 <= bi <= n
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 在二维网格中，给定一些列的点，之后所有小于等于此点的点的值加一。
# 求最大值的个数。
# 就是求给定一系列点的两个坐标轴的最小值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        from functools import reduce
        ops.append([m, n])
        x, y = reduce(lambda a, b: (min(a[0], b[0]), min(a[1], b[1])), ops)
        return x * y
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('m = 3, n = 3, ops = [[2,2],[3,3]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().maxCount(3, 3, [[2, 2], [3, 3]])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'm = 3, n = 3, ops =[[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]'
    )
    print('Exception :')
    print('4')
    print('Output :')
    print(
        str(Solution().maxCount(
            3, 3, [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3],
                   [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('m = 3, n = 3, ops = []')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().maxCount(3, 3, [])))
    print()

    pass
# @lc main=end