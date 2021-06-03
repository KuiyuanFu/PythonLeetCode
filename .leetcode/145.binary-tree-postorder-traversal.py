# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Easy (58.69%)
# Likes:    2675
# Dislikes: 117
# Total Accepted:    497.1K
# Total Submissions: 846.1K
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the postorder traversal of its nodes'
# values.
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [3,2,1]
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: [1]
#
#
# Example 4:
#
#
# Input: root = [1,2]
# Output: [2,1]
#
#
# Example 5:
#
#
# Input: root = [1,null,2]
# Output: [2,1]
#
#
#
# Constraints:
#
#
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#

# @lc tags=stack;tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 后续遍历
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(
            root.right) + [root.val]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,null,2,3]')
    print('Exception :')
    print('[3,2,1]')
    print('Output :')
    print(str(Solution().postorderTraversal(listToTreeNode([1, None, 2, 3]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().postorderTraversal(listToTreeNode([]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().postorderTraversal(listToTreeNode([1]))))
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [1,2]')
    print('Exception :')
    print('[2,1]')
    print('Output :')
    print(str(Solution().postorderTraversal(listToTreeNode([1, 2]))))
    print()

    print('Example 5:')
    print('Input : ')
    print('root = [1,null,2]')
    print('Exception :')
    print('[2,1]')
    print('Output :')
    print(str(Solution().postorderTraversal(listToTreeNode([1, None, 2]))))
    print()

    pass
# @lc main=end