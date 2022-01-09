# @lc app=leetcode id=808 lang=python3
#
# [808] Soup Servings
#
# https://leetcode.com/problems/soup-servings/description/
#
# algorithms
# Medium (41.67%)
# Likes:    233
# Dislikes: 707
# Total Accepted:    13.8K
# Total Submissions: 33K
# Testcase Example:  '50'
#
# There are two types of soup: type A and type B. Initially, we have n ml of
# each type of soup. There are four kinds of operations:
#
#
# Serve 100 ml of soup A and 0 ml of soup B,
# Serve 75 ml of soup A and 25 ml of soup B,
# Serve 50 ml of soup A and 50 ml of soup B, and
# Serve 25 ml of soup A and 75 ml of soup B.
#
#
# When we serve some soup, we give it to someone, and we no longer have it.
# Each turn, we will choose from the four operations with an equal probability
# 0.25. If the remaining volume of soup is not enough to complete the
# operation, we will serve as much as possible. We stop once we no longer have
# some quantity of both types of soup.
#
# Note that we do not have an operation where all 100 ml's of soup B are used
# first.
#
# Return the probability that soup A will be empty first, plus half the
# probability that A and B become empty at the same time. Answers within 10^-5
# of the actual answer will be accepted.
#
#
# Example 1:
#
#
# Input: n = 50
# Output: 0.62500
# Explanation: If we choose the first two operations, A will become empty
# first.
# For the third operation, A and B will become empty at the same time.
# For the fourth operation, B will become empty first.
# So the total probability of A becoming empty first plus half the probability
# that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) =
# 0.625.
#
#
# Example 2:
#
#
# Input: n = 100
# Output: 0.71875
#
#
#
# Constraints:
#
#
# 0 <= n <= 10^9
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 两碗汤，有给定的方式，求先空的概率。
# 纯数学。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def soupServings(self, n: int) -> float:
        if n == 0:
            return 0.5
        if n > 4000:
            return 1
        n = (n + 24) // 25
        dp = [[0 for _ in range(n)] for _ in range(n)]
        chooses = [[4, 0], [3, 1], [2, 2], [1, 3]]
        for i in range(n):
            for j in range(n):
                r = 0
                for oi, oj in chooses:
                    ni, nj = i - oi, j - oj
                    f1, f2 = ni < 0, nj < 0
                    if f1 and f2:
                        r += 0.5
                    elif f1:
                        r += 1
                    elif f2:
                        pass
                    else:
                        r += dp[ni][nj]
                r /= 4
                dp[i][j] = r
        return dp[-1][-1]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    for i in range(1, 10000000):
        r = Solution().soupServings(i)
        print((i, r))
        if r > 0.99995:
            break
    print('Example 1:')
    print('Input : ')
    print('n = 50')
    print('Exception :')
    print('0.62500')
    print('Output :')
    print(str(Solution().soupServings(50)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 100')
    print('Exception :')
    print('0.71875')
    print('Output :')
    print(str(Solution().soupServings(100)))
    print()

    pass
# @lc main=end