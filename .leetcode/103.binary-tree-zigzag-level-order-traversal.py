# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (50.57%)
# Likes:    3445
# Dislikes: 129
# Total Accepted:    512.3K
# Total Submissions: 1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the zigzag level order traversal of
# its nodes' values. (i.e., from left to right, then right to left for the next
# level and alternate between).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
#
#
#

# @lc tags=stack;tree;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二叉树，返回每层的结点，第一层从左向右，第二层从右向左，以此类推。
# 广度优先遍历。简单的每次加入时，隔一行，反转，即可。
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        resultAll = []
        currents = []
        nexts = []
        flag = False
        if root:
            nexts.append(root)
        while nexts:
            currents, nexts, resultLevel = nexts, [], []
            for n in currents:
                resultLevel.append(n.val)
                if n.left:
                    nexts.append(n.left)
                if n.right:
                    nexts.append(n.right)

            if flag:
                resultLevel = list(reversed(resultLevel))
            flag = not flag
            resultAll.append(resultLevel)

        return resultAll
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,9,20,null,null,15,7]')
    print('Output :')
    print(
        str(Solution().zigzagLevelOrder(
            listToTreeNode([3, 9, 20, None, None, 15, 7]))))
    print('Exception :')
    print('[[3],[20,9],[15,7]]')
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1]')
    print('Output :')
    print(str(Solution().zigzagLevelOrder(listToTreeNode([1]))))
    print('Exception :')
    print('[[1]]')
    print()

    print('Example 3:')
    print('Input : ')
    print('root = []')
    print('Output :')
    print(str(Solution().zigzagLevelOrder(listToTreeNode([]))))
    print('Exception :')
    print('[]')
    print()

    pass
# @lc main=end