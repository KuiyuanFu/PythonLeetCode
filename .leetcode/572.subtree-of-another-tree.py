# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (44.76%)
# Likes:    4129
# Dislikes: 198
# Total Accepted:    363.8K
# Total Submissions: 811.9K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# Given the roots of two binary trees root and subRoot, return true if there is
# a subtree of root with the same structure and node values of subRoot and
# false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and
# all of this node's descendants. The tree tree could also be considered as a
# subtree of itself.
#
#
# Example 1:
#
#
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -10^4 <= root.val <= 10^4
# -10^4 <= subRoot.val <= 10^4
#
#
#

# @lc tags=tree

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断树是否存在子树，与另一个树结构相同。
# 从底向上判断。
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
    def isSubtree(self, root: Optional[TreeNode],
                  subRoot: Optional[TreeNode]) -> bool:
        def isSame(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            return root.val == subRoot.val and isSame(
                root.left, subRoot.left) and isSame(root.right, subRoot.right)

        def isSub(root: Optional[TreeNode]):
            return isSame(root, subRoot) \
                or (root.left is not None and isSub(root.left)) \
                or (root.right is not None and isSub(root.right))

        return isSub(root)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [3,4,5,1,2], subRoot = [4,1,2]')
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().isSubtree(listToTreeNode([3, 4, 5, 1, 2]),
                                 listToTreeNode([4, 1, 2]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(
        str(Solution().isSubtree(
            listToTreeNode([3, 4, 5, 1, 2, None, None, None, None, 0]),
            listToTreeNode([4, 1, 2]))))
    print()

    pass
# @lc main=end