# @lc app=leetcode id=879 lang=python3
#
# [879] Profitable Schemes
#
# https://leetcode.com/problems/profitable-schemes/description/
#
# algorithms
# Hard (40.63%)
# Likes:    437
# Dislikes: 40
# Total Accepted:    14.6K
# Total Submissions: 36K
# Testcase Example:  '5\n3\n[2,2]\n[2,3]'
#
# There is a group of n members, and a list of various crimes they could
# commit. The i^th crime generates a profit[i] and requires group[i] members to
# participate in it. If a member participates in one crime, that member can't
# participate in another crime.
#
# Let's call a profitable scheme any subset of these crimes that generates at
# least minProfit profit, and the total number of members participating in that
# subset of crimes is at most n.
#
# Return the number of schemes that can be chosen. Since the answer may be very
# large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# Output: 2
# Explanation: To make a profit of at least 3, the group could either commit
# crimes 0 and 1, or just crime 1.
# In total, there are 2 schemes.
#
# Example 2:
#
#
# Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
# Output: 7
# Explanation: To make a profit of at least 5, the group could commit any
# crimes, as long as they commit one.
# There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and
# (0,1,2).
#
#
# Constraints:
#
#
# 1 <= n <= 100
# 0 <= minProfit <= 100
# 1 <= group.length <= 100
# 1 <= group[i] <= 100
# profit.length == group.length
# 0 <= profit[i] <= 100
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 不同的犯罪方案，有使用人数和收益，问在给定最低收益情况下，有多少种方案。
# 存储收益与剩余人数
# DP。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def profitableSchemes(self, members: int, minProfit: int,
                          groups: List[int], profits: List[int]) -> int:
        membersLength = members + 1
        profitLength = minProfit + 1
        groupsLength = len(groups) + 1
        dpOld = [[0 for _ in range(profitLength)]
                 for _ in range(membersLength)]

        dpOld[-1][0] = 1

        for groupIdx in range(groupsLength - 1):

            dpNew = dpOld.copy()
            profit = profits[groupIdx]
            menber = groups[groupIdx]

            for memberIdx in range(menber, membersLength):
                for profitIdx in range(0, profitLength):
                    profitNew = min(minProfit, profitIdx + profit)
                    dpNew[memberIdx -
                          menber][profitNew] += dpOld[memberIdx][profitIdx]
            dpOld = dpNew
        return sum(profitList[-1] for profitList in dpOld) % 1000000007
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 5, minProfit = 3, group = [2,2], profit = [2,3]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().profitableSchemes(5, 3, [2, 2], [2, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8])))
    print()

    pass
# @lc main=end