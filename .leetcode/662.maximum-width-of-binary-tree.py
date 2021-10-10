# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (39.46%)
# Likes:    2841
# Dislikes: 461
# Total Accepted:    127.5K
# Total Submissions: 322.5K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# Given the root of a binary tree, return the maximum width of the given tree.
#
# The maximum width of a tree is the maximum width among all levels.
#
# The width of one level is defined as the length between the end-nodes (the
# leftmost and rightmost non-null nodes), where the null nodes between the
# end-nodes are also counted into the length calculation.
#
# It is guaranteed that the answer will in the range of 32-bit signed
# integer.
#
#
# Example 1:
#
#
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4
# (5,3,null,9).
#
#
# Example 2:
#
#
# Input: root = [1,3,null,5,3]
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2
# (5,3).
#
#
# Example 3:
#
#
# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2
# (3,2).
#
#
# Example 4:
#
#
# Input: root = [1,3,2,5,null,null,9,6,null,null,7]
# Output: 8
# Explanation: The maximum width existing in the fourth level with the length 8
# (6,null,null,null,null,null,null,7).
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 3000].
# -100 <= Node.val <= 100
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
#  求数的最大宽度。
# 即左右两侧非空节点间的最大数量，包括空节点。
# 保存每个节点之后的空节点个数。
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        pl = [[None, 0], [root, 0]]
        res = 1
        while len(pl) > 1:
            width = 0
            pln = [[None, 0]]
            for i in range(1, len(pl)):
                p, n = pl[i]
                if p.left:
                    width += 1 + pln[-1][-1]
                    pln.append([p.left, 0])

                else:
                    pln[-1][-1] += 1
                if p.right:
                    width += 1 + pln[-1][-1]
                    pln.append([p.right, 2 * n])

                else:
                    pln[-1][-1] += 2 * n + 1
            width -= pln[0][-1]
            res = max(res, width)
            pl = pln
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,3,2,5,3,null,9]')
    print('Exception :')
    print('4')
    print('Output :')
    print(
        str(Solution().widthOfBinaryTree(
            listToTreeNode([1, 3, 2, 5, 3, None, 9]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,3,null,5,3]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().widthOfBinaryTree(listToTreeNode([1, 3, None, 5,
                                                           3]))))
    print()

    print('Example 3:')
    print('Input : ')
    print('root = [1,3,2,5]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().widthOfBinaryTree(listToTreeNode([1, 3, 2, 5]))))
    print()

    print('Example 4:')
    print('Input : ')
    print('root = [1,3,2,5,null,null,9,6,null,null,7]')
    print('Exception :')
    print('8')
    print('Output :')
    print(
        str(Solution().widthOfBinaryTree(
            listToTreeNode([1, 3, 2, 5, None, None, 9, 6, None, None, 7]))))
    print()

    pass
# @lc main=end