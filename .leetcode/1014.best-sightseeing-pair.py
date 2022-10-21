# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#
# https://leetcode.com/problems/best-sightseeing-pair/description/
#
# algorithms
# Medium (59.53%)
# Likes:    2058
# Dislikes: 45
# Total Accepted:    74K
# Total Submissions: 124.3K
# Testcase Example:  '[8,1,5,2,6]'
#
# You are given an integer array values where values[i] represents the value of
# the i^th sightseeing spot. Two sightseeing spots i and j have a distance j -
# i between them.
#
# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i
# - j: the sum of the values of the sightseeing spots, minus the distance
# between them.
#
# Return the maximum score of a pair of sightseeing spots.
#
#
# Example 1:
#
#
# Input: values = [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 =
# 11
#
#
# Example 2:
#
#
# Input: values = [1,2]
# Output: 2
#
#
#
# Constraints:
#
#
# 2 <= values.length <= 5 * 10^4
# 1 <= values[i] <= 1000
#
#
#

# @lc tags=divide-and-conquer;heap;sort

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 景点有一个分值，一对经典的分值为分值之和减去距离
# 计算左右节点则真实贡献，之后增序排列
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        res = 0
        ls, rs = [], []
        for d, v in enumerate(values):

            lv, rv = v + d, v - d

            ls.append((d, lv))
            while len(rs) > 0 and rs[-1][1] < rv:
                rs.pop()
            rs.append((d, rv))
        ri = 0
        for li, rv in ls:

            while ri < len(rs) and rs[ri][0] <= li:
                ri += 1
            if ri < len(rs):
                res = max(res, rv + rs[ri][1])

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('values = [10,4,6,4,10]')
    print('Exception :')
    print('16')
    print('Output :')
    print(str(Solution().maxScoreSightseeingPair([10, 4, 6, 4, 10])))
    print()
    print('Example 1:')
    print('Input : ')
    print('values = [8,1,5,2,6]')
    print('Exception :')
    print('11')
    print('Output :')
    print(str(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6])))
    print()

    print('Example 2:')
    print('Input : ')
    print('values = [1,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().maxScoreSightseeingPair([1, 2])))
    print()

    pass
# @lc main=end