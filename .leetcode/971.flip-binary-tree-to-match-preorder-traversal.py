# @lc app=leetcode id=971 lang=python3
#
# [971] Flip Binary Tree To Match Preorder Traversal
#
# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/description/
#
# algorithms
# Medium (49.90%)
# Likes:    777
# Dislikes: 247
# Total Accepted:    36.7K
# Total Submissions: 73.6K
# Testcase Example:  '[1,2]\n[2,1]'
#
# You are given the root of a binary tree with n nodes, where each node is
# uniquely assigned a value from 1 to n. You are also given a sequence of n
# values voyage, which is the desired pre-order traversal of the binary tree.
#
# Any node in the binary tree can be flipped by swapping its left and right
# subtrees. For example, flipping node 1 will have the following effect:
#
# Flip the smallest number of nodes so that the pre-order traversal of the tree
# matches voyage.
#
# Return a list of the values of all flipped nodes. You may return the answer
# in any order. If it is impossible to flip the nodes in the tree to make the
# pre-order traversal match voyage, return the list [-1].
#
#
# Example 1:
#
#
# Input: root = [1,2], voyage = [2,1]
# Output: [-1]
# Explanation: It is impossible to flip the nodes such that the pre-order
# traversal matches voyage.
#
#
# Example 2:
#
#
# Input: root = [1,2,3], voyage = [1,3,2]
# Output: [1]
# Explanation: Flipping node 1 swaps nodes 2 and 3, so the pre-order traversal
# matches voyage.
#
# Example 3:
#
#
# Input: root = [1,2,3], voyage = [1,2,3]
# Output: []
# Explanation: The tree's pre-order traversal already matches voyage, so no
# nodes need to be flipped.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is n.
# n == voyage.length
# 1 <= n <= 100
# 1 <= Node.val, voyage[i] <= n
# All the values in the tree are unique.
# All the values in voyage are unique.
#
#
#

# @lc tags=depth-first-search;breadth-first-search

# @lc imports=start
import re
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定二叉树，可以交换左右子节点，是前序遍历结果与给定顺序一致，求交换左右子节点的节点的值的列表。
# 直接遍历。只有右节点为下一个访问的节点，且左节点也不为空时才交换。
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

    def flipMatchVoyage(self, root: Optional[TreeNode],
                        voyage: List[int]) -> List[int]:

        res = []
        q = [root]
        for now, next in pairwise(voyage):
            p = q.pop()
            if p.val != now:
                return [-1]
            if p.right and p.left and p.right.val == next:
                p.left, p.right = p.right, p.left
                res.append(p.val)

            if p.right:
                q.append(p.right)
            if p.left:
                q.append(p.left)
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2], voyage = [2,1]')
    print('Exception :')
    print('[-1]')
    print('Output :')
    print(str(Solution().flipMatchVoyage(listToTreeNode([1, 2]), [2, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,3], voyage = [1,3,2]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().flipMatchVoyage(listToTreeNode([1, 2, 3]),
                                         [1, 3, 2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1,2,3], voyage = [1,2,3]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().flipMatchVoyage(listToTreeNode([1, 2, 3]),
                                         [1, 2, 3])))
    print()

    pass
# @lc main=end