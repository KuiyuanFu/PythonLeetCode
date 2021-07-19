# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#
# https://leetcode.com/problems/minimum-height-trees/description/
#
# algorithms
# Medium (35.07%)
# Likes:    3402
# Dislikes: 139
# Total Accepted:    142.3K
# Total Submissions: 402.1K
# Testcase Example:  '4\n[[1,0],[1,2],[1,3]]'
#
# A tree is an undirected graph in which any two vertices are connected by
# exactly one path. In other words, any connected graph without simple cycles
# is a tree.
#
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
# where edges[i] = [ai, bi] indicates that there is an undirected edge between
# the two nodes ai and bi in the tree, you can choose any node of the tree as
# the root. When you select a node x as the root, the result tree has height h.
# Among all possible rooted trees, those with minimum height (i.e. min(h))  are
# called minimum height trees (MHTs).
#
# Return a list of all MHTs' root labels. You can return the answer in any
# order.
#
# The height of a rooted tree is the number of edges on the longest downward
# path between the root and a leaf.
#
#
# Example 1:
#
#
# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node
# with label 1 which is the only MHT.
#
#
# Example 2:
#
#
# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]
#
#
# Example 3:
#
#
# Input: n = 1, edges = []
# Output: [0]
#
#
# Example 4:
#
#
# Input: n = 2, edges = [[0,1]]
# Output: [0,1]
#
#
#
# Constraints:
#
#
# 1 <= n <= 2 * 10^4
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# All the pairs (ai, bi) are distinct.
# The given input is guaranteed to be a tree and there will be no repeated
# edges.
#
#
#

# @lc tags=breadth-first-search;graph

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求一个树以特定结点为根时具有一个高度，求高度最小的所有情况。
# 求每个结点离其他结点最远距离，最远距离最小的就是所求结点。
# 最朴素的思想就是依次指定结点为根节点，之后计算其高度。
# 比较有效率的想法，是高度最小的树的根，一定是距离所有叶子距离最近的结点，且最多有两个，所以依次找叶子结点，之后向内收缩，直到剩下不超过两个结点。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        adjoin = {}
        for i in range(n):
            adjoin[i] = set()
        for i, j in edges:
            adjoin[i].add(j)
            adjoin[j].add(i)
        leaves = []
        for k in adjoin:
            s = adjoin[k]
            if len(s) <= 1:
                leaves.append(k)

        while len(adjoin) > 2:
            leavesNew = []
            for i in leaves:
                for j in adjoin[i]:
                    adjoin[j].remove(i)
                    if len(adjoin[j]) == 1:
                        leavesNew.append(j)
                adjoin.pop(i)
            leaves = leavesNew
        return list(adjoin)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 4, edges = [[1,0],[1,2],[1,3]]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]')
    print('Exception :')
    print('[3,4]')
    print('Output :')
    print(
        str(Solution().findMinHeightTrees(
            6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 1, edges = []')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().findMinHeightTrees(1, [])))
    print()

    print('Example 4:')
    print('Input : ')
    print('n = 2, edges = [[0,1]]')
    print('Exception :')
    print('[0,1]')
    print('Output :')
    print(str(Solution().findMinHeightTrees(2, [[0, 1]])))
    print()

    pass
# @lc main=end