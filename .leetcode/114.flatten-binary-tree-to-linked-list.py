# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (52.59%)
# Likes:    4466
# Dislikes: 412
# Total Accepted:    456.7K
# Total Submissions: 854.5K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given the root of a binary tree, flatten the tree into a "linked list":
#
#
# The "linked list" should use the same TreeNode class where the right child
# pointer points to the next node in the list and the left child pointer is
# always null.
# The "linked list" should be in the same order as a pre-order traversal of the
# binary tree.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
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
# Input: root = [0]
# Output: [0]
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
# Follow up: Can you flatten the tree in-place (with O(1) extra space)?
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
#
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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        def recur(root: TreeNode) -> TreeNode:
            left = root.left
            right = root.right
            last = root
            if left:
                root.left = None
                last = recur(left)
                last.right = right
                root.right = left
            if right:
                last = recur(right)
            return last

        recur(root)
        return root
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,5,3,4,null,6]')
    print('Output :')
    print(str(Solution().flatten(listToTreeNode([1, 2, 5, 3, 4, None, 6]))))
    print('Exception :')
    print('[1,null,2,null,3,null,4,null,5,null,6]')
    print()

    print('Example 2:')
    print('Input : ')
    print('root = []')
    print('Output :')
    print(str(Solution().flatten(listToTreeNode([]))))
    print('Exception :')
    print('[]')
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [0]')
    print('Output :')
    print(str(Solution().flatten(listToTreeNode([0]))))
    print('Exception :')
    print('[0]')
    print()

    pass
# @lc main=end