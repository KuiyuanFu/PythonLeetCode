# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#
# https://leetcode.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (46.40%)
# Likes:    3574
# Dislikes: 117
# Total Accepted:    194.7K
# Total Submissions: 418.8K
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# Given a root node reference of a BST and a key, delete the node with the
# given key in the BST. Return the root node reference (possibly updated) of
# the BST.
#
# Basically, the deletion can be divided into two stages:
#
#
# Search for a node to remove.
# If the node is found, delete the node.
#
#
# Follow up: Can you solve it with time complexity O(height of tree)?
#
#
# Example 1:
#
#
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and
# delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's
# also accepted.
#
#
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
#
#
# Example 3:
#
#
# Input: root = [], key = 0
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# Each node has a unique value.
# root is a valid binary search tree.
# -10^5 <= key <= 10^5
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 在二叉搜索树中，删除一个节点。
# 用右子树最左节点代替这个节点，迭代。
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
    def deleteNode(self, root: Optional[TreeNode],
                   key: int) -> Optional[TreeNode]:
        if not root:
            return root

        pseudo = TreeNode(left=root)
        pp, p = pseudo, root
        while p:
            if p.val == key:
                break
            elif p.val > key:
                pp, p = p, p.left
            else:
                pp, p = p, p.right

        def replace(pp, p, pn):
            if pp.left == p:
                pp.left = pn
            elif pp.right == p:
                pp.right = pn

        while p:

            if not p.left:
                pn = p.right
                replace(pp, p, pn)
                break
            elif not p.right:
                pn = p.left
                replace(pp, p, pn)
                break

            po = p
            pp, p = p, p.right
            while p.left:
                pp, p = p, p.left
            po.val = p.val

        return pseudo.left

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [5,3,6,2,4,null,7], key = 3')
    print('Exception :')
    print('[5,4,6,2,null,null,7]')
    print('Output :')
    print(str(Solution().deleteNode([5, 3, 6, 2, 4, null, 7], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [5,3,6,2,4,null,7], key = 0')
    print('Exception :')
    print('[5,3,6,2,4,null,7]')
    print('Output :')
    print(str(Solution().deleteNode([5, 3, 6, 2, 4, null, 7], 0)))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [], key = 0')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().deleteNode([], 0)))
    print()

    pass
# @lc main=end