# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#
# https://leetcode.com/problems/two-city-scheduling/description/
#
# algorithms
# Medium (64.91%)
# Likes:    4099
# Dislikes: 307
# Total Accepted:    203.6K
# Total Submissions: 313.6K
# Testcase Example:  '[[10,20],[30,200],[400,50],[30,20]]'
#
# A company is planning to interview 2n people. Given the array costs where
# costs[i] = [aCosti, bCosti], the cost of flying the i^th person to city a is
# aCosti, and the cost of flying the i^th person to city b is bCosti.
#
# Return the minimum cost to fly every person to a city such that exactly n
# people arrive in each city.
#
#
# Example 1:
#
#
# Input: costs = [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation:
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
#
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
# interviewing in each city.
#
#
# Example 2:
#
#
# Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# Output: 1859
#
#
# Example 3:
#
#
# Input: costs =
# [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
# Output: 3086
#
#
#
# Constraints:
#
#
# 2 * n == costs.length
# 2 <= costs.length <= 100
# costs.length is even.
# 1 <= aCosti, bCosti <= 1000
#
#
#

# @lc tags=hash-table;tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定2n个元素，每个元素分别给定到各组的代价，分成两组，求最小代价。
# 求差值，排序。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        s = [(c[0] - c[1], c) for c in costs]
        s.sort()

        res = sum(s[i][1][0] for i in range(len(costs) // 2)) + sum(
            s[i][1][1] for i in range(len(costs) // 2, len(costs)))
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('costs = [[10,20],[30,200],[400,50],[30,20]]')
    print('Exception :')
    print('110')
    print('Output :')
    print(
        str(Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50],
                                         [30, 20]])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]')
    print('Exception :')
    print('1859')
    print('Output :')
    print(
        str(Solution().twoCitySchedCost([[259, 770], [448, 54], [926, 667],
                                         [184, 139], [840, 118], [577, 469]])))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'costs =[[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]'
    )
    print('Exception :')
    print('3086')
    print('Output :')
    print(
        str(Solution().twoCitySchedCost([[515, 563], [451, 713], [537, 709],
                                         [343, 819], [855, 779], [457, 60],
                                         [650, 359], [631, 42]])))
    print()

    pass
# @lc main=end