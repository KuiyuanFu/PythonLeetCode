# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
# https://leetcode.com/problems/clone-graph/description/
#
# algorithms
# Medium (40.59%)
# Likes:    3134
# Dislikes: 1731
# Total Accepted:    477.8K
# Total Submissions: 1.2M
# Testcase Example:  '[[2,4],[1,3],[2,4],[1,3]]'
#
# Given a reference of a node in a connected undirected graph.
#
# Return a deep copy (clone) of the graph.
#
# Each node in the graph contains a value (int) and a list (List[Node]) of its
# neighbors.
#
#
# class Node {
# ⁠   public int val;
# ⁠   public List<Node> neighbors;
# }
#
#
#
#
# Test case format:
#
# For simplicity, each node's value is the same as the node's index
# (1-indexed). For example, the first node with val == 1, the second node with
# val == 2, and so on. The graph is represented in the test case using an
# adjacency list.
#
# An adjacency list is a collection of unordered lists used to represent a
# finite graph. Each list describes the set of neighbors of a node in the
# graph.
#
# The given node will always be the first node with val = 1. You must return
# the copy of the given node as a reference to the cloned graph.
#
#
# Example 1:
#
#
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val =
# 3).
#
#
# Example 2:
#
#
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists
# of only one node with val = 1 and it does not have any neighbors.
#
#
# Example 3:
#
#
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.
#
#
# Example 4:
#
#
# Input: adjList = [[2],[1]]
# Output: [[2],[1]]
#
#
#
# Constraints:
#
#
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no repeated edges and no self-loops in the graph.
# The Graph is connected and all nodes can be visited starting from the given
# node.
#
#
#

# @lc tags=depth-first-search;breadth-first-search;graph

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定一个连通无向图的结点。
# 得到图的深拷贝。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def generateNode(self, node: 'Node'):
        nodeNew = Node(node.val)
        self.mem[node.val] = nodeNew
        for n in node.neighbors:
            if n.val not in self.mem:
                neighbor = self.generateNode(n)
            else:
                neighbor = self.mem[n.val]
            nodeNew.neighbors.append(neighbor)
        return nodeNew

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        self.mem = {}
        nodeN = self.generateNode(node)
        return nodeN
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    nodes = [Node(i) for i in range(10)]

    for i in range(1, 10):
        nodes[i].neighbors.append(nodes[i - 1])
        nodes[0].neighbors.append(nodes[i])

        nodes = [Node(i) for i in range(10)]

    node1 = Node(1)
    node2 = Node(2)
    node1.neighbors.append(node2)
    node2.neighbors.append(node1)
    print(str(Solution().cloneGraph(node1)))
# @lc main=end