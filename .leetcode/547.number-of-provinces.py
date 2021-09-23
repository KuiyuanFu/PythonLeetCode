# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#
# https://leetcode.com/problems/number-of-provinces/description/
#
# algorithms
# Medium (61.85%)
# Likes:    3801
# Dislikes: 207
# Total Accepted:    331.4K
# Total Submissions: 534.8K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# There are n cities. Some of them are connected, while some are not. If city a
# is connected directly with city b, and city b is connected directly with city
# c, then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other
# cities outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
# i^th city and the j^th city are directly connected, and isConnected[i][j] = 0
# otherwise.
#
# Return the total number of provinces.
#
#
# Example 1:
#
#
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
#
#
# Example 2:
#
#
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]
#
#
#

# @lc tags=depth-first-search;union-find

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定图的邻接矩阵，判断树的个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited = set()

        res = 0
        for i in range(len(isConnected)):
            if i in visited:
                continue
            res += 1
            s = [i]
            while s:
                c = s.pop()
                for idx, f in enumerate(isConnected[c]):
                    if f and idx not in visited:
                        visited.add(idx)
                        s.append(idx)

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('isConnected = [[1,1,0],[1,1,0],[0,0,1]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('isConnected = [[1,0,0],[0,1,0],[0,0,1]]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]])))
    print()

    pass
# @lc main=end