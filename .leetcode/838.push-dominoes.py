# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#
# https://leetcode.com/problems/push-dominoes/description/
#
# algorithms
# Medium (52.19%)
# Likes:    1568
# Dislikes: 105
# Total Accepted:    56K
# Total Submissions: 107.3K
# Testcase Example:  '"RR.L"'
#
# There are n dominoes in a line, and we place each domino vertically upright.
# In the beginning, we simultaneously push some of the dominoes either to the
# left or to the right.
#
# After each second, each domino that is falling to the left pushes the
# adjacent domino on the left. Similarly, the dominoes falling to the right
# push their adjacent dominoes standing on the right.
#
# When a vertical domino has dominoes falling on it from both sides, it stays
# still due to the balance of the forces.
#
# For the purposes of this question, we will consider that a falling domino
# expends no additional force to a falling or already fallen domino.
#
# You are given a string dominoes representing the initial state where:
#
#
# dominoes[i] = 'L', if the i^th domino has been pushed to the left,
# dominoes[i] = 'R', if the i^th domino has been pushed to the right, and
# dominoes[i] = '.', if the i^th domino has not been pushed.
#
#
# Return a string representing the final state.
#
#
# Example 1:
#
#
# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second
# domino.
#
#
# Example 2:
#
#
# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
#
#
#
# Constraints:
#
#
# n == dominoes.length
# 1 <= n <= 10^5
# dominoes[i] is either 'L', 'R', or '.'.
#
#
#

# @lc tags=linked-list;design

# @lc imports=start
import enum
from imports import *

# @lc imports=end

# @lc idea=start
#
# 多米诺，最终状态。
# 时序。集合。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        res = [c for c in dominoes]
        l = len(res)
        ls, rs = set(), set()
        for i, c in enumerate(res):
            if c == 'L':
                ls.add(i)
            elif c == 'R':
                rs.add(i)

        while len(ls) + len(rs) > 0:

            lsn = set(i - 1 for i in ls)
            rsn = set(i + 1 for i in rs)

            same = lsn.intersection(rsn)

            ls = lsn.difference(same)
            rs = rsn.difference(same)

            for i in list(ls):
                if i >= 0 and res[i] == '.':
                    res[i] = 'L'
                else:
                    ls.remove(i)
            for i in list(rs):
                if i < l and res[i] == '.':
                    res[i] = 'R'
                else:
                    rs.remove(i)

        return ''.join(res)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('dominoes = "RR.L"')
    print('Exception :')
    print('"RR.L"')
    print('Output :')
    print(str(Solution().pushDominoes("RR.L")))
    print()

    print('Example 2:')
    print('Input : ')
    print('dominoes = ".L.R...LR..L.."')
    print('Exception :')
    print('"LL.RR.LLRRLL.."')
    print('Output :')
    print(str(Solution().pushDominoes(".L.R...LR..L..")))
    print()

    pass
# @lc main=end