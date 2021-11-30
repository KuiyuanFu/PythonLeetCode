# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#
# https://leetcode.com/problems/is-graph-bipartite/description/
#
# algorithms
# Medium (49.37%)
# Likes:    3456
# Dislikes: 249
# Total Accepted:    243.3K
# Total Submissions: 490.1K
# Testcase Example:  '[[1,2,3],[0,2],[0,1,3],[0,2]]'
#
# There is an undirected graph with n nodes, where each node is numbered
# between 0 and n - 1. You are given a 2D array graph, where graph[u] is an
# array of nodes that node u is adjacent to. More formally, for each v in
# graph[u], there is an undirected edge between node u and node v. The graph
# has the following properties:
#
#
# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such
# that there is no path between them.
#
#
# A graph is bipartite if the nodes can be partitioned into two independent
# sets A and B such that every edge in the graph connects a node in set A and a
# node in set B.
#
# Return true if and only if it is bipartite.
#
#
# Example 1:
#
#
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets
# such that every edge connects a node in one and a node in the other.
#
# Example 2:
#
#
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
#
#
# Constraints:
#
#
# graph.length == n
# 1 <= n <= 100
# 0 <= graph[u].length < n
# 0 <= graph[u][i] <= n - 1
# graph[u] does not contain u.
# All the values of graph[u] are unique.
# If graph[u] contains v, then graph[v] contains u.
#
#
#

# @lc tags=string;stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断一个图是否可以二分，即将点分成两集合，每条边的两个结点处在不同的集合中。
# 对每一个连通部分分别判断。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        length = len(graph)
        needToVisited = set(range(length))
        while len(needToVisited) > 0:
            thisTree = []
            s = set()
            while len(needToVisited) > 0:
                i = needToVisited.pop()
                if len(graph[i]) > 0:
                    thisTree.append(i)
                    s.add(i)
                    break
            while len(thisTree) > 0:
                i = thisTree.pop()
                f = i in s
                for j in graph[i]:

                    # new node
                    if j in needToVisited:
                        needToVisited.remove(j)
                        thisTree.append(j)
                        if not f:
                            s.add(j)
                    # the same set
                    elif f == (j in s):
                        return False

        return True

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('graph = [[1,2,3],[0,2],[0,1,3],[0,2]]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('graph = [[1,3],[0,2],[1,3],[0,2]]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]])))
    print()

    pass
# @lc main=end