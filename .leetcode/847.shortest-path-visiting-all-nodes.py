# @lc app=leetcode id=847 lang=python3
#
# [847] Shortest Path Visiting All Nodes
#
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/description/
#
# algorithms
# Hard (60.88%)
# Likes:    2283
# Dislikes: 118
# Total Accepted:    53.3K
# Total Submissions: 87.4K
# Testcase Example:  '[[1,2,3],[0],[0],[0]]'
#
# You have an undirected, connected graph of n nodes labeled from 0 to n - 1.
# You are given an array graph where graph[i] is a list of all the nodes
# connected with node i by an edge.
#
# Return the length of the shortest path that visits every node. You may start
# and stop at any node, you may revisit nodes multiple times, and you may reuse
# edges.
#
#
# Example 1:
#
#
# Input: graph = [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]
#
#
# Example 2:
#
#
# Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]
#
#
#
# Constraints:
#
#
# n == graph.length
# 1 <= n <= 12
# 0 <= graph[i].length < n
# graph[i] does not contain i.
# If graph[a] contains b, then graph[b] contains a.
# The input graph is always connected.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 通过所有点的最短距离
# 直接暴力遍历。
# 同一起点的不同路径，不走重复的道路。
# 广度优先
# 记录 新到达点与以访问结点 为索引的信息，避免重复。
#
# @lc idea=end

# @lc group=graph

# @lc rank=10


# @lc code=start
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        step = 0
        counts = len(graph)
        target = (1 << counts) - 1
        nodes = [(i, 1 << i) for i in range(counts)]
        visited = [[False for _ in range(2**counts)] for _ in range(counts)]

        while True:
            nodesNew = []

            for node in nodes:
                src, v = node
                if v == target:
                    return step
                for des in graph[src]:
                    k = v | (1 << des)
                    # visited
                    if visited[des][k]:
                        continue
                    visited[des][k] = True
                    nodesNew.append((des, k))

            nodes = nodesNew
            step += 1


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    print(
        str(Solution().shortestPathLength([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                           [0, 2, 3, 4, 5, 6, 7, 8, 9],
                                           [0, 1, 3, 4, 5, 6, 7, 8, 9],
                                           [0, 1, 2, 4, 5, 6, 7, 8, 9],
                                           [0, 1, 2, 3, 5, 6, 7, 8, 9],
                                           [0, 1, 2, 3, 4, 6, 7, 8, 9],
                                           [0, 1, 2, 3, 4, 5, 7, 8, 9],
                                           [0, 1, 2, 3, 4, 5, 6, 8, 9],
                                           [0, 1, 2, 3, 4, 5, 6, 7, 9, 10],
                                           [0, 1, 2, 3, 4, 5, 6, 7, 8, 11],
                                           [8], [9]])))
    print(
        str(Solution().shortestPathLength([[1], [0, 2, 4], [1, 3], [2], [1, 5],
                                           [4]])))
    print()
    print('Example 1:')
    print('Input : ')
    print(
        'graph = [[7],[3],[3,9],[1,2,4,5,7,11],[3],[3],[9],[3,10,8,0],[7],[11,6,2],[7],[3,9]]'
    )
    print('Exception :')
    print('17')
    print('Output :')
    print(
        str(Solution().shortestPathLength([[7], [3], [3, 9],
                                           [1, 2, 4, 5, 7, 11], [3], [3], [9],
                                           [3, 10, 8, 0], [7], [11, 6, 2], [7],
                                           [3, 9]])))
    print()
    print('Example 1:')
    print('Input : ')
    print('graph = [[1,2,3],[0],[0],[0]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().shortestPathLength([[1, 2, 3], [0], [0], [0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(
        str(Solution().shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2],
                                           [1, 2]])))
    print()

    pass
# @lc main=end