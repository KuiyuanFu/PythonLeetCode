# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (74.84%)
# Likes:    2063
# Dislikes: 108
# Total Accepted:    213.8K
# Total Submissions: 285.7K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# You are given the root node of a binary search tree (BST) and a value to
# insert into the tree. Return the root node of the BST after the insertion. It
# is guaranteed that the new value does not exist in the original BST.
#
# Notice that there may exist multiple valid ways for the insertion, as long as
# the tree remains a BST after insertion. You can return any of them.
#
#
# Example 1:
#
#
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:
#
#
#
# Example 2:
#
#
# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
#
#
# Example 3:
#
#
# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree will be in the range [0, 10^4].
# -10^8 <= Node.val <= 10^8
# All the values Node.val are unique.
# -10^8 <= val <= 10^8
# It's guaranteed that val does not exist in the original BST.
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 插入搜索二叉树。
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
    def insertIntoBST(self, root: Optional[TreeNode],
                      val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val=val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [4,2,7,1,3], val = 5')
    print('Exception :')
    print('[4,2,7,1,3,5]')
    print('Output :')
    print(str(Solution().insertIntoBST(listToTreeNode([4, 2, 7, 1, 3]), 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [40,20,60,10,30,50,70], val = 25')
    print('Exception :')
    print('[40,20,60,10,30,50,70,null,null,25]')
    print('Output :')
    print(
        str(Solution().insertIntoBST(
            listToTreeNode([40, 20, 60, 10, 30, 50, 70]), 25)))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [4,2,7,1,3,null,null,null,null,null,null], val = 5')
    print('Exception :')
    print('[4,2,7,1,3,5]')
    print('Output :')
    print(
        str(Solution().insertIntoBST(
            listToTreeNode([4, 2, 7, 1, 3, None, None, None, None, None,
                            None]), 5)))
    print()

    pass
# @lc main=end