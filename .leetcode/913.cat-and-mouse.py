# @lc app=leetcode id=913 lang=python3
#
# [913] Cat and Mouse
#
# https://leetcode.com/problems/cat-and-mouse/description/
#
# algorithms
# Hard (35.76%)
# Likes:    626
# Dislikes: 111
# Total Accepted:    14.8K
# Total Submissions: 41.5K
# Testcase Example:  '[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]'
#
# A game on an undirected graph is played by two players, Mouse and Cat, who
# alternate turns.
#
# The graph is given as follows: graph[a] is a list of all nodes b such that ab
# is an edge of the graph.
#
# The mouse starts at node 1 and goes first, the cat starts at node 2 and goes
# second, and there is a hole at node 0.
#
# During each player's turn, they must travel along one edge of the graph that
# meets where they are.  For example, if the Mouse is at node 1, it must travel
# to any node in graph[1].
#
# Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)
#
# Then, the game can end in three ways:
#
#
# If ever the Cat occupies the same node as the Mouse, the Cat wins.
# If ever the Mouse reaches the Hole, the Mouse wins.
# If ever a position is repeated (i.e., the players are in the same position as
# a previous turn, and it is the same player's turn to move), the game is a
# draw.
#
#
# Given a graph, and assuming both players play optimally, return
#
#
# 1 if the mouse wins the game,
# 2 if the cat wins the game, or
# 0 if the game is a draw.
#
#
#
# Example 1:
#
#
# Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
# Output: 0
#
#
# Example 2:
#
#
# Input: graph = [[1,3],[0],[3],[0,2]]
# Output: 1
#
#
#
# Constraints:
#
#
# 3 <= graph.length <= 50
# 1 <= graph[i].length < graph.length
# 0 <= graph[i][j] < graph.length
# graph[i][j] != i
# graph[i] is unique.
# The mouse and the cat can always move.
#
#
#

# @lc tags=random

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 猫捉老鼠。
# 染色
#
# @lc idea=end

# @lc group=

# @lc rank=10


# @lc code=start
class Solution:

    def catMouseGame(self, mouseGraph):
        mouseWin, catWin, draw = 0, 1, 2
        mouse, cat = 0, 1
        length = len(mouseGraph)

        catGraph = [mouseGraph[i].copy() for i in range(length)]
        for idx in catGraph[0]:
            catGraph[idx].remove(0)
        catGraph[0] = []
        graphs = [mouseGraph, catGraph]

        degrees = [list(map(len, mouseGraph)), list(map(len, catGraph))]

        degrees = [[l.copy() for _ in range(length)] for l in degrees]

        dp = [[[draw for _ in range(length)] for _ in range(length)]
              for _ in range(2)]

        q = []

        for i in range(1, length):
            dp[mouse][0][i] = mouseWin
            q.append((mouse, 0, i, mouseWin))
            dp[mouse][i][i] = catWin
            q.append((mouse, i, i, catWin))
            dp[cat][i][0] = mouseWin
            q.append((cat, i, 0, mouseWin))
            dp[cat][i][i] = catWin
            q.append((cat, i, i, catWin))
        while q:
            role, roleIdx, peerIdx, win = q.pop()
            peer = 1 - role
            if peer == win:
                for peerIdxPre in graphs[peer][peerIdx]:
                    if dp[peer][peerIdxPre][roleIdx] == draw:
                        dp[peer][peerIdxPre][roleIdx] = win
                        q.append((peer, peerIdxPre, roleIdx, win))
            else:
                for peerIdxPre in graphs[peer][peerIdx]:
                    if dp[peer][peerIdxPre][roleIdx] == draw:
                        degrees[peer][roleIdx][peerIdxPre] -= 1
                        if degrees[peer][roleIdx][peerIdxPre] == 0:
                            dp[peer][peerIdxPre][roleIdx] = win
                            q.append((peer, peerIdxPre, roleIdx, win))

        return (dp[mouse][1][2] + 1) % 3


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('graph = [[5,6],[3,4],[6],[1,4,5],[1,3,5],[0,3,4,6],[0,2,5]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().catMouseGame([[5, 6], [3, 4], [6], [1, 4, 5], [1, 3, 5],
                                     [0, 3, 4, 6], [0, 2, 5]])))
    print()
    print('Example 1:')
    print('Input : ')
    print('graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(
        str(Solution().catMouseGame([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3],
                                     [0, 2, 3]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('graph = [[1,3],[0],[3],[0,2]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().catMouseGame([[1, 3], [0], [3], [0, 2]])))
    print()

    pass
# @lc main=end