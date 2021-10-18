# @lc app=leetcode id=685 lang=python3
#
# [685] Redundant Connection II
#
# https://leetcode.com/problems/redundant-connection-ii/description/
#
# algorithms
# Hard (33.30%)
# Likes:    1357
# Dislikes: 258
# Total Accepted:    47.4K
# Total Submissions: 141.9K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# In this problem, a rooted tree is a directed graph such that, there is
# exactly one node (the root) for which all other nodes are descendants of this
# node, plus every node has exactly one parent, except for the root node which
# has no parents.
#
# The given input is a directed graph that started as a rooted tree with n
# nodes (with distinct values from 1 to n), with one additional directed edge
# added. The added edge has two different vertices chosen from 1 to n, and was
# not an edge that already existed.
#
# The resulting graph is given as a 2D-array of edges. Each element of edges is
# a pair [ui, vi] that represents a directed edge connecting nodes ui and vi,
# where ui is a parent of child vi.
#
# Return an edge that can be removed so that the resulting graph is a rooted
# tree of n nodes. If there are multiple answers, return the answer that occurs
# last in the given 2D-array.
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
# Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
# Output: [4,1]
#
#
#
# Constraints:
#
#
# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
#
#
#

# @lc tags=tree;depth-first-search;union-find;graph

# @lc imports=start
from re import T
from imports import *

# @lc imports=end

# @lc idea=start
#
# 有向的树。找多出的一个边，使其变成有向树。
# 判断是否有环，以及是否有两个父节点。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findRedundantDirectedConnection(self,
                                        edges: List[List[int]]) -> List[int]:
        fs = [None for _ in range(1, len(edges) + 1)]
        s, b, t = None, None, None
        for l, r in edges:
            if fs[r - 1] is not None:
                s, b, t = fs[r - 1], l - 1, r - 1
            fs[r - 1] = l - 1
        # double father
        if s is not None:
            st = s
            f = False
            while st is not None:
                if st == t:
                    f = True
                    break
                else:
                    st = fs[st]
            if f:
                return [s + 1, t + 1]
            else:
                return [b + 1, t + 1]
        else:
            idx = [None for i in range(1, len(edges) + 1)]
            for i, (l, r) in enumerate(edges):
                idx[r - 1] = i
            visited = set()
            for i in range(len(edges)):
                if i in visited:
                    continue
                cir = set()
                f = False
                while True:
                    if i in cir:
                        f = True
                        break
                    if i in visited:
                        break
                    visited.add(i)
                    cir.add(i)
                    i = fs[i]
                if f:
                    res = [fs[i], i]
                    m = idx[i]
                    t = i
                    i = fs[i]
                    while i != t:
                        mt = idx[i]
                        if mt > m:
                            res = [fs[i], i]
                            m = mt
                        i = fs[i]
                    return [res[0] + 1, res[1] + 1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('edges = [[2,3],[3,1],[3,4],[4,2]]')
    print('Exception :')
    print('[4,2]')
    print('Output :')
    print(
        str(Solution().findRedundantDirectedConnection([[2, 3], [3, 1], [3, 4],
                                                        [4, 2]])))
    print()
    print('Example 1:')
    print('Input : ')
    print('edges = [[1,2],[1,3],[2,3]]')
    print('Exception :')
    print('[2,3]')
    print('Output :')
    print(
        str(Solution().findRedundantDirectedConnection([[1, 2], [1, 3], [2,
                                                                         3]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]')
    print('Exception :')
    print('[4,1]')
    print('Output :')
    print(
        str(Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4],
                                                        [4, 1], [1, 5]])))
    print()
    print('Input : ')
    print('edges = [[2,1],[3,1],[4,2],[1,4]]')
    print('Exception :')
    print('[2,1]')
    print('Output :')
    print(
        str(Solution().findRedundantDirectedConnection([[2, 1], [3, 1], [4, 2],
                                                        [1, 4]])))
    print()

    pass
# @lc main=end