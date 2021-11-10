# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#
# https://leetcode.com/problems/network-delay-time/description/
#
# algorithms
# Medium (46.64%)
# Likes:    3313
# Dislikes: 263
# Total Accepted:    189.2K
# Total Submissions: 401.6K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
# You are given a network of n nodes, labeled from 1 to n. You are also given
# times, a list of travel times as directed edges times[i] = (ui, vi, wi),
# where ui is the source node, vi is the target node, and wi is the time it
# takes for a signal to travel from source to target.
#
# We will send a signal from a given node k. Return the time it takes for all
# the n nodes to receive the signal. If it is impossible for all the n nodes to
# receive the signal, return -1.
#
#
# Example 1:
#
#
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
#
#
# Example 2:
#
#
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
#
#
# Example 3:
#
#
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
#
#
#
# Constraints:
#
#
# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 从一点传输到全网的延迟。
# 图。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ns = [[] for _ in range(n + 1)]
        for u, v, w in times:
            ns[u].append((v, w))

        visited = set()
        heap = [(0, k)]
        res = 0
        while heap:
            w, v = heappop(heap)
            if v in visited:
                continue
            res = w
            visited.add(v)
            for u, wa in ns[v]:
                heappush(heap, (w + wa, u))
        if len(visited) < n:
            return -1

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4,
                                        2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('times = [[1,2,1]], n = 2, k = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().networkDelayTime([[1, 2, 1]], 2, 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('times = [[1,2,1]], n = 2, k = 2')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().networkDelayTime([[1, 2, 1]], 2, 2)))
    print()
    print(
        str(Solution().networkDelayTime(
            [[1, 5, 66], [3, 5, 55], [4, 3, 29], [1, 2, 9], [3, 4, 10],
             [3, 1, 3], [2, 3, 78], [1, 4, 98], [4, 5, 21], [5, 2, 19],
             [5, 1, 76], [4, 1, 65], [3, 2, 27], [5, 3, 23], [5, 4, 12],
             [2, 1, 36], [4, 2, 75], [2, 4, 11], [1, 3, 30], [2, 5, 8]], 5,
            1)))
    pass
# @lc main=end