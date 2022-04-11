# @lc app=leetcode id=882 lang=python3
#
# [882] Reachable Nodes In Subdivided Graph
#
# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/description/
#
# algorithms
# Hard (49.89%)
# Likes:    514
# Dislikes: 198
# Total Accepted:    20.1K
# Total Submissions: 40.2K
# Testcase Example:  '[[0,1,10],[0,2,1],[1,2,2]]\n6\n3'
#
# You are given an undirected graph (the "original graph") with n nodes labeled
# from 0 to n - 1. You decide to subdivide each edge in the graph into a chain
# of nodes, with the number of new nodes varying between each edge.
#
# The graph is given as a 2D array of edges where edges[i] = [ui, vi, cnti]
# indicates that there is an edge between nodes ui and vi in the original
# graph, and cnti is the total number of new nodes that you will subdivide the
# edge into. Note that cnti == 0 means you will not subdivide the edge.
#
# To subdivide the edge [ui, vi], replace it with (cnti + 1) new edges and cnti
# new nodes. The new nodes are x1, x2, ..., xcnti, and the new edges are [ui,
# x1], [x1, x2], [x2, x3], ..., [xcnti-1, xcnti], [xcnti, vi].
#
# In this new graph, you want to know how many nodes are reachable from the
# node 0, where a node is reachable if the distance is maxMoves or less.
#
# Given the original graph and maxMoves, return the number of nodes that are
# reachable from node 0 in the new graph.
#
#
# Example 1:
#
#
# Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
# Output: 13
# Explanation: The edge subdivisions are shown in the image above.
# The nodes that are reachable are highlighted in yellow.
#
#
# Example 2:
#
#
# Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
# Output: 23
#
#
# Example 3:
#
#
# Input: edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n =
# 5
# Output: 1
# Explanation: Node 0 is disconnected from the rest of the graph, so only node
# 0 is reachable.
#
#
#
# Constraints:
#
#
# 0 <= edges.length <= min(n * (n - 1) / 2, 10^4)
# edges[i].length == 3
# 0 <= ui < vi < n
# There are no multiple edges in the graph.
# 0 <= cnti <= 10^4
# 0 <= maxMoves <= 10^9
# 1 <= n <= 3000
#
#
#

# @lc tags=binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一个无向图中，所有边长n大于1的，增加n个结点，成一个链。
# 求从0结点开始，距离在 maxMoves 中的结点数量。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int,
                       n: int) -> int:

        adjs = [{} for _ in range(n)]
        for l, r, c in edges:
            adjs[l][r] = c
            adjs[r][l] = c
        res = 0

        nodes = [(0, 0)]
        visited = set()

        while nodes:
            dis, node = heappop(nodes)

            if node in visited:
                continue

            visited.add(node)
            res += 1

            for pair in adjs[node].items():
                adj, c = pair

                if dis + c + 1 <= maxMoves:
                    res += c
                    heappush(nodes, (dis + c + 1, adj))
                    adjs[adj][node] = 0
                else:
                    res += maxMoves - dis
                    adjs[adj][node] -= maxMoves - dis

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3')
    print('Exception :')
    print('13')
    print('Output :')
    print(
        str(Solution().reachableNodes([[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6,
                                      3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4')
    print('Exception :')
    print('23')
    print('Output :')
    print(
        str(Solution().reachableNodes(
            [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], 10, 4)))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n =5'
    )
    print('Exception :')
    print('1')
    print('Output :')
    print(
        str(Solution().reachableNodes(
            [[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]], 17, 5)))
    print()

    pass
# @lc main=end