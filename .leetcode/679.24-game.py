# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#
# https://leetcode.com/problems/24-game/description/
#
# algorithms
# Hard (47.82%)
# Likes:    1040
# Dislikes: 196
# Total Accepted:    55.4K
# Total Submissions: 115.4K
# Testcase Example:  '[4,1,8,7]'
#
# You are given an integer array cards of length 4. You have four cards, each
# containing a number in the range [1, 9]. You should arrange the numbers on
# these cards in a mathematical expression using the operators ['+', '-', '*',
# '/'] and the parentheses '(' and ')' to get the value 24.
#
# You are restricted with the following rules:
#
#
# The division operator '/' represents real division, not integer
# division.
#
#
# For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
#
#
# Every operation done is between two numbers. In particular, we cannot use '-'
# as a unary operator.
#
# For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not
# allowed.
#
#
# You cannot concatenate numbers together
#
# For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not
# valid.
#
#
#
#
# Return true if you can get such expression that evaluates to 24, and false
# otherwise.
#
#
# Example 1:
#
#
# Input: cards = [4,1,8,7]
# Output: true
# Explanation: (8-4) * (7-1) = 24
#
#
# Example 2:
#
#
# Input: cards = [1,2,1,2]
# Output: false
#
#
#
# Constraints:
#
#
# cards.length == 4
# 1 <= cards[i] <= 9
#
#
#

# @lc tags=depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二十四点。
# 递归。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        dp = {}

        def recur(cards: List[int]):
            cards.sort()
            k = tuple(cards)
            if k in dp:
                return dp[k]
            res = False
            if len(cards) == 1:
                res = abs(cards[0] - 24) < 0.0000001
            else:
                for i in range(1, len(cards)):
                    for j in range(i):
                        n1 = cards[i]
                        n2 = cards[j]
                        ct = [0] + cards[:j] + cards[j + 1:i] + cards[i + 1:]
                        ct[0] = n1 + n2
                        if recur(ct.copy()):
                            res = True
                            break
                        ct[0] = n1 - n2
                        if recur(ct.copy()):
                            res = True
                            break
                        ct[0] = n2 - n1
                        if recur(ct.copy()):
                            res = True
                            break
                        ct[0] = n1 * n2
                        if recur(ct.copy()):
                            res = True
                            break
                        if n2 != 0:
                            ct[0] = n1 / n2
                            if recur(ct.copy()):
                                res = True
                                break
                        if n1 != 0:
                            ct[0] = n2 / n1
                            if recur(ct.copy()):
                                res = True
                                break

                    if res:
                        break
            dp[k] = res
            return res

        return recur(cards)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('cards = [4,1,8,7]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().judgePoint24([4, 1, 8, 7])))
    print()

    print('Example 2:')
    print('Input : ')
    print('cards = [1,2,1,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().judgePoint24([1, 2, 1, 2])))
    print()
    print('Exception :')
    print('True')
    print(str(Solution().judgePoint24([1, 3, 4, 6])))

    print('Exception :')
    print('false')
    print(str(Solution().judgePoint24([1, 1, 7, 7])))
    print('Exception :')
    print('true')
    print(str(Solution().judgePoint24([3, 3, 8, 8])))
    pass
# @lc main=end