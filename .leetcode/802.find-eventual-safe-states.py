# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#
# https://leetcode.com/problems/find-eventual-safe-states/description/
#
# algorithms
# Medium (50.91%)
# Likes:    1627
# Dislikes: 295
# Total Accepted:    65.9K
# Total Submissions: 128.2K
# Testcase Example:  '[[1,2],[2,3],[5],[0],[5],[],[]]'
#
# There is a directed graph of n nodes with each node labeled from 0 to n - 1.
# The graph is represented by a 0-indexed 2D integer array graph where graph[i]
# is an integer array of nodes adjacent to node i, meaning there is an edge
# from node i to each node in graph[i].
#
# A node is a terminal node if there are no outgoing edges. A node is a safe
# node if every possible path starting from that node leads to a terminal
# node.
#
# Return an array containing all the safe nodes of the graph. The answer should
# be sorted in ascending order.
#
#
# Example 1:
#
#
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above.
# Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either
# of them.
# Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
#
# Example 2:
#
#
# Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# Output: [4]
# Explanation:
# Only node 4 is a terminal node, and every path starting at node 4 leads to
# node 4.
#
#
#
# Constraints:
#
#
# n == graph.length
# 1 <= n <= 10^4
# 0 <= graph[i].length <= n
# 0 <= graph[i][j] <= n - 1
# graph[i] is sorted in a strictly increasing order.
# The graph may contain self-loops.
# The number of edges in the graph will be in the range [1, 4 * 10^4].
#
#
#

# @lc tags=binary-search;heap

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定有向图，找从其出发所有路径都有终点的结点。
# 反向遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # out degree,priority queue
        ods = [len(ls) for ls in graph]
        h = [(od, nodeIdx) for nodeIdx, od in enumerate(ods)]
        heapify(h)
        # reversed graph
        rg = [[] for _ in range(len(graph))]
        for nodeIdx, ls in enumerate(graph):
            for oIdx in ls:
                rg[oIdx].append(nodeIdx)

        res = []
        #
        while h and h[0][0] == 0:
            nodeIdx = heappop(h)[1]
            res.append(nodeIdx)

            for inIdx in rg[nodeIdx]:
                ods[inIdx] -= 1
                heappush(h, (ods[inIdx], inIdx))
        res.sort()
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('graph = [[1,2],[2,3],[5],[0],[5],[],[]]')
    print('Exception :')
    print('[2,4,5,6]')
    print('Output :')
    print(
        str(Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [],
                                          []])))
    print()

    print('Example 2:')
    print('Input : ')
    print('graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]')
    print('Exception :')
    print('[4]')
    print('Output :')
    print(
        str(Solution().eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4],
                                          []])))
    print()

    pass
# @lc main=end