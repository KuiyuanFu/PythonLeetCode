# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#
# https://leetcode.com/problems/find-the-town-judge/description/
#
# algorithms
# Easy (49.43%)
# Likes:    3927
# Dislikes: 291
# Total Accepted:    307.4K
# Total Submissions: 621.8K
# Testcase Example:  '2\n[[1,2]]'
#
# In a town, there are n people labeled from 1 to n. There is a rumor that one
# of these people is secretly the town judge.
#
# If the town judge exists, then:
#
#
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
#
#
# You are given an array trust where trust[i] = [ai, bi] representing that the
# person labeled ai trusts the person labeled bi.
#
# Return the label of the town judge if the town judge exists and can be
# identified, or return -1 otherwise.
#
#
# Example 1:
#
#
# Input: n = 2, trust = [[1,2]]
# Output: 2
#
#
# Example 2:
#
#
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
#
#
# Example 3:
#
#
# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
#
#
#
# Constraints:
#
#
# 1 <= n <= 1000
# 0 <= trust.length <= 10^4
# trust[i].length == 2
# All the pairs of trust are unique.
# ai != bi
# 1 <= ai, bi <= n
#
#
#

# @lc tags=Unknown

# @lc imports=start
from enum import IntFlag
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找所有人指向其的，但不指向别人的。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        buffer = [1] * (n + 1)
        buffer[0] = -inf
        for s, d in trust:
            buffer[s] = -inf
            buffer[d] += 1
        for i, c in enumerate(buffer):
            if c == n:
                return i
        return -1

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2, trust = [[1,2]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findJudge(2, [[1, 2]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 3, trust = [[1,3],[2,3]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findJudge(3, [[1, 3], [2, 3]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 3, trust = [[1,3],[2,3],[3,1]]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]])))
    print()

    pass
# @lc main=end