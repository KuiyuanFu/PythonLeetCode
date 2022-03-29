# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/
#
# algorithms
# Medium (67.72%)
# Likes:    1880
# Dislikes: 322
# Total Accepted:    100.4K
# Total Submissions: 148.2K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]'
#
# Given the root of a binary tree, the depth of each node is the shortest
# distance to the root.
#
# Return the smallest subtree such that it contains all the deepest nodes in
# the original tree.
#
# A node is called the deepest if it has the largest depth possible among any
# node in the entire tree.
#
# The subtree of a node is a tree consisting of that node, plus the set of all
# descendants of that node.
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the
# diagram.
# The nodes coloured in blue are the deepest nodes of the tree.
# Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2
# is the smallest subtree among them, so we return it.
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [1]
# Explanation: The root is the deepest node in the tree.
#
#
# Example 3:
#
#
# Input: root = [0,1,3,null,2]
# Output: [2]
# Explanation: The deepest node in the tree is 2, the valid subtrees are the
# subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree will be in the range [1, 500].
# 0 <= Node.val <= 500
# The values of the nodes in the tree are unique.
#
#
#
# Note: This question is the same as 1123:
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
#
#

# @lc tags=depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求具有原树中深度最高的所有结点的最小子树。
# 求最深叶子结点后，反向，依层次找父节点，直到父节点为同一个结点.
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        maxLength = 0
        maxNodes = []

        nodes = [(root, 0)]
        fatherMap = {}
        while nodes:
            node, d = nodes.pop()
            if d > maxLength:
                maxLength = d
                maxNodes.clear()
            if d == maxLength:
                maxNodes.append(node)
            if node.left:
                nodes.append((node.left, d + 1))
                fatherMap[node.left] = node
            if node.right:
                nodes.append((node.right, d + 1))
                fatherMap[node.right] = node

        maxNodes = set(maxNodes)
        while len(maxNodes) > 1:
            maxNodesN = set()
            for node in maxNodes:
                maxNodesN.add(fatherMap[node])
            maxNodes = maxNodesN

        return list(maxNodes)[0]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,5,1,6,2,0,8,null,null,7,4]')
    print('Exception :')
    print('[2,7,4]')
    print('Output :')
    print(
        str(Solution().subtreeWithAllDeepest(
            listToTreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().subtreeWithAllDeepest(listToTreeNode([1]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [0,1,3,null,2]')
    print('Exception :')
    print('[2]')
    print('Output :')
    print(
        str(Solution().subtreeWithAllDeepest(listToTreeNode([0, 1, 3, None,
                                                             2]))))
    print()

    pass
# @lc main=end