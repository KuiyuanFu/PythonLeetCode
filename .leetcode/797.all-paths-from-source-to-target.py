# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (79.22%)
# Likes:    3294
# Dislikes: 107
# Total Accepted:    218K
# Total Submissions: 271.1K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find
# all possible paths from node 0 to node n - 1 and return them in any order.
#
# The graph is given as follows: graph[i] is a list of all nodes you can visit
# from node i (i.e., there is a directed edge from node i to node
# graph[i][j]).
#
#
# Example 1:
#
#
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
#
#
# Example 2:
#
#
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
#
#
# Example 3:
#
#
# Input: graph = [[1],[]]
# Output: [[0,1]]
#
#
# Example 4:
#
#
# Input: graph = [[1,2,3],[2],[3],[]]
# Output: [[0,1,2,3],[0,2,3],[0,3]]
#
#
# Example 5:
#
#
# Input: graph = [[1,3],[2],[3],[]]
# Output: [[0,1,2,3],[0,3]]
#
#
#
# Constraints:
#
#
# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i (i.e., there will be no self-loops).
# All the elements of graph[i] are unique.
# The input graph is guaranteed to be a DAG.
#
#
#

# @lc tags=hash-table;math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 有向无环图，找两点的所有路径。
# 排序。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)

        # in-degree
        inDegree = defaultdict(int)
        for l in graph:
            for o in l:
                inDegree[o] += 1
        # priority queue
        h = [(inDegree[i], i) for i in range(n)]
        heapify(h)

        # record path
        path = [[[i]] for i in range(n)]
        # traverse
        while h[0][1] != n - 1:
            s = heappop(h)[1]
            ds = graph[s]
            for d in ds:
                id = inDegree[d] - 1
                inDegree[d] = id
                heappush(h, (id, d))
                for p in path[s]:
                    if p[0] == 0:
                        path[d].append(p + [d])
        path[n - 1].pop(0)
        return path[n - 1]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('graph = [[1,2],[3],[3],[]]')
    print('Exception :')
    print('[[0,1,3],[0,2,3]]')
    print('Output :')
    print(str(Solution().allPathsSourceTarget([[1, 2], [3], [3], []])))
    print()

    print('Example 2:')
    print('Input : ')
    print('graph = [[4,3,1],[3,2,4],[3],[4],[]]')
    print('Exception :')
    print('[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]')
    print('Output :')
    print(
        str(Solution().allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4],
                                             []])))
    print()

    print('Example 3:')
    print('Input : ')
    print('graph = [[1],[]]')
    print('Exception :')
    print('[[0,1]]')
    print('Output :')
    print(str(Solution().allPathsSourceTarget([[1], []])))
    print()

    print('Example 4:')
    print('Input : ')
    print('graph = [[1,2,3],[2],[3],[]]')
    print('Exception :')
    print('[[0,1,2,3],[0,2,3],[0,3]]')
    print('Output :')
    print(str(Solution().allPathsSourceTarget([[1, 2, 3], [2], [3], []])))
    print()

    print('Example 5:')
    print('Input : ')
    print('graph = [[1,3],[2],[3],[]]')
    print('Exception :')
    print('[[0,1,2,3],[0,3]]')
    print('Output :')
    print(str(Solution().allPathsSourceTarget([[1, 3], [2], [3], []])))
    print()

    pass
# @lc main=end