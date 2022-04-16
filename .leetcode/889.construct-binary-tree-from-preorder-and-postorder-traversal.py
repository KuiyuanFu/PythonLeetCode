# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
#
# algorithms
# Medium (69.85%)
# Likes:    1833
# Dislikes: 85
# Total Accepted:    69.7K
# Total Submissions: 99.8K
# Testcase Example:  '[1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]'
#
# Given two integer arrays, preorder and postorder where preorder is the
# preorder traversal of a binary tree of distinct values and postorder is the
# postorder traversal of the same tree, reconstruct and return the binary
# tree.
#
# If there exist multiple answers, you can return any of them.
#
#
# Example 1:
#
#
# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
#
#
# Example 2:
#
#
# Input: preorder = [1], postorder = [1]
# Output: [1]
#
#
#
# Constraints:
#
#
# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# All the values of preorder are unique.
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# All the values of postorder are unique.
# It is guaranteed that preorder and postorder are the preorder traversal and
# postorder traversal of the same binary tree.
#
#
#

# @lc tags=string

# @lc imports=start
from calendar import isleap
from tkinter.font import BOLD
from imports import *

# @lc imports=end

# @lc idea=start
#
# 通过先序和后序构建二叉树。
# 递归，通过先序当前元素在后序中的位置确定左右两子树的范围。
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

    def constructFromPrePost(self, preorder: List[int],
                             postorder: List[int]) -> Optional[TreeNode]:
        pseudo = TreeNode()

        s = {postorder[i]: i for i in range(len(postorder))}

        def recur(p: Optional[TreeNode], isLeft: bool, preIndex: int,
                  postLeft: int, postRight: int):

            v = preorder[preIndex]
            preIndex += 1
            postRight -= 1

            # add
            pn = TreeNode(v)
            if isLeft:
                p.left = pn
            else:
                p.right = pn

            # child
            if postLeft <= postRight:
                postMiddle = s[preorder[preIndex]]

                recur(pn, True, preIndex, postLeft, postMiddle)
                if postMiddle != postRight:
                    recur(pn, False, preIndex + (postMiddle + 1 - postLeft),
                          postMiddle + 1, postRight)

            pass

        recur(pseudo, True, 0, 0, len(preorder) - 1)

        return pseudo.left

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    # print('Example 1:')
    # print('Input : ')
    # print('preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]')
    # print('Exception :')
    # print('[1,2,3,4,5,6,7]')
    # print('Output :')
    # print(
    #     str(Solution().constructFromPrePost([1, 2, 4, 5, 3, 6, 7],
    #                                         [4, 5, 2, 6, 7, 3, 1])))
    # print()

    # print('Example 2:')
    # print('Input : ')
    # print('preorder = [1], postorder = [1]')
    # print('Exception :')
    # print('[1]')
    # print('Output :')
    # print(str(Solution().constructFromPrePost([1], [1])))
    # print()

    print(str(Solution().constructFromPrePost([2, 1], [1, 2])))
    print()

    pass
# @lc main=end