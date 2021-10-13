# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (43.05%)
# Likes:    988
# Dislikes: 1285
# Total Accepted:    117.7K
# Total Submissions: 272.7K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# Given a non-empty special binary tree consisting of nodes with the
# non-negative value, where each node in this tree has exactly two or zero
# sub-node. If the node has two sub-nodes, then this node's value is the
# smaller value among its two sub-nodes. More formally, the property root.val =
# min(root.left.val, root.right.val) always holds.
#
# Given such a binary tree, you need to output the second minimum value in the
# set made of all the nodes' value in the whole tree.
#
# If no such second minimum value exists, output -1 instead.
#
#
#
#
# Example 1:
#
#
# Input: root = [2,2,5,null,null,5,7]
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
#
#
# Example 2:
#
#
# Input: root = [2,2,2]
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest
# value.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 25].
# 1 <= Node.val <= 2^31 - 1
# root.val == min(root.left.val, root.right.val) for each internal node of the
# tree.
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 二叉树，每一个节点的值为子节点的最小值。 求第二小的值。
# 如果分支的节点的值大于了根节点值，其子节点一定不可能是第二小的值。
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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        v = root.val
        res = None
        q = [root]
        while q:
            p = q.pop()
            if p.val > v:
                if not res:
                    res = p.val
                else:
                    res = min(res, p.val)
            else:
                if p.left:
                    q.append(p.left)
                    q.append(p.right)
        return res if res else -1

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [2,2,5,null,null,5,7]')
    print('Exception :')
    print('5')
    print('Output :')
    print(
        str(Solution().findSecondMinimumValue(
            listToTreeNode([2, 2, 5, None, None, 5, 7]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [2,2,2]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().findSecondMinimumValue(listToTreeNode([2, 2, 2]))))
    print()

    pass
# @lc main=end