# @lc app=leetcode id=655 lang=python3
#
# [655] Print Binary Tree
#
# https://leetcode.com/problems/print-binary-tree/description/
#
# algorithms
# Medium (57.48%)
# Likes:    81
# Dislikes: 88
# Total Accepted:    43.8K
# Total Submissions: 75.9K
# Testcase Example:  '[1,2]'
#
# Given the root of a binary tree, construct a 0-indexed m x n string matrix
# res that represents a formatted layout of the tree. The formatted layout
# matrix should be constructed using the following rules:
#
#
# The height of the tree is height and the number of rows m should be equal to
# height + 1.
# The number of columns n should be equal to 2^height+1 - 1.
# Place the root node in the middle of the top row (more formally, at location
# res[0][(n-1)/2]).
# For each node that has been placed in the matrix at position res[r][c], place
# its left child at res[r+1][c-2^height-r-1] and its right child at
# res[r+1][c+2^height-r-1].
# Continue this process until all the nodes in the tree have been placed.
# Any empty cells should contain the empty string "".
#
#
# Return the constructed matrix res.
#
#
# Example 1:
#
#
# Input: root = [1,2]
# Output:
# [["","1",""],
# ["2","",""]]
#
#
# Example 2:
#
#
# Input: root = [1,2,3,null,4]
# Output:
# [["","","","1","","",""],
# ["","2","","","","3",""],
# ["","","4","","","",""]]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 2^10].
# -99 <= Node.val <= 99
# The depth of the tree will be in the range [1, 10].
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 输出二叉树。
# 先找层数。确定间距。宽度为对应层数满二叉树的节点数。
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
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        sl = [[root]]
        while True:
            snn = []
            for p in sl[-1]:
                if p:
                    snn.append(p.left)
                    snn.append(p.right)
                else:
                    snn.append(None)
                    snn.append(None)
            if snn.count(None) == len(snn):
                break
            else:
                sl.append(snn)
        length = len(sl)
        res = []
        for i in reversed(range(length)):
            r = []
            d = 2**i - 1
            for p in sl[-1 - i]:
                r += [''] * d
                r.append(str(p.val) if p else '')
                r += [''] * (d + 1)
            r.pop()
            res.append(r)
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().printTree(
            listToTreeNode([3, 1, 5, 0, 2, 4, 6, None, None, None, 3]))))
    print('Example 1:')
    print('Input : ')
    print('root = [1,2]')
    print('Exception :')
    print('[["","1",""],["2","",""]]')
    print('Output :')
    print(str(Solution().printTree(listToTreeNode([1, 2]))))
    print()

    print('Example 2:')
    print('Input : ')
    print('root = [1,2,3,null,4]')
    print('Exception :')
    print(
        '[["","","","1","","",""],["","2","","","","3",""],["","","4","","","",""]]'
    )
    print('Output :')
    print(str(Solution().printTree(listToTreeNode([1, 2, 3, None, 4]))))
    print()

    pass
# @lc main=end