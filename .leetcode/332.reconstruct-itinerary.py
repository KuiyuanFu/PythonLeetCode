# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (38.82%)
# Likes:    3005
# Dislikes: 1360
# Total Accepted:    227.2K
# Total Submissions: 584.8K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# You are given a list of airline tickets where tickets[i] = [fromi, toi]
# represent the departure and the arrival airports of one flight. Reconstruct
# the itinerary in order and return it.
#
# All of the tickets belong to a man who departs from "JFK", thus, the
# itinerary must begin with "JFK". If there are multiple valid itineraries, you
# should return the itinerary that has the smallest lexical order when read as
# a single string.
#
#
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than
# ["JFK", "LGB"].
#
#
# You may assume all tickets form at least one valid itinerary. You must use
# all the tickets once and only once.
#
#
# Example 1:
#
#
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
#
#
# Example 2:
#
#
# Input: tickets =
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
#
#
#
# Constraints:
#
#
# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi and toi consist of uppercase English letters.
# fromi != toi
#
#
#

# @lc tags=depth-first-search;graph

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个图，从起点开始可以遍历每条边一次且仅一次，求按照字典序，最小的遍历顺序。
# 对于每个节点来说，有多个节点可以访问，那么访问哪个节点就是一个问题了。朴素的想法是，按照字典序，依次访问，但这样会遇到一个问题，即如果有一路径直接访问到了终点，那么就没有访问其他路径的机会了。
# 所以需要找到哪条路是通向终点的，判断方法就是看是否可以回到此节点。
# 首先，对于每个节点，按照字典序次序，深度优先遍历，如果能回到此节点，那么就无影响，访问下一个路径；如果回不到，就说明到了终点，回溯，遍历其他路径。
# 由于我们不知道每个节点应该访问的第一个路径，但是知道最后一个路径，所以，要倒序记录，之后再倒序输出。
#
# @lc idea=end

# @lc group=depth-first-search;graph

# @lc rank=10


# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def s2i(s):
            return (ord(s[0]) * 128 * 128 + ord(s[1]) * 128 + ord(s[2]))

        def i2s(i):

            return chr(i // 128 // 128) + chr((i // 128) % 128) + chr(i % 128)

        from collections import defaultdict, deque
        from heapq import heapify, heappop, heappush

        # 邻接链表
        ftd = defaultdict(list)
        for f, t in tickets:
            heappush(ftd[s2i(f)], s2i(t))

        # 对于每个节点，从后向前访问
        route, stack = [], [s2i('JFK')]
        while stack:
            while ftd[stack[-1]]:
                stack += heappop(ftd[stack[-1]]),
            route += i2s(stack.pop()),
        return route[::-1]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().findItinerary([["bbb", "ccc"], ["JFK", "bbb"],
                                      ["bbb", "ddd"], ["ddd", "bbb"],
                                      ["bbb", "aaa"], ["aaa", "bbb"]])))
    print('Example 1:')
    print('Input : ')
    print(
        'tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]')
    print('Exception :')
    print('["JFK","MUC","LHR","SFO","SJC"]')
    print('Output :')
    print(
        str(Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"],
                                      ["SFO", "SJC"], ["LHR", "SFO"]])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'tickets =[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]'
    )
    print('Exception :')
    print('["JFK","ATL","JFK","SFO","ATL","SFO"]')
    print('Output :')
    print(
        str(Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"],
                                      ["SFO", "ATL"], ["ATL", "JFK"],
                                      ["ATL", "SFO"]])))
    print()

    pass
# @lc main=end