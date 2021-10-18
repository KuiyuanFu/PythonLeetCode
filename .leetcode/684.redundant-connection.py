# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#
# https://leetcode.com/problems/redundant-connection/description/
#
# algorithms
# Medium (60.21%)
# Likes:    2960
# Dislikes: 274
# Total Accepted:    170.1K
# Total Submissions: 281.6K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# In this problem, a tree is an undirected graph that is connected and has no
# cycles.
#
# You are given a graph that started as a tree with n nodes labeled from 1 to
# n, with one additional edge added. The added edge has two different vertices
# chosen from 1 to n, and was not an edge that already existed. The graph is
# represented as an array edges of length n where edges[i] = [ai, bi] indicates
# that there is an edge between nodes ai and bi in the graph.
#
# Return an edge that can be removed so that the resulting graph is a tree of n
# nodes. If there are multiple answers, return the answer that occurs last in
# the input.
#
#
# Example 1:
#
#
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
#
#
# Example 2:
#
#
# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
#
#
#
# Constraints:
#
#
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.
#
#
#

# @lc tags=tree;union-find;graph

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找形成环的边。
# 分组合并。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        vtos = [[i] for i in range(1, len(edges) + 1)]

        for l, r in edges:
            ls, rs = vtos[l - 1], vtos[r - 1]
            if ls == rs:
                return [l, r]
            if rs < ls:
                ls, rs = rs, ls
            for lss in ls:
                rs.append(lss)
                vtos[lss - 1] = rs

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('edges = [[1,2],[1,3],[2,3]]')
    print('Exception :')
    print('[2,3]')
    print('Output :')
    print(str(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]')
    print('Exception :')
    print('[1,4]')
    print('Output :')
    print(
        str(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4],
                                                [1, 5]])))
    print()

    pass
# @lc main=end