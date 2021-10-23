# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
#
# algorithms
# Easy (73.92%)
# Likes:    1965
# Dislikes: 137
# Total Accepted:    339.5K
# Total Submissions: 457.2K
# Testcase Example:  '[4,2,7,1,3]\n2'
#
# You are given the root of a binary search tree (BST) and an integer val.
#
# Find the node in the BST that the node's value equals val and return the
# subtree rooted with that node. If such a node does not exist, return null.
#
#
# Example 1:
#
#
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
#
#
# Example 2:
#
#
# Input: root = [4,2,7,1,3], val = 5
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 10^7
# root is a binary search tree.
# 1 <= val <= 10^7
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 搜索二叉树。
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
    def searchBST(self, root: Optional[TreeNode],
                  val: int) -> Optional[TreeNode]:
        p = root
        while p:
            if p.val < val:
                p = p.right
            elif p.val > val:
                p = p.left
            else:
                return p
        return None

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [4,2,7,1,3], val = 2')
    print('Exception :')
    print('[2,1,3]')
    print('Output :')
    print(str(Solution().searchBST(listToTreeNode([4, 2, 7, 1, 3]), 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [4,2,7,1,3], val = 5')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().searchBST(listToTreeNode([4, 2, 7, 1, 3]), 5)))
    print()

    pass
# @lc main=end